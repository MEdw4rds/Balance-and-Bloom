// Function to hide messages after a delay
setTimeout(function() {
    let messageContainer = document.getElementById('message-container');
    if (messageContainer) {
        messageContainer.style.display = 'none';
        }
}, 8000);  // Change 5000 to the desired delay time in milliseconds (5000ms = 5 seconds)

