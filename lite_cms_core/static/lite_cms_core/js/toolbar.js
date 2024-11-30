document.addEventListener('DOMContentLoaded', function () {
    // Get the elements
    const hideToolbarButtons = document.querySelectorAll('.hide-toolbar');
    const showToolbarButtons = document.querySelectorAll('.show-toolbar');
    const adminLinks = document.querySelectorAll('.admin-link');

    // Add click event to hide-toolbar buttons
    hideToolbarButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            button.style.display = 'none';
            showToolbarButtons.forEach(btn => btn.style.display = 'block');
            adminLinks.forEach(link => link.style.display = 'none');
        });
    });

    // Add click event to show-toolbar buttons
    showToolbarButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            button.style.display = 'none';
            hideToolbarButtons.forEach(btn => btn.style.display = 'block');
            adminLinks.forEach(link => link.style.display = 'block');
        });
    });
});


