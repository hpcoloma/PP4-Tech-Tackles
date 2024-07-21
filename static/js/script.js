document.addEventListener('DOMContentLoaded', function () {
    const deleteTicketButtons = document.querySelectorAll('.delete-button');
    const deleteCommentButtons = document.querySelectorAll('.delete-comment-button');

    // Handle ticket deletion
    deleteTicketButtons.forEach(button => {
        button.addEventListener('click', function () {
            const ticketId = this.getAttribute('data-ticket-id');
            const deleteForm = document.getElementById('deleteForm');
            const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));

            deleteForm.action = `/ticket/${ticketId}/delete/`;
            deleteModal.show();
        });
    });

    // Handle comment deletion
    deleteCommentButtons.forEach(button => {
        button.addEventListener('click', function () {
            const commentId = this.getAttribute('data-comment-id');
            const deleteForm = document.getElementById('deleteCommentForm');
            const deleteModal = new bootstrap.Modal(document.getElementById('deleteCommentModal'));
            deleteForm.action = `/comment/${commentId}/delete/`;
            deleteModal.show();
        });
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const editCommentButtons = document.querySelectorAll('.edit-comment-btn');
    const editCommentModal = new bootstrap.Modal(document.getElementById('editCommentModal'));
    // const editCommentForm = document.getElementById('editCommentForm');
    const editCommentId = document.getElementById('editCommentId');
    const editCommentText = document.getElementById('editCommentText');
    editCommentButtons.forEach(button => {
        button.addEventListener('click', function () {
            const commentId = this.getAttribute('data-comment-id');
            const comment = this.getAttribute('data-comment');

            editCommentId.value = commentId;
            editCommentText.value = comment;

            editCommentModal.show();
        });
    });
});