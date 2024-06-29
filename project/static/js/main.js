(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.sticky-top').addClass('shadow-sm').css('top', '0px');
        } else {
            $('.sticky-top').removeClass('shadow-sm').css('top', '-100px');
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: true,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            }
        }
    });
    document.addEventListener("DOMContentLoaded", function () {
        const portfolioFilters = document.getElementById("portfolio-flters");
        const tabs = portfolioFilters.querySelectorAll("li");
    
        tabs.forEach(function (tab) {
            tab.addEventListener("click", function () {
                tabs.forEach(function (tab) {
                    tab.classList.remove("active");
                });
    
                tab.classList.add("active");
    
                const filter = tab.getAttribute("data-filter");
    
                if (filter === "first") {
                    document.querySelectorAll(".data").forEach(function (data) {
                        data.style.display = "block";
                    });
                } else {
                    document.querySelectorAll(".data").forEach(function (data) {
                        data.style.display = "none";
                    });
                    document.querySelectorAll("." + filter.substring(1)).forEach(function (data) {
                        data.style.display = "block";
                    });
                }
            });
        });
        tabs[0].click();
    });
})
(jQuery);

