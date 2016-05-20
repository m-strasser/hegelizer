function call_from_overlay(f, node) {
	f(node);
	hide_menu();
	overlay_menu_visible = false;
}

function add_branch(id) {
	add_node(id, 'New1');
	add_node(id, 'New2');
	node = nodes.get(id);
	node.split = true;
	nodes.update(node);

	canvas.redraw();
}

function remove_branch(node) {
	kids = get_kids(node);

	kids.forEach(function(kid){
		nodes.remove(kid);
	});

	canvas.redraw();
}

function merge_branch(id) {
	leafs = get_leafs(id);

	if(!leafs){
		alert("Unable to merge.");
		return false;
	}

	// We have a root node
	merged_id = add_node(id, 'Merged1', false);

	leafs.forEach(function(leaf) {
		edges.add({ from: leaf, to: merged_id });
		edges.add({ from: leaf, to: merged_id });
	});

	node = nodes.get(id);
	node.merged = merged_id;
	nodes.update(node);

	canvas.redraw();
}

/**
 * Checks if the dialectic is ready for merging (meaning that the level of
 * splits and merges are the same on each branch of the contradiction.
 * @param {int} id - The id of the node that shall be checked.
 * @return - False if not ready for merge, the 2 IDs otherwise.
 */
function get_leafs(id, level=0) {
	node = nodes.get(id);

	// If node is not split, there's nothing to do.
	if(!node.split) return id;
	if(!node.merged && level > 0) return false;
	// If node is already merged, jump to the merged node.
	if(node.merged) return get_leafs(node.merged, level);

	kids = get_kids(id);
	path_1 = get_leafs(kids[0], level+1);
	path_2 = get_leafs(kids[1], level+1);

	if(!path_1 || !path_2) return false;
	return [path_1, path_2];
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

function add_node(root_id, label_txt, add_edge=true) {
	var child_id = counter + 1;
	counter += 1;

	nodes.add({
		id: child_id,
		label: label_txt,
		shape: 'box',
		merged: false,
		split: false
		synonyms: [],
	});

	if(add_edge)
		edges.add({ from: root_id, to: child_id });

	return child_id;
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

