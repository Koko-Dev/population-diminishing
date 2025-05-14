/* ============================================
  🌌 SCRIPT.JS — Sacred Scroll Behavior
  --------------------------------------------
  This file manages interactions, animations,
  and enhancements for the Scroll experience.
============================================ */

/* --------------------------------------------
  🔽 Scroll-down arrow — smooth scroll to next section
  ✨ Fade-in animations — sacred decade reveals
-------------------------------------------- */
document.addEventListener("DOMContentLoaded", () => {
    // Scroll-down behavior
    const scrollDownArrow = document.querySelector(".scroll-down");

    if (scrollDownArrow) {
        scrollDownArrow.addEventListener("click", () => {
            const nextSection = document.querySelector(".scroll-section");
            if (nextSection) {
                nextSection.scrollIntoView({ behavior: "smooth" });
            }
        });
    }

    // Fade-in observer behavior
    const fadeInElements = document.querySelectorAll('.fade-in');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.15 });

    fadeInElements.forEach(el => observer.observe(el));
});


/* --------------------------------------------
  🧭 Optional future features:
  - Section reveal on scroll
  - Sound effects (ambient triggers)
  - Header fade or scroll indicator updates
  - Theme toggle (light/dark, star density)
-------------------------------------------- */