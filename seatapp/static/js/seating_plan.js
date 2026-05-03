document.addEventListener('DOMContentLoaded', function () {
    const searchIcon = document.getElementById('searchIcon');
    const searchInput = document.getElementById('guestSearch');
    const guestItems = document.querySelectorAll('.guest-item');

    if (searchIcon && searchInput) {
        searchIcon.addEventListener('click', function () {
            searchInput.classList.toggle('active');
            searchInput.focus();
        });

        document.addEventListener('click', function (e) {
            if (!searchIcon.contains(e.target) && !searchInput.contains(e.target)) {
                searchInput.classList.remove('active');
            }
        });

        searchInput.addEventListener('input', function () {
            const searchValue = searchInput.value.toLowerCase();

            guestItems.forEach(function (guest) {
                const guestName = guest.textContent.toLowerCase();

                if (guestName.includes(searchValue)) {
                    guest.style.display = '';
                } else {
                    guest.style.display = 'none';
                }
            });
        });
    }
});