

// smooth scroll
$(document).ready(function(){
    $(".navbar .nav-link").on('click', function(event) {

        if (this.hash !== "") {

            event.preventDefault();

            var hash = this.hash;

            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 700, function(){
                window.location.hash = hash;
            });
        } 
    });
}); 
// Wait for the page to fully load
document.addEventListener("DOMContentLoaded", function () {
    // Showthe loading spinner
    const spinner = document.getElementById("loading-spinner");
    spinner.style.display = "flex";

    // Simulate longer loading time
    setTimeout(function () {
        // Once the page is loaded, show the content and hide the spinner
        spinner.style.opacity = "0";
        spinner.style.pointerEvents = "none";
        const aboutContent = document.getElementById("about-content");
        aboutContent.style.opacity = "1";

        // Get all the Learn More buttons
        const learnMoreButtons = document.querySelectorAll(".learn-more-button");
        learnMoreButtons.forEach(function (button) {
            button.addEventListener("click", function () {
                const memberInfo = button.parentElement.querySelector(".member-info p.member-details");
                memberInfo.classList.toggle("hidden");
                if (memberInfo.classList.contains("hidden")) {
                    button.textContent = "Learn More";
                } else {
                    button.textContent = "Hide";
                }
            });
        });
    }, 3000); // Adjust the duration (in milliseconds) as needed
});
