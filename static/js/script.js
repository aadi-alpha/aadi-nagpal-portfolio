
// Mobile Navigation

const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector("#navLinks");

menuToggle.addEventListener("click", () => {

    const isOpen = navLinks.classList.toggle("open");

    menuToggle.setAttribute(
        "aria-expanded",
        String(isOpen)
    );

});

// Close mobile menu after clicking a link

const navItems = document.querySelectorAll(".nav-link");

navItems.forEach((link) => {

    link.addEventListener("click", () => {

        navLinks.classList.remove("open");

        menuToggle.setAttribute(
            "aria-expanded",
            "false"
        );

    });

});


// Active Navigation Based on Current Section

const sections = document.querySelectorAll("main section[id]");

const observer = new IntersectionObserver(
    (entries) => {

        entries.forEach((entry) => {

            if (!entry.isIntersecting) return;

            navItems.forEach((item) => {

                item.classList.toggle(
                    "active",
                    item.getAttribute("href") ===
                    `#${entry.target.id}`
                );

            });

        });

    },
    {
        rootMargin: "-35% 0px -55% 0px"
    }
);

sections.forEach((section) => {
    observer.observe(section);
});


// Project Link Feedback

const toast = document.querySelector(".toast");

let toastTimer;

document.querySelectorAll("[data-project]").forEach((link) => {

    link.addEventListener("click", (event) => {

        event.preventDefault();

        toast.textContent =
            `${link.dataset.project}: Add your project URL in index.html.`;

        toast.classList.add("show");

        clearTimeout(toastTimer);

        toastTimer = setTimeout(() => {

            toast.classList.remove("show");

        }, 3000);

    });

});


// Dynamic Copyright Year

document.querySelector("#year").textContent =
    new Date().getFullYear();
