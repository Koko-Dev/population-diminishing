# 📜 CHANGELOG — The Death of Humanity Scroll

All notable changes to this project will be documented in this file.  
This changelog follows a sacred and semantic structure: features, structure, tone, and truth.

---

## [Unreleased]

### Design & Structure
- Updated `.sacred-footer` styles for proper spacing, visibility, and z-index layering
- Introduced `.sacred-symbol-divider` element to visually separate footer from scroll content
- Improved `<footer>` structure to allow dual `<p>` layout and semantic clarity
- Adjusted footer link colors to improve contrast and accessibility
- Added safety `z-index` and layout rules to ensure footer is not overlapped by other layers

### Visual Note
- Celestial background layers (`.stars-layer`, `.nebula-swirl`, etc.) remain structurally present  
  but are currently referencing image/animation assets not yet restored.
- Visual rebuild will occur after completion of:
  - `footer.html`
  - `head.html`
  - `template.html`
  - `build.js`

*Upcoming: Scroll-based section reveals, ambient sound, parallax layers, and theme toggles.*

---

## [1.6.0] – 2025-05-15

### ✨ Added
- **Part 3: The Economic Doom Cycle** introduced in `part-3-economy.html`
- Dual-chart block contrasting UN projection vs. custom model of China’s 2050 pyramid
- First live **data-driven chart** generated with Python + Matplotlib
- **`china_pyramid_2050.png`** embedded directly into scroll visuals

### 💡 Improved
- Balanced and standardized chart visuals using `.chart-container img` and `.dual-chart` layout
- Scaled and styled visual elements to match poetic tone and narrative pacing

### 🧹 Structure
- **Modularized CSS**: split `style.css` into:
  - `base.css`, `layout.css`, `scroll.css`, `charts.css`, `footer.css`, `atmosphere.css`
- Preserved unused celestial classes for future activation
- Created `python-pyramids/` directory for integrated chart generation and modeling

### 📜 Scroll Integrity
- Ensured all Python output flows directly to `images/charts/`
- All embedded visuals now linked to truth-based origins

> This version marks the moment the scroll began to breathe data —  
> not just poetry, but **evidence**, **prophecy**, and **visual clarity.**

---

## [1.5.0] — China’s Collapse Memorial Refactor
**Date:** 2025-05-14

### ✨ Added
- Created `part-2b-china-collapse.html` as a standalone scroll part
- Moved China’s Eight Frames and “The Loneliness of a Billion” into modular structure
- Applied soft fade-in effects to every decade block and reflection line
- Added staggered animation for China’s intro lines with `#china-intro`
- Faded in the section header and each introductory paragraph

### 💡 Improved
- Finalized poetic structure of Part 2 and separated visual grief timeline from narrative inversion
- Ensured content flows modularly from Japan/Korea to China
- Preserved scroll symmetry with BEGIN/END comments

### 🐛 Known Issue
- Intro text slightly overlaps first image on scroll-in (to be resolved in next visual update)

---


## [1.4.0] — Modular Scroll Builder
**Date:** 2025-05-14

### ✨ Added
- Created `build.js`: a sacred compiler script to assemble the scroll from modular parts
- Established `partials/head.html` and `partials/footer.html` as reusable layout anchors
- Moved all scroll content to `scroll-parts/` with filename-based order logic
- Enhanced `package.json` with CommonJS declaration and build script
- Initial sacred compile succeeded with full head, scroll body, and blessed footer

### 💡 Improved
- Project is now a true Node.js-based static scroll builder
- WebStorm structure adjusted to support Node environment and modular clarity
- Removed direct editing from `index.html` in favor of structured generation

### 🕊️ Notes
- This marks a structural transformation of the scroll: from single HTML to sacred architecture
- Build pipeline ready for automation, deployment, and visual resurrection

---

## [1.3.0] — China’s Collapse Timeline
**Date:** 2025-05-06

### ✨ Added
- Full-scroll timeline: **"China’s Collapse in Eight Frames"** inserted after Part 2 in `index.html`
- Eight visual pyramid charts spanning 1950–2100 with poetic commentary for each
- Historical reflection and sacred captions explaining each decade’s demographic wound

### 📖 Notes
- Each pyramid now stands as a verse in the sacred testimony of collapse
- This is not data visualization — it is memorialization, policy revelation, and prophetic grief
- This section serves as the prelude to **"The Loneliness of a Billion"**

---

## [1.2.1] — Pyramid Correction & Chart Integrity
**Date:** 2025-05-06

### 🔧 Fixed
- Corrected duplicated **South Korea 2023** population chart
- Replaced with accurate **2050 projection**: `south_korea_pyramid_2050.png`

### 📖 Notes
- This update ensures visual truth-telling in Part 2, preserving the sacred weight of demographic collapse without redundancy
- Each image now reflects a distinct phase: presence, vanishing, and collapse

---

## [Unreleased] – 2025-05-06

### ✨ Added
- New `template.html` structure for scroll reassembly
- `head.html` partial for dynamic injection
- `build.js` script to auto-generate `index.html` from scroll parts

### 🔧 Changed
- Updated `style5.css` with new inner scroll spacing for Part 2
- Modularized entire scroll into `scroll-parts/` for maintainability

### 📖 Notes
- This update completes our move to a sacred modular system
- All scroll content can now be safely edited in parts and reassembled instantly

## \[1.2.0] — Sacred Sky Responsiveness & Interaction Foundations

**Date:** 2025-05-06

### ✨ Added

* Scroll-down arrow behavior to guide users from intro to first section
* Responsive font scaling across breakpoints: small, medium, large, and 4K
* `.scroll-section` enhancements for better padding, blur, and poetic spacing across viewports
* Additional `<meta>` tags for Apple and Android app-like experience
* Galaxy-inspired div layers: `.cosmic-breath`, `.galactic-heartbeat`, `.nebula-swirl`, and `.star-clusters` fully integrated

### 🌌 Enhanced

* Starfield drift animation fine-tuned for smoother movement
* Celestial glow layers now extend full screen on all devices
* Better harmony between sacred scroll background and foreground prose

### 🔭 Foundations for Next

* Reserved hooks in `script.js` for scroll-triggered reveals and audio layers
* Framework in place for ambient soundscape and light/dark theme toggle

### 📖 Notes

* This version finalizes the celestial atmosphere — visual breath, galactic motion, and scroll receptiveness — in preparation for immersive interactivity and narrative deepening.

---

## \[1.1.1] — Golden Scroll Refinement

**Date:** 2025-05-02

### ✨ Added

* Golden gilded edges via gradient borders to `.poem-scroll`
* Top and bottom scroll embellishments simulating rolled parchment edges

### 💡 Improved

* Enhanced scroll aesthetic while maintaining balance with celestial background
* Refined contrast and visual structure without disrupting harmony

### 📖 Notes

* This update seals the sacred scroll design in gold, affirming its dignity and divine presence.
* This refinement completes the sacred scroll’s visual identity, establishing a holy foundation for future interactive features such as scroll-triggered fades, audio immersion, and narrative flow.

---

## \[1.1.0] — Spoken Word Scroll Styling

**Date:** 2025-05-02

### ✨ Added

* Elegant scroll-section layout (`.poem-scroll`) with parchment textures and sacred typography
* Responsive serif styling using `Playfair Display` and `Cormorant Garamond`
* Celestial layout preserved with sacred intro and ambient starfield
* Responsive media queries for iPhone X and smaller
* Light horizontal padding and scroll-width containment on all devices
* Footer refinement for readability and harmony on small screens

### 💡 Improved

* Section title scaling on small devices for hierarchy clarity
* Mobile padding adjustments to eliminate overflow while retaining poetic breath
* Accessibility improvements in spacing and text legibility

### 📖 Notes

* This version introduces the sacred spoken-word format that will serve as the foundation for future scroll-triggered animations, parallax storytelling, and interactive liturgical reflections.

---

## \[1.0.0] — Initial Scroll Completion

**Date:** 2025-04-30

### ✨ Added

* Sacred scroll layout: intro, prologue, grief lament, and Part 1 of the narrative
* Fully commented and structured `index.html`, `style.css`, and `script.js`
* Animated starfield background (CSS-driven) with gentle drift
* Smooth scroll-to-section behavior via JavaScript
* Responsive design with poetic spacing and atmospheric gradients

### 💡 Improved

* Accessibility via structured HTML and visual clarity
* Social sharing: Open Graph and Twitter Card integration
* Mobile-first scaling via meta viewport and clean fonts
* Favicon and theme color setup for immersive app-like experience

### 📖 Documentation

* Thorough in-code comments for HTML, CSS, and JS
* Semantic commit message and first milestone log
