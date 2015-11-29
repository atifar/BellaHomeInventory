// Handles the rendering of text area field content that may be HTML
// formatted text. Clicking the render button renders the contents
// from the corresponding text area input field.

// ///////////// Product description /////////////
// Grab the render button
var render_desc_button = document.getElementById('render_desc');

// Set up a listener to render button click
render_desc_button.addEventListener('click', function(e) {
    // Copy the content of the description's 'textarea' element to the render
    // box.
    $('#desc_output_box').html($('#id_description').val());
});

// ///////////// Product short description /////////////
// Grab the render button
var render_sh_desc_button = document.getElementById('render_sh_desc');

// Set up a listener to render button click
render_sh_desc_button.addEventListener('click', function(e) {
    // Copy the content of the short description's 'textarea' element to the
    // render box.
    $('#sh_desc_output_box').html($('#id_short_description').val());
});
