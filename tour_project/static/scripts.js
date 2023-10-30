document.addEventListener("DOMContentLoaded", function() {

    // Функция для отображения сообщений в модальном окне
    function showMessageModal(message) {
        const modalBody = document.querySelector('#errorMessageModal .modal-body p');
        if (modalBody) {
            modalBody.textContent = message;
            // Используя jQuery, показываем модальное окно
            $('#errorMessageModal').modal('show');
        }
    }

    const errorElement = document.querySelector('#errorMessageModal .modal-body p');
    if (errorElement) {
        const errorMessage = errorElement.textContent.trim();
        if (errorMessage) {
            showMessageModal(errorMessage);
        }
    }
});
