document.getElementById('commentForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    await fetch('/', { method: 'POST', body: formData });
    location.reload();
});
