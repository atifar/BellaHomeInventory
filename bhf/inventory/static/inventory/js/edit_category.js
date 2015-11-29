// Handles the rendering of text area field content that may be HTML
// formatted text. Clicking the render button renders the contents
// from the corresponding text area input field.

// ///////////// Category description /////////////
// Grab the render button, description textarea, output text box
var render_button = document.getElementById('render');

// Set up a listener to render button click
render_button.addEventListener('click', function(e) {
    renderDescription(e);
});

function renderDescription(e) {
    // Grab the content of the description's 'textarea' element
    var description = $('#id_description').val();
    // Insert the description into the render box
    $('#output_box').html(description);
};
