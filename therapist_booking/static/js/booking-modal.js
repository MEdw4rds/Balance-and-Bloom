let deleteModal = document.getElementById('deleteModal');
let form = null;

deleteModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    let button = event.relatedTarget;
    // Extract info from data-* attributes
    let itemId = button.getAttribute('data-item-id');
    // Update the form action with the item ID
    form = document.getElementById('deleteForm' + itemId);
});

document.getElementById('confirmDelete').addEventListener('click', function() {
    if (form) {
        form.submit();
    } else {
        console.error('Form is null');
    }
});
