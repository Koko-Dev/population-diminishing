// build.js — Scroll Assembly Script
// -----------------------------------
// This script assembles the final scroll (index.html)
// by weaving together:
//   - head.html (crown of the scroll)
//   - scroll-parts/*.html (sacred story content)
//   - footer.html (closing, symbol, and return link)
/* eslint-env node */



const fs = require('fs');
const path = require('path');

// 🛤 Paths
const outputPath = path.join(__dirname, 'index.html');
const partialsDir = path.join(__dirname, 'partials');
const scrollPartsDir = path.join(__dirname, 'scroll-parts');

// 📜 1. Read Sacred Head and Footer
const head = fs.readFileSync(path.join(partialsDir, 'head.html'), 'utf8');
const footer = fs.readFileSync(path.join(partialsDir, 'footer.html'), 'utf8');

// 📖 2. Read and order the Scroll Parts
const scrollFiles = fs.readdirSync(scrollPartsDir)
    .filter(file => file.endsWith('.html'))
    .sort(); // Alphabetical sort = proper scroll sequence (00-, 01-, part-1, etc.)

const scrollContent = scrollFiles.map(file => {
    const filePath = path.join(scrollPartsDir, file);
    return fs.readFileSync(filePath, 'utf8');
}).join('\n\n');

// 🧵 3. Weave the Scroll Together
const html = `<!DOCTYPE html>
<html lang="en">
${head}
<body>
  <!-- 🌌 Celestial Background -->
  <div class="divs-and-divinity">
    <div class="cosmic-breath"></div>
    <div class="stars-layer"></div>
    <div class="nebula-swirl"></div>
    <div class="star-clusters"></div>
    <div class="galactic-heartbeat"></div>
  </div>
  <div class="stars"></div>

  ${scrollContent}

  ${footer}
</body>
</html>`;

// 🖋️ 4. Write Final Scroll
fs.writeFileSync(outputPath, html, 'utf8');
console.log('✅ Sacred scroll assembled → index.html created.');
