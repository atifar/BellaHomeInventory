$(function () {
    // If the login was unsuccessful, change the error text color to red.
    if (login_error) {
        $('#login_error').css({'color': 'red'});
    }
});

