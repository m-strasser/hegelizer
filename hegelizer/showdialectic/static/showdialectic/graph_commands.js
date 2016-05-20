function call_from_overlay(f, node) {
	f(node);
	hide_menu();
}

function add_branch(node) {
	add_node(node, 'New1');
	add_node(node, 'New2');

	canvas.redraw();
}

function remove_branch(node) {
	kids = get_kids(node);

	kids.forEach(function(kid){
		nodes.remove(kid);
	});

	canvas.redraw();
}

function merge_branch(node) {
	kids = get_kids(node);

	if(kids.length > 0) {
		// We have a root node
		merged_id = add_node(node, 'Merged1', false);

		kids.forEach(function(kid) {
			edges.add({ from: kid, to: merged_id });
			edges.add({ from: kid, to: merged_id });
		});
	}

	canvas.redraw();
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
	var edge_ids = canvas.getConnectedEdges(id);
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

