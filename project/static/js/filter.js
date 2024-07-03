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