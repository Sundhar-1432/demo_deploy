document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contactForm');
    const responseMessage = document.getElementById('responseMessage');

    contactForm.addEventListener('submit', function(e) {
        // 1. Prevent the default form submission (page reload)
        e.preventDefault();

        // 2. Collect the data
        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            subject: document.getElementById('subject').value,
            message: document.getElementById('message').value
        };

        // 3. Log data to console (Simulating an API call)
        console.log('Form Data Collected:', formData);

        // 4. Show success message to user
        responseMessage.textContent = "Thank you! Your message has been sent.";
        responseMessage.className = "success";

        // 5. Reset the form
        contactForm.reset();

        // 6. Optionally hide the message after 5 seconds
        setTimeout(() => {
            responseMessage.className = "hidden";
        }, 5000);
    });
});