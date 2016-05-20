function add_canvas() {
	canvas_id = 1;
	name = 'New canvas';
	nodes = new vis.DataSet([
	{
		id: 1,
		label: 'Base Node',
		shape: 'box',
	},
	]);
	edges = new vis.DataSet([{}]);
	data = {
		nodes: nodes,
		edges: edges
	};

	canvas = new vis.Network(container, data, options);
	set_listeners(canvas);

	networks.push({
		"container": container,
		"data": data,
		"options": options,
		"name": name
	});

	$('#canvas_navigation').append('<button type="button" id="canvas_' +
			canvas_id + '" onclick="select_canvas(' + canvas_id +
			');">' + name + '</button>');
}

function select_canvas(id) {
	container = networks[id]['container'];
	data = networks[id]['data'];
	nodes = data.nodes;
	edges = data.edges;
	options = networks[id]['options'];

	canvas = new vis.Network(container, data, options);
	set_listeners(canvas);
}

function set_listeners(canvas) {
	canvas.on("click", function(params) {
		$("#menu").css('display', 'inline');
		current = params.nodes[0];
	});

	canvas.on("doubleClick", function (params) {
		$("#overlay_menu").css('display', 'inline');
		current = params.nodes[0];
	});
}

function hide_menu() {
	$("#overlay_menu").css('display', 'none');
}
