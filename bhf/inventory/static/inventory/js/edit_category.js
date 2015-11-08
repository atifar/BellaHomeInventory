// Handles the rendering of the description field content, which may be HTML
// formatted text.

// Grab the render button, description textarea, output text box
var render_button = document.getElementById("render");

// Set up a listener to render button click
render_button.addEventListener('click', function (e) {
    renderDescription(e);
});

function renderDescription(e) {
    // Grab the content of the description's 'textarea' element
    var description = $("#id_description").html();
    // Decode the encoded HTML content
    var decoded = $("<div/>").html(description).text();
    // Insert the description into the render box
    $('#output_box').html(decoded);
};
