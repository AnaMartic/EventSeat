document.addEventListener('DOMContentLoaded', function () {
    const openModal = document.getElementById('openModal');
    const closeModal = document.getElementById('closeModal');
    const addModal = document.getElementById('addModal');

    const modalAction = document.getElementById('modalAction');
    const eventId = document.getElementById('eventId');
    const usernameInput = document.getElementById('usernameInput');
    const passwordInput = document.getElementById('passwordInput');
    const eventNameInput = document.getElementById('eventNameInput');
    const eventDateInput = document.getElementById('eventDateInput');
    const modalSubmitBtn = document.getElementById('modalSubmitBtn');

    if (openModal && addModal) {
        openModal.addEventListener('click', function (e) {
            e.preventDefault();

            modalAction.value = 'create';
            eventId.value = '';
            usernameInput.value = '';
            passwordInput.value = '';
            eventNameInput.value = '';
            eventDateInput.value = '';
            modalSubmitBtn.textContent = 'Kreiraj';

            addModal.classList.add('active');
        });
    }

    document.querySelectorAll('.edit-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
            modalAction.value = 'edit';
            eventId.value = btn.dataset.id;
            usernameInput.value = btn.dataset.username;
            passwordInput.value = '';
            eventNameInput.value = btn.dataset.name;
            eventDateInput.value = btn.dataset.date;
            modalSubmitBtn.textContent = 'Spremi promjene';

            addModal.classList.add('active');
        });
    });

    if (closeModal && addModal) {
        closeModal.addEventListener('click', function () {
            addModal.classList.remove('active');
        });
    }

    if (addModal) {
        addModal.addEventListener('click', function (e) {
            if (e.target === addModal) {
                addModal.classList.remove('active');
            }
        });
    }
});