from google.refine import refine
import tempfile
import os
import requests
import codecs
import time

class RefineProj:


    def __init__(self, source=None):
        self.refine_server = refine.Refine(server="http://127.0.0.1:3333")
        #the source object will have the project_id of OR
        #if project_id does not exist then createOR

        #check that source exists and is good
        #bad URLS and bad files are not possible

        
        self.source = source

        if not source.ORid:
            self.refineproj = self.createOR(source)
        else:
            self.refineproj = refine.RefineProject(server="http://127.0.0.1:3333", project_id=str(int(self.source.ORid)))



    def getProjectID(self):
        return self.source.ORid


    #depending on how long this takes, it could be a celery call
    def createOR(self, source):

        #download source data and save to temp file
        #add checks for a valid URL or file path
        resp = requests.get(source.url)

        #do the preprocessing funcs here!!!!
        print source.prefuncs
        if (len(source.prefuncs.keys()) > 0):
            print "we have the processing functions in createOR this is where we need to do it"


        
        


        filepath = os.path.join(tempfile.gettempdir(), str(int(time.time())) + ".csv").replace("\\","/")
        with codecs.open(filepath, 'wb', 'utf-8') as f:
            f.write(resp.text)

        #store raw file here with barn


        refineproj = self.refine_server.new_project(project_file=filepath,project_name=self.source.name, separator=',',
                #store_blank_rows=True,
                #store_blank_cells_as_nulls=True
                )

        os.remove(filepath)


        #and save the edited sourcew
        if refineproj.project_id:

            return refineproj
        else:
            return None

    def list_ops_to_json(self, rawops):
        tempjsonobj = {}
        counter = 0
        for rawop in rawops:
            tempjsonobj[str(counter)] = rawop
            counter +=1
        print tempjsonobj
        return tempjsonobj


    def list_ops_to_list(self,jsonops):
        temparray = []
        for jsonindex in jsonops.keys():
            temparray.append(jsonops[jsonindex])
        return temparray





    def get_operations(self):
        return self.list_ops_to_json(self.refineproj.get_operations())


    def get_file(self):
        #apply the operations tot he project and get result
        return self.refineproj.export(export_format='csv')






    def applyOR(self, refineproj):
        if self.openrefine_transformation and self.openrefine_transformation != "":
            import json
            entryobject = json.loads(self.openrefine_transformation)
            operations = []
            print entryobject
            for entry in entryobject['entries']:
                if 'operation' in entry.keys():
                    operations.append(entry['operation'])
            data = {'operations': json.dumps(operations)}
            r = refineproj.do_json("apply-operations", data=data)
            return True
        else:
            return None

    def deleteOR(refineproj=None):
        if not refineproj:
            refiner = refine.RefineProject(server="http://localhost:3333", project_id=int(self.openrefine_projectnumber))
        else:
            refiner = refineproj
        refiner.delete()
        self.openrefine_projectnumber = ""
        self.save()
        return True

    def getUpdatedCSV(asText=True):
        #we may just need to do an explore on the refineproj?
        refineproj = self.createOR()
        self.applyOR(refineproj)
        f = refineproj.export(export_format='csv')
        self.deleteOR(refineproj)
        return f.read()