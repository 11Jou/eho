document.addEventListener("DOMContentLoaded", function() {
    var popup = document.getElementById("popup");
    var okBtn = document.getElementById("ok-btn");

    // Show the pop-up when the page loads
    popup.classList.add("show");

    okBtn.addEventListener("click", function() {
        popup.classList.add("hide");
        setTimeout(function() {
            popup.style.display = "none";
        }, 500);
    });

    // Close the pop-up when clicking anywhere outside of the pop-up content
    window.addEventListener("click", function(event) {
        if (event.target == popup) {
            popup.classList.add("hide");
            setTimeout(function() {
                popup.style.display = "none";
            }, 500); // Match this time with CSS transition duration
        }
    });
});