document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('.delete-button');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {
            const ticketId = this.getAttribute('data-ticket-id');
            const deleteForm = document.getElementById('deleteForm');
            const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
            
            deleteForm.action = `/ticket/${ticketId}/delete/`;
            
            deleteModal.show();
        });
    });
});
