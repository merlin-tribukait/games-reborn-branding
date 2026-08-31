# GAMES REBORN — Brand Identity & Design System v2.0.0

Official 3D Brand Standards, Scalable Vector Graphics, Molecular Components, Calibrated Design Tokens, and Asset Kit for **GAMES REBORN**.

---

## 🚀 Quick Navigation
* **[`BRAND_GUIDEBOOK.html`](./BRAND_GUIDEBOOK.html)**: Interactive Molecular Guidebook, Token Inspector, and Vector Download Hub.
* **[`08_effects_showcase/index.html`](./08_effects_showcase/index.html)**: Interactive Visual FX, 3D Parallax Tilt & Web Audio Sandbox.
* **[`06_design_tokens/brand_tokens.json`](./06_design_tokens/brand_tokens.json)**: Machine-readable Design Tokens JSON for developer handoff.

---

## 📦 Directory Hierarchy
```
games-reborn-branding/
├── 01_vectors_svg/               (100% Scalable Vector SVGs: Master Crest, Lockups, Monochrome)
├── 02_raster_png/                (Multi-resolution PNG cutouts: 16px to 2048px)
├── 03_favicons_app_icons/        (Multi-size favicon.ico, Apple Touch, Android PWA)
├── 04_social_media_kit/          (Calibrated Headers: Twitter/X, OpenGraph, Discord, YouTube)
├── 05_wallpapers_4k/             (4K Desktop 3840x2160, 1080p, Ultrawide)
├── 06_design_tokens/             (JSON tokens, CSS Custom Properties, Tailwind CSS Preset)
├── 07_molecular_components/      (Atoms, Molecules, Organisms, Templates)
├── 08_effects_showcase/          (Live Web Audio Synthesizer, 3D Parallax Tilt & CRT Scanlines)
├── BRAND_GUIDEBOOK.html          (Master Interactive Single-Page Molecular Guidebook)
├── index.html                    (Interactive Showcase Portal)
└── README.md
```

---

## 💻 Developer Handoff
```css
@import url('06_design_tokens/brand_tokens.css');

.brand-crest {
  background: var(--brand-surface);
  border: 1px solid var(--brand-border-glow);
  box-shadow: var(--shadow-glow);
}
```

© 2026 Merlin Tribukait. All rights reserved.
