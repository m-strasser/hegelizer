function add_canvas() {
	canvas_id = 1;
	name = 'New canvas';
	data = {};

	canvas = new vis.Network(container, data, options);
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
	options = networks[id]['options'];

	canvas = new vis.Network(container, data, options);
}

function add_branch() {
	if(current != -1) {
		add_node(current, 'New1');
		add_node(current, 'New2');

		network.redraw();
	}
}

function remove_branch() {
	if(current != -1) {
		kids = get_kids(current);

		kids.forEach(function(kid){
			nodes.remove(kid);
		});

		network.redraw();
	}
}

function merge_branch() {
	if(current != -1) {
		kids = get_kids(current);

		if(kids.length > 0) {
			// We have a root node
			merged_id = add_node(current, 'Merged1', false);

			kids.forEach(function(kid) {
				edges.add({ from: kid, to: merged_id });
				edges.add({ from: kid, to: merged_id });
			});
		}

		network.redraw();
	}
}

function add_node(root_id, label_txt, add_edge=true) {
	var child_id = counter + 1;
	counter += 1;

	nodes.add({ id: child_id, label: label_txt, shape: 'box'});

	if(add_edge)
		edges.add({ from: root_id, to: child_id });

	return child_id;
}

function get_kids(id) {
	var edge_ids = network.getConnectedEdges(id);
	var outgoing = [];
	var edge;

	edge_ids.forEach(function(edge_id) {
		edge = edges.get(edge_id);

		if(edge.from == id)
			outgoing.push(edge.to);
	});

	return outgoing;
}

function has_kids(id) {
}

function is_child(id) {
	var suffix = id.slice(-3);

	switch(suffix) {
		case '.ro':
			return false;
			break;
		case '.c1':
			return true;
			break;
		case '.c2':
			return true;
			break;
		default:
			return true;
	}
}

function get_parent(id) {
	var root = id.slice(-4);
	alert(root);
}

