openerp.web_kanban_graph = function (instance) {

/**
 * Kanban widgets: Graph
 *
 */

instance.web_kanban.KanbanGraphWidget = instance.web_kanban.AbstractField.extend({
    className: "oe_kanban_graph",
    height: '507',
    width: '700',
    start: function() {
        var self = this;
        var field_value = JSON.parse(self.field.value);
        var id_dict = _.pluck(field_value, 'id');

        this.$el.append($("<svg id='chart_"+id_dict+"' class='oe_graph'>"));
        this.svg = '#chart_'+id_dict;
        self.bar(field_value);
    },
    bar: function (data) {
        var self = this;
        nv.addGraph(function () {
            var chart = nv.models.discreteBarChart()
                .x(function(d) { return d.label })    //Specify the data accessors.
                .y(function(d) { return d.value })
                .staggerLabels(true)    //Too many bars and not enough room? Try staggering labels.
                .tooltips(true)        //Don't show tooltips
                .showValues(true)       //...instead, show the bar value right on top of each bar.
                .transitionDuration(350);

            d3.select(self.svg)
                .datum(data)
                .call(chart);
            nv.utils.windowResize(chart.update);
            return chart;
        });
    },
});

instance.web_kanban.fields_registry.add("kanban_graph", "instance.web_kanban.KanbanGraphWidget");


}
