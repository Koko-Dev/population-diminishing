/* ============================================
  🌌 SCRIPT.JS — Sacred Scroll Behavior
  --------------------------------------------
  This file manages interactions, animations,
  and enhancements for the Scroll experience.
============================================ */

/* --------------------------------------------
  🔽 Scroll-down arrow — smooth scroll to next section
-------------------------------------------- */
document.addEventListener("DOMContentLoaded", () => {
    const scrollDownArrow = document.querySelector(".scroll-down");

    if (scrollDownArrow) {
        scrollDownArrow.addEventListener("click", () => {
            const nextSection = document.querySelector(".scroll-section");
            if (nextSection) {
                nextSection.scrollIntoView({ behavior: "smooth" });
            }
        });
    }
});

/* --------------------------------------------
  🧭 Optional future features:
  - Section reveal on scroll
  - Sound effects (ambient triggers)
  - Header fade or scroll indicator updates
  - Theme toggle (light/dark, star density)
-------------------------------------------- */