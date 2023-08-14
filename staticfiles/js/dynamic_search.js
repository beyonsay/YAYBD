document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');
    const resultsContainer = document.getElementById('resultsContainer');

    searchInput.addEventListener('input', performSearch);

    function performSearch() {
        const query = searchInput.value;
        if (query.trim() === '') {
            resultsContainer.innerHTML = '';
            return;
        }

        fetch(`/search/?q=${query}`)
            .then(response => response.text())
            .then(data => {
                resultsContainer.innerHTML = data;
            });
    }
});
