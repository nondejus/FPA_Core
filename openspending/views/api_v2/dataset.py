import logging

from flask import Blueprint, request
from flask.ext.login import current_user
from flask.ext.babel import gettext as _
from colander import SchemaNode, String, Invalid
from restpager import Pager

from openspending.core import db
from openspending.model import Dataset
from openspending.auth import require
from openspending.lib import solr_util as solr
from openspending.lib.jsonexport import jsonify
from openspending.lib.helpers import get_dataset
from openspending.lib.indices import clear_index_cache
from openspending.views.cache import etag_cache_keygen
from openspending.views.context import api_form_data
from openspending.views.error import api_json_errors
from openspending.validation.model.dataset import dataset_schema
from openspending.validation.model.common import ValidationState


log = logging.getLogger(__name__)
blueprint = Blueprint('datasets_api2', __name__)


@blueprint.route('/datasets')
@api_json_errors
def index():
    #page = request.args.get('page')
    fields = request.args.get('fields', "").split(",")

    q = Dataset.all_by_account(current_user).all()

    if len(fields) < 1:
        return jsonify(q)

    #this can be done better
    returnset = []
    for obj in q:
        obj_dict = obj.as_dict()
        tempobj = {}
        for field in fields:
            if field in obj_dict.keys():
                tempobj[field] = obj_dict[field]
        returnset.append(tempobj) 



    # TODO: Facets for territories and languages
    # TODO: filters on facet dimensions
    #maybe put the pager back in
    # print q
    # pager = Pager(q)
    return jsonify(returnset)


@blueprint.route('/datasets/<name>')
@api_json_errors
def view(name):
    dataset = get_dataset(name)
    etag_cache_keygen(dataset)
    return jsonify(dataset)


@blueprint.route('/datasets/<name>/model')
@api_json_errors
def model(name):
    dataset = get_dataset(name)
    etag_cache_keygen(dataset)
    return jsonify(dataset.mapping)


@blueprint.route('/datasets/<name>/fields')
@api_json_errors
def fields(name):
    dataset = get_dataset(name)
    etag_cache_keygen(dataset)
    return jsonify(dataset.fields)


@blueprint.route('/datasets', methods=['POST', 'PUT'])
@api_json_errors
def create():
    """
    This takes a json format post with label, name, description
    and creates a private dataset to put sources in
    The json_errors return a json object
    """

    if not auth.dataset.create():
        return jsonify({"errors":["Can not create new dataset.  Permission denied"]})

    try:
        dataset = api_form_data()
        model = {'dataset': dataset}
        schema = dataset_schema(ValidationState(model))
        data = schema.deserialize(dataset)
        if Dataset.by_name(data['name']) is not None:
            return jsonify({"errors":["A dataset with this name already exists"]})
        dataset = Dataset({'dataset': data})
        dataset.private = True
        dataset.managers.append(current_user)
        db.session.add(dataset)
        db.session.commit()
        return jsonify({"success":True, "dataset":dataset.name})
    except Exception, e:
        return jsonify({"errors":['Unknown Error has occurred']})



@blueprint.route('/datasets/<name>', methods=['POST', 'PUT'])
@api_json_errors
def update(name):
    dataset = get_dataset(name)
    print dataset
    #TODO
    return jsonify({"Success":"notyet"})
    # require.dataset.update(dataset)
    # schema = dataset_schema(ValidationState(dataset.model_data))
    # data = schema.deserialize(api_form_data())
    # dataset.update(data)
    # db.session.commit()
    # clear_index_cache()
    # return view(name)


@blueprint.route('/datasets/<name>/model', methods=['POST', 'PUT'])
@api_json_errors
def update_model(name):
    dataset = get_dataset(name)
    print dataset
    #TODO
    return jsonify({"Success":"notyet"})
    # require.dataset.update(dataset)
    # model_data = dataset.model_data
    # model_data['mapping'] = api_form_data()
    # schema = mapping_schema(ValidationState(model_data))
    # new_mapping = schema.deserialize(model_data['mapping'])
    # dataset.data['mapping'] = new_mapping
    # db.session.commit()
    # return model(name)


@blueprint.route('/datasets/<name>', methods=['DELETE'])
@api_json_errors
def delete(name):
    dataset = get_dataset(name)
    print dataset
    #TODO
    return jsonify({"Success":"notyet"})
    # require.dataset.update(dataset)

    # dataset.fact_table.drop()
    # db.session.delete(dataset)
    # db.session.commit()
    # clear_index_cache()
    # solr.drop_index(dataset.name)
    # return jsonify({'status': 'deleted'}, status=410)