document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("commentForm");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const formData = new FormData(form);

        const response = await fetch("/", {
            method: "POST",
            body: formData
        });

        if (response.ok) {
            location.reload(); // or dynamically append comment
        } else {
            alert("Failed to submit comment");
        }
    });
});
