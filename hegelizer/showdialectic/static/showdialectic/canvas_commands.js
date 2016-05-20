adding_synonym = false;
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

/**
 * Loads the overlay information for a node and makes the overlay visible.
 * @param {int} id - The ID of the node.
 */
function load_overlay(id) {
	$("#overlay_menu").css('display', 'inline');
	overlay_menu_visible = true;
	$("#overlay_text").html(generate_info(id));
}

/**
 * Gets the information about a node and returns an HTML representation of it.
 * @param {int} id - The ID of the node.
 * @return - HTML description of the node.
 */
function generate_info(id) {
	node = nodes.get(id);
	synonyms = node.synonyms;

	node_name_html = "<h3>" + node.label + "</h3>";
	synonyms_html  = "<h4>Synonyms: ";
	synonyms_html += "<button id='overlay_add_synonym'"
			 +"onclick='add_synonym(" + id + ")'>"
			 +"Add Synonym"
			 +"</button>"
			 +"</h4>";
	synonyms_html += "<ul>";
	synonyms.forEach(function(synonym) {
		synonyms_html += "<li>" + synonym + "</li>";
	});
	synonyms_html += "</ul>";

	return node_name_html + "\n" + synonyms_html;
}

function add_synonym(id) {
	if(adding_synonym) return;

	adding_synonym = true;
	item = add_synonym_html("<input type='text' id='overlay_enter_synonym'></input>");
	item.bind("keydown", function(event) {
		listen_for_enter(event, id);
	});
}

function save_synonym(id) {
	txtInput = $('#overlay_enter_synonym')[0];
	synonym = txtInput.value;
	txtInput.remove();
	item = add_synonym_html("<li>" + synonym + "</li>");

	node = nodes.get(id);
	node.synonyms.push(synonym);
	nodes.update(node);

	adding_synonym = false;
}

/**
 * Adds HTML to the list of synonyms in the overlay.
 * @param {string} html - The HTMl that shall be added.
 * @return - The ul item.
 */
function add_synonym_html(html) {
	item = $('#overlay_text').find('ul');
	synonyms_html = item.html();
	synonyms_html += html;
	item.html(synonyms_html);

	return item;
}

function listen_for_enter(event, id) {
	if(event.keyCode == 13) {
		save_synonym(id);
		return false;
	}

	return true;
}
function set_listeners(canvas) {
	canvas.on("click", function(params) {
		$("#menu").css('display', 'inline');
		current = params.nodes[0];
		if(overlay_menu_visible) hide_menu();
	});

	canvas.on("doubleClick", function (params) {
		current = params.nodes[0];
		load_overlay(current);
	});
}

function hide_menu() {
	$("#overlay_menu").css('display', 'none');
}
