// Handles the rendering of text area field content that may be HTML
// formatted text.

// ///////////// Product description /////////////
// Grab the render button, description textarea, output text box
var render_desc_button = document.getElementById("render_desc");

// Set up a listener to render button click
render_desc_button.addEventListener('click', function (e) {
    renderDescription(e);
});

function renderDescription(e) {
    // Grab the content of the description's 'textarea' element
    var description = $("#id_description").html();
    // Decode the encoded HTML content
    var decoded = $("<div/>").html(description).text();
    // Insert the decoded HTML into the render box
    $('#desc_output_box').html(decoded);
};


// ///////////// Product short description /////////////
// Grab the render button, short description textarea, output text box
var render_sh_desc_button = document.getElementById("render_sh_desc");

// Set up a listener to render button click
render_sh_desc_button.addEventListener('click', function (e) {
    renderShDescription(e);
});

function renderShDescription(e) {
    // Grab the content of the description's 'textarea' element
    var description = $("#id_short_description").html();
    // Decode the encoded HTML content
    var decoded = $("<div/>").html(description).text();
    // Insert the decoded HTML into the render box
    $('#sh_desc_output_box').html(decoded);
};
