!function(){$(function(){});var e=function(){$(".list-group-item").popover({trigger:"hover"}),$(".flip").click(function(){if(a)return a=!1,void 0;$(".flip").css("z-index",10),$(this).css("z-index",1e3),$(".flip").find("div.list-group").removeClass("shadow"),$(this).find("div.list-group").addClass("shadow");var e=$(this).find(".card").hasClass("flipped");return $(".flip").find(".card").removeClass("flipped"),e||$(this).find(".card").addClass("flipped"),!0})},a=!1,t={selectIndicator:function(){if(!a){var e=arguments[0].label,r=arguments[0].id;t.activeIndicator(e),t.activeIndicatorId(r);var o=t.selectionTracker();o.indicator=!0,o.vizualization=!1,t.selectionTracker(o),$('#vizTabs a[href="#select-vizualization"]').tab("show"),window.loadIndicatorData(r,i)}},selectVizualization:function(e){var a=e;t.activeChart(a);var r=t.selectionTracker();r.indicator=!0,r.vizualization=!0,t.selectionTracker(r),$('#vizTabs a[href="#vizualize"]').tab("show");var o=t.activeData();o.title.text=t.activeIndicator(),o.chart.type=e,o.yAxis.title.text="",$("#viz-container").highcharts(t.activeData())},selectCountry:function(){},expandCategory:function(){a=!0},clearIndicator:function(){var e=t.selectionTracker();e.indicator=!1,t.selectionTracker(e)},clearChart:function(){var e=t.selectionTracker();e.vizualization=!1,t.selectionTracker(e)},selectionTracker:ko.observable({indicator:!1,vizualization:!1}),filterIndicators:function(e,a){var r=(a.charCode,a.currentTarget.value),o=t.indicatorsModelMaster();t.indicatorsModel.removeAll();for(var i in o)o[i].label.toLowerCase().indexOf(r.toLowerCase())>=0&&t.indicatorsModel.push(o[i]);return!0},filterCountries:function(e,a){var r=(a.charCode,a.currentTarget.value),o=t.countriesModelMaster();t.countriesModel.removeAll();for(var i in o)o[i].label.toLowerCase().indexOf(r.toLowerCase())>=0&&t.countriesModel.push(o[i]);return!0},activeIndicator:ko.observable(""),activeIndicatorId:ko.observable(""),activeChart:ko.observable(""),activeData:ko.observable({}),countriesModel:ko.observableArray([]),countriesModelMaster:ko.observableArray([]),categoriesModel:ko.observableArray([]),sourcesModel:ko.observableArray([]),indicatorsModel:ko.observableArray([]),indicatorsModelMaster:ko.observableArray([]),newSearch:ko.observable(!0)},r=function(e){t.countriesModel(e.data),t.countriesModelMaster(_.clone(e.data,!0))},o=function(a){var r=a.data.categories,o=a.data.sources,i=a.data.indicators,c=[],n=[],l=[];for(var s in r.data){var d=_.map(r.data[s].indicators,function(e){var a=(_.get(i,"data[indicatorId].source"),_.get(o,"data[sourceId].label")),t=_.clone(i.data[e],!0);return t.source=a,t.id=e,t}),u={label:r.data[s].label,length:r.data[s].indicators.length,indicators:d,subcategories:[]};c.push(u)}for(var v in o.data){var f=_.map(o.data[v].indicators,function(e){var a=(_.get(o,"data[indicatorId].category"),_.get(o,"data[categoryId].label")),t=_.clone(i.data[e],!0);return t.source=a,t.id=e,t}),b={label:o.data[v].label,length:o.data[v].indicators.length,indicators:f};n.push(b)}for(var h in i.data){{var g=i.data[h];g.source,g.category}g.source=_.get(o,"data[sourceId].label"),g.category=_.get(r,"data[categoryId].label"),g.id=h,l.push(g)}t.categoriesModel(c),t.sourcesModel(n),t.indicatorsModel(l),t.indicatorsModelMaster(_.clone(l,!0)),ko.applyBindings(t),e()};window.loadIndicatorList(window.config.server+window.config.services.categories,o),window.loadCountries("",r);var i=function(e){var a=$("#callback");$("select").multiselect({click:function(e,t){a.text(t.value+" "+(t.checked?"checked":"unchecked"))},beforeopen:function(){a.text("Select about to be opened...")},open:function(){a.text("Select opened!")},beforeclose:function(){a.text("Select about to be closed...")},close:function(){a.text("Select closed!")},checkAll:function(){a.text("Check all clicked!")},uncheckAll:function(){a.text("Uncheck all clicked!")},optgrouptoggle:function(e,t){var r=$.map(t.inputs,function(e){return e.value}).join(", ");a.html("<strong>Checkboxes "+(t.checked?"checked":"unchecked")+":</strong> "+r)}}),$("#slider-years").slider({range:!0,min:1990,max:2013,values:[1994,2015],slide:function(e,a){$("#years-label").val(a.values[0]+" - "+a.values[1])}}),$("#years-label").val($("#slider-years").slider("values",0)+" - "+$("#slider-years").slider("values",1));var r=window.prepareHighchartsJson(e,t.activeIndicator(),t.activeChart(),t.activeIndicatorId());t.activeData(r)}}();