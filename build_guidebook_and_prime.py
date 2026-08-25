import os

base_dir = r"G:\Venice"
brand_sys = os.path.join(base_dir, "reborn_3d_brand_system")

# 1. BRAND_GUIDEBOOK.html
guidebook_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DARK REBORN 3D — Official Brand Identity & Design System Guidebook</title>
    <link rel="icon" type="image/png" href="03_app_icons_favicons/favicon-32x32.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;800;900&family=Rajdhani:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="07_design_tokens_and_code/brand_styles.css">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body {
            font-family: var(--dr-font-body);
            background: var(--dr-bg-base);
            color: #e0e4ec;
            font-size: 17px;
            line-height: 1.6;
        }

        /* TOP NAVIGATION */
        .brand-nav {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(6, 7, 9, 0.94);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--dr-border);
            padding: 0 40px;
            height: 75px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .brand-logo-lockup {
            display: flex;
            align-items: center;
            gap: 15px;
            text-decoration: none;
        }
        .brand-logo-lockup img {
            height: 38px;
            filter: drop-shadow(0 0 10px var(--dr-primary-glow));
        }
        .nav-sections {
            display: flex;
            gap: 25px;
        }
        .nav-sections a {
            color: #8f96a3;
            text-decoration: none;
            font-family: var(--dr-font-display);
            font-size: 0.82rem;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            transition: color 0.2s;
        }
        .nav-sections a:hover {
            color: #fff;
        }
        .nav-action-btn {
            background: linear-gradient(135deg, var(--dr-primary), var(--dr-primary-light));
            color: #fff;
            padding: 10px 22px;
            border-radius: 6px;
            font-family: var(--dr-font-display);
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            text-decoration: none;
            font-weight: 700;
            box-shadow: var(--dr-shadow-glow);
        }

        /* HERO HEADER */
        .guide-hero {
            padding: 100px 40px 80px;
            text-align: center;
            background: radial-gradient(circle at 50% 25%, rgba(184, 20, 20, 0.2) 0%, rgba(6, 7, 9, 0.98) 75%);
            border-bottom: 1px solid var(--dr-border);
            position: relative;
        }
        .badge-ver {
            display: inline-block;
            font-family: var(--dr-font-display);
            font-size: 0.8rem;
            letter-spacing: 3px;
            text-transform: uppercase;
            padding: 6px 18px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--dr-border);
            border-radius: 30px;
            color: var(--dr-primary-light);
            margin-bottom: 20px;
        }
        .guide-title {
            font-family: var(--dr-font-display);
            font-size: clamp(2.6rem, 5vw, 4.5rem);
            font-weight: 900;
            letter-spacing: 6px;
            color: #ffffff;
            margin-bottom: 15px;
            text-transform: uppercase;
            text-shadow: 0 0 30px var(--dr-primary-glow);
        }
        .guide-subtitle {
            color: #8f96a3;
            font-size: 1.25rem;
            max-width: 850px;
            margin: 0 auto 40px;
        }
        .quick-jump-chips {
            display: flex;
            gap: 12px;
            justify-content: center;
            flex-wrap: wrap;
        }
        .jump-chip {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--dr-border);
            color: #ccc;
            text-decoration: none;
            padding: 8px 18px;
            border-radius: 20px;
            font-family: var(--dr-font-display);
            font-size: 0.78rem;
            letter-spacing: 1px;
            transition: all 0.25s;
        }
        .jump-chip:hover {
            border-color: var(--dr-primary);
            color: #fff;
            background: rgba(184, 20, 20, 0.15);
            transform: translateY(-2px);
        }

        /* MAIN CONTAINER */
        .guide-container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 80px 40px;
        }

        .guide-section {
            margin-bottom: 120px;
        }
        .section-header-wrap {
            margin-bottom: 45px;
        }
        .section-num {
            font-family: var(--dr-font-display);
            font-size: 0.85rem;
            color: var(--dr-primary-light);
            letter-spacing: 3px;
            text-transform: uppercase;
            display: block;
            margin-bottom: 8px;
        }
        .section-heading {
            font-family: var(--dr-font-display);
            font-size: 2.4rem;
            font-weight: 800;
            color: #ffffff;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 10px;
        }
        .section-lead {
            color: #8f96a3;
            font-size: 1.15rem;
            max-width: 900px;
        }

        /* ASSET MATRIX & CARDS */
        .assets-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 30px;
        }
        .asset-card {
            background: var(--dr-bg-elevated);
            border: 1px solid var(--dr-border);
            border-radius: 16px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            transition: var(--dr-transition);
        }
        .asset-card:hover {
            border-color: var(--dr-primary);
            box-shadow: var(--dr-shadow-glow);
            transform: translateY(-5px);
        }
        .asset-card.wide-2col {
            grid-column: span 2;
        }
        .asset-preview {
            height: 240px;
            background: #090a0d;
            background-image: radial-gradient(rgba(255,255,255,0.06) 1px, transparent 1px);
            background-size: 20px 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 25px;
            border-bottom: 1px solid var(--dr-border);
            position: relative;
        }
        .asset-card.wide-2col .asset-preview {
            height: 320px;
        }
        .asset-preview img {
            max-width: 90%;
            max-height: 90%;
            object-fit: contain;
            transition: transform 0.3s ease;
        }
        .asset-card:hover .asset-preview img {
            transform: scale(1.05);
        }
        .asset-details {
            padding: 25px;
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .asset-title-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        .asset-title {
            font-family: var(--dr-font-display);
            font-size: 1.15rem;
            color: #fff;
        }
        .format-badge {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            padding: 3px 8px;
            border-radius: 4px;
            background: rgba(184, 20, 20, 0.2);
            border: 1px solid rgba(184, 20, 20, 0.4);
            color: #ff4d4d;
            text-transform: uppercase;
        }
        .asset-desc {
            color: #8f96a3;
            font-size: 0.95rem;
            margin-bottom: 20px;
        }
        .asset-btn-bar {
            display: flex;
            gap: 10px;
            align-items: center;
            padding-top: 15px;
            border-top: 1px solid rgba(255,255,255,0.05);
        }
        .btn-download {
            background: rgba(255,255,255,0.04);
            border: 1px solid var(--dr-border);
            color: #fff;
            padding: 8px 16px;
            border-radius: 6px;
            text-decoration: none;
            font-family: var(--dr-font-display);
            font-size: 0.78rem;
            letter-spacing: 1px;
            font-weight: 700;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }
        .btn-download:hover {
            background: var(--dr-primary);
            border-color: var(--dr-primary);
            box-shadow: 0 0 15px var(--dr-primary-glow);
        }

        /* COLOR SYSTEM */
        .color-matrix {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 25px;
        }
        .color-card {
            background: var(--dr-bg-elevated);
            border: 1px solid var(--dr-border);
            border-radius: 14px;
            overflow: hidden;
        }
        .color-bar {
            height: 120px;
            width: 100%;
            position: relative;
        }
        .color-info-body {
            padding: 20px;
        }
        .color-title {
            font-family: var(--dr-font-display);
            font-size: 1.1rem;
            color: #fff;
            margin-bottom: 8px;
        }
        .color-detail-row {
            display: flex;
            justify-content: space-between;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            color: #8f96a3;
            margin-bottom: 6px;
            padding-bottom: 4px;
            border-bottom: 1px solid rgba(255,255,255,0.04);
        }
        .color-detail-row:last-child {
            border-bottom: none;
        }
        .copy-hex {
            color: var(--dr-primary-light);
            cursor: pointer;
            text-decoration: underline;
        }

        /* TYPOGRAPHY */
        .type-hierarchy-box {
            background: var(--dr-bg-elevated);
            border: 1px solid var(--dr-border);
            border-radius: 16px;
            padding: 40px;
        }
        .type-row {
            margin-bottom: 35px;
            padding-bottom: 25px;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }
        .type-row:last-child {
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }
        .type-meta {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8rem;
            color: var(--dr-primary-light);
            margin-bottom: 8px;
        }

        /* MOCKUPS SHOWCASE */
        .mockups-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
        }
        .mockup-item {
            background: var(--dr-bg-elevated);
            border: 1px solid var(--dr-border);
            border-radius: 16px;
            overflow: hidden;
        }
        .mockup-img-wrap {
            width: 100%;
            overflow: hidden;
        }
        .mockup-img-wrap img {
            width: 100%;
            height: auto;
            display: block;
            transition: transform 0.4s ease;
        }
        .mockup-item:hover .mockup-img-wrap img {
            transform: scale(1.03);
        }
        .mockup-desc {
            padding: 25px;
        }
        .mockup-title {
            font-family: var(--dr-font-display);
            font-size: 1.25rem;
            color: #fff;
            margin-bottom: 6px;
        }

        /* CODE & TOKENS */
        .token-code-box {
            background: #08090d;
            border: 1px solid var(--dr-border);
            border-radius: 12px;
            padding: 25px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9rem;
            color: #abb2bf;
            overflow-x: auto;
            line-height: 1.5;
        }

        footer {
            border-top: 1px solid var(--dr-border);
            padding: 60px 40px;
            text-align: center;
            color: #666;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>

<nav class="brand-nav">
    <a href="#" class="brand-logo-lockup">
        <img src="01_vectors_svg/logo_horizontal_wordmark.svg" alt="Dark Reborn 3D">
    </a>
    <div class="nav-sections">
        <a href="#vectors">Vector SVGs</a>
        <a href="#pngs">4K PNGs</a>
        <a href="#colors">Color System</a>
        <a href="#typography">Typography</a>
        <a href="#social">Social Kit</a>
        <a href="#mockups">Mockups</a>
        <a href="#code">Design Tokens</a>
    </div>
    <a href="../reborn_prime_landing_page.html" class="nav-action-btn">Launch Live Landing Page →</a>
</nav>

<header class="guide-hero">
    <span class="badge-ver">Brand Identity & Design System 2.0</span>
    <h1 class="guide-title">Dark Reborn 3D System</h1>
    <p class="guide-subtitle">The definitive, multi-format brand architecture for esports ecosystems, high-performance gaming hardware, digital products, and physical merchandise.</p>
    <div class="quick-jump-chips">
        <a href="#vectors" class="jump-chip">📐 7 Editable Vector SVGs</a>
        <a href="#pngs" class="jump-chip">🖼️ 4K Transparent PNGs</a>
        <a href="#colors" class="jump-chip">🎨 Complete Color Spec</a>
        <a href="#social" class="jump-chip">📱 Omnichannel Social Kit</a>
        <a href="#mockups" class="jump-chip">🏆 Battlestation & Merch Mockups</a>
        <a href="#code" class="jump-chip">💻 CSS & Tailwind Tokens</a>
    </div>
</header>

<main class="guide-container">

    <!-- 1. VECTOR SVGS -->
    <section class="guide-section" id="vectors">
        <div class="section-header-wrap">
            <span class="section-num">01 / Vector Assets</span>
            <h2 class="section-heading">Scalable Vector SVGs</h2>
            <p class="section-lead">Infinitely scalable, resolution-independent vector graphics crafted for Adobe Illustrator, Figma, Inkscape, Laser Engraving, and Web integration.</p>
        </div>

        <div class="assets-grid">
            <div class="asset-card">
                <div class="asset-preview">
                    <img src="01_vectors_svg/logo_primary_3d_lockup.svg" alt="Primary 3D Shield Vector">
                </div>
                <div class="asset-details">
                    <div>
                        <div class="asset-title-row">
                            <h4 class="asset-title">Primary 3D Shield Lockup</h4>
                            <span class="format-badge">SVG Vector</span>
                        </div>
                        <p class="asset-desc">Faceted titanium bevels, neon laser red glow, and GAMES-REBORN wordmark.</p>
                    </div>
                    <div class="asset-btn-bar">
                        <a href="01_vectors_svg/logo_primary_3d_lockup.svg" download class="btn-download">Download SVG ↓</a>
                    </div>
                </div>
            </div>

            <div class="asset-card">
                <div class="asset-preview">
                    <img src="01_vectors_svg/logo_horizontal_wordmark.svg" alt="Horizontal Nav Wordmark">
                </div>
                <div class="asset-details">
                    <div>
                        <div class="asset-title-row">
                            <h4 class="asset-title">Horizontal Header Wordmark</h4>
                            <span class="format-badge">SVG Vector</span>
                        </div>
                        <p class="asset-desc">Optimized wide format for website navigation, live stream overlays, and banners.</p>
                    </div>
                    <div class="asset-btn-bar">
                        <a href="01_vectors_svg/logo_horizontal_wordmark.svg" download class="btn-download">Download SVG ↓</a>
                    </div>
                </div>
            </div>

            <div class="asset-card">
                <div class="asset-preview">
                    <img src="01_vectors_svg/logo_monogram_icon.svg" alt="Monogram Squircle Icon">
                </div>
                <div class="asset-details">
                    <div>
                        <div class="asset-title-row">
                            <h4 class="asset-title">Monogram Squircle Icon</h4>
                            <span class="format-badge">SVG Vector</span>
                        </div>
                        <p class="asset-desc">Pure GR monogram icon for mobile applications, app store icons, and avatars.</p>
                    </div>
                    <div class="asset-btn-bar">
                        <a href="01_vectors_svg/logo_monogram_icon.svg" download class="btn-download">Download SVG ↓</a>
                    </div>
                </div>
            </div>

            <div class="asset-card">
                <div class="asset-preview">
                    <img src="01_vectors_svg/logo_monochrome_white.svg" alt="Monochrome White">
                </div>
                <div class="asset-details">
                    <div>
                        <div class="asset-title-row">
                            <h4 class="asset-title">Monochrome White</h4>
                            <span class="format-badge">SVG Vector</span>
                        </div>
                        <p class="asset-desc">High-contrast solid white line art for dark print, embroidery, and silkscreen.</p>
                    </div>
                    <div class="asset-btn-bar">
                        <a href="01_vectors_svg/logo_monochrome_white.svg" download class="btn-download">Download SVG ↓</a>
                    </div>
                </div>
            </div>

            <div class="asset-card">
                <div class="asset-preview" style="background: #e5e8ef;">
                    <img src="01_vectors_svg/logo_monochrome_black.svg" alt="Monochrome Black">
                </div>
                <div class="asset-details">
                    <div>
                        <div class="asset-title-row">
                            <h4 class="asset-title">Monochrome Black</h4>
                            <span class="format-badge">SVG Vector</span>
                        </div>
                        <p class="asset-desc">Solid black silhouette for white documents, letterheads, and stamps.</p>
                    </div>
                    <div class="asset-btn-bar">
                        <a href="01_vectors_svg/logo_monochrome_black.svg" download class="btn-download">Download SVG ↓</a>
                    </div>
                </div>
            </div>

            <div class="asset-card">
                <div class="asset-preview">
                    <img src="01_vectors_svg/brand_grid_construction.svg" alt="Construction Blueprint Grid">
                </div>
                <div class="asset-details">
                    <div>
                        <div class="asset-title-row">
                            <h4 class="asset-title">Construction Blueprint</h4>
                            <span class="format-badge">SVG Guide</span>
                        </div>
                        <p class="asset-desc">Geometric construction lines, 45° angle guides, and 80px clearspace boundary.</p>
                    </div>
                    <div class="asset-btn-bar">
                        <a href="01_vectors_svg/brand_grid_construction.svg" download class="btn-download">Download SVG ↓</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 2. HIGH RES 4K PNGS -->
    <section class="guide-section" id="pngs">
        <div class="section-header-wrap">
            <span class="section-num">02 / High-Resolution Bitmaps</span>
            <h2 class="section-heading">4K Transparent PNGs & Renders</h2>
            <p class="section-lead">32-bit alpha channel cutouts rendered at up to 4096×4096 resolution for effortless compositing on any background.</p>
        </div>

        <div class="assets-grid">
            <div class="asset-card">
                <div class="asset-preview">
                    <img src="02_transparent_png/primary_logo_4k_transparent.png" alt="4K Transparent Shield">
                </div>
                <div class="asset-details">
                    <div>
                        <div class="asset-title-row">
                            <h4 class="asset-title">Primary 3D Shield (4K)</h4>
                            <span class="format-badge">4096×4096 PNG</span>
                        </div>
                        <p class="asset-desc">Ultra-high detail brushed metallic finish with transparent alpha channel.</p>
                    </div>
                    <div class="asset-btn-bar">
                        <a href="02_transparent_png/primary_logo_4k_transparent.png" download class="btn-download">Download 4K PNG ↓</a>
                        <a href="02_transparent_png/primary_logo_2k_transparent.png" download class="btn-download">2K PNG</a>
                    </div>
                </div>
            </div>

            <div class="asset-card">
                <div class="asset-preview">
                    <img src="02_transparent_png/horizontal_nav_lockup.png" alt="3D Horizontal Lockup">
                </div>
                <div class="asset-details">
                    <div>
                        <div class="asset-title-row">
                            <h4 class="asset-title">3D Horizontal Lockup</h4>
                            <span class="format-badge">1536×768 PNG</span>
                        </div>
                        <p class="asset-desc">Faceted 3D emblem accompanied by GAMES REBORN typography.</p>
                    </div>
                    <div class="asset-btn-bar">
                        <a href="02_transparent_png/horizontal_nav_lockup.png" download class="btn-download">Download PNG ↓</a>
                    </div>
                </div>
            </div>

            <div class="asset-card">
                <div class="asset-preview">
                    <img src="02_transparent_png/crest_shield.png" alt="Angular Cyber Crest">
                </div>
                <div class="asset-details">
                    <div>
                        <div class="asset-title-row">
                            <h4 class="asset-title">Angular Cyber Crest</h4>
                            <span class="format-badge">1536×1536 PNG</span>
                        </div>
                        <p class="asset-desc">High-speed esports badge with ruby underglow.</p>
                    </div>
                    <div class="asset-btn-bar">
                        <a href="02_transparent_png/crest_shield.png" download class="btn-download">Download PNG ↓</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. COLOR SYSTEM -->
    <section class="guide-section" id="colors">
        <div class="section-header-wrap">
            <span class="section-num">03 / Color Architecture</span>
            <h2 class="section-heading">Official Color Palette & Swatches</h2>
            <p class="section-lead">Calibrated specifications across Digital (HEX/RGB/HSL), Print (CMYK), and Physical Production (Pantone Matching System).</p>
        </div>

        <div class="color-matrix">
            <div class="color-card">
                <div class="color-bar" style="background: #b81414;"></div>
                <div class="color-info-body">
                    <h4 class="color-title">Ruby Laser Red</h4>
                    <div class="color-detail-row"><span>HEX:</span><span class="copy-hex" onclick="navigator.clipboard.writeText('#b81414'); alert('Copied #b81414');">#b81414</span></div>
                    <div class="color-detail-row"><span>RGB:</span><span>184, 20, 20</span></div>
                    <div class="color-detail-row"><span>CMYK:</span><span>10, 98, 95, 20</span></div>
                    <div class="color-detail-row"><span>Pantone:</span><span>PMS 186 C</span></div>
                    <div class="color-detail-row"><span>Role:</span><span>Primary Brand Accent</span></div>
                </div>
            </div>

            <div class="color-card">
                <div class="color-bar" style="background: #ff263b;"></div>
                <div class="color-info-body">
                    <h4 class="color-title">Electric Scarlet Flare</h4>
                    <div class="color-detail-row"><span>HEX:</span><span class="copy-hex" onclick="navigator.clipboard.writeText('#ff263b'); alert('Copied #ff263b');">#ff263b</span></div>
                    <div class="color-detail-row"><span>RGB:</span><span>255, 38, 59</span></div>
                    <div class="color-detail-row"><span>CMYK:</span><span>0, 85, 77, 0</span></div>
                    <div class="color-detail-row"><span>Pantone:</span><span>PMS Warm Red C</span></div>
                    <div class="color-detail-row"><span>Role:</span><span>Glow & Laser Highlights</span></div>
                </div>
            </div>

            <div class="color-card">
                <div class="color-bar" style="background: #8f96a3;"></div>
                <div class="color-info-body">
                    <h4 class="color-title">Brushed Steel 3D</h4>
                    <div class="color-detail-row"><span>HEX:</span><span class="copy-hex" onclick="navigator.clipboard.writeText('#8f96a3'); alert('Copied #8f96a3');">#8f96a3</span></div>
                    <div class="color-detail-row"><span>RGB:</span><span>143, 150, 163</span></div>
                    <div class="color-detail-row"><span>CMYK:</span><span>35, 25, 20, 10</span></div>
                    <div class="color-detail-row"><span>Pantone:</span><span>Cool Gray 8 C</span></div>
                    <div class="color-detail-row"><span>Role:</span><span>Metallic Chrome Bevels</span></div>
                </div>
            </div>

            <div class="color-card">
                <div class="color-bar" style="background: #060709;"></div>
                <div class="color-info-body">
                    <h4 class="color-title">Obsidian Deep</h4>
                    <div class="color-detail-row"><span>HEX:</span><span class="copy-hex" onclick="navigator.clipboard.writeText('#060709'); alert('Copied #060709');">#060709</span></div>
                    <div class="color-detail-row"><span>RGB:</span><span>6, 7, 9</span></div>
                    <div class="color-detail-row"><span>CMYK:</span><span>75, 68, 65, 90</span></div>
                    <div class="color-detail-row"><span>Pantone:</span><span>Black 6 C</span></div>
                    <div class="color-detail-row"><span>Role:</span><span>Foundation Background</span></div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. TYPOGRAPHY -->
    <section class="guide-section" id="typography">
        <div class="section-header-wrap">
            <span class="section-num">04 / Typography</span>
            <h2 class="section-heading">Type Hierarchy & Fonts</h2>
            <p class="section-lead">Futuristic geometry meets high-readability esports interface design.</p>
        </div>

        <div class="type-hierarchy-box">
            <div class="type-row">
                <div class="type-meta">DISPLAY / HEADINGS — Orbitron Black 900 (Letter-spacing: 4px–12px)</div>
                <h1 style="font-family: 'Orbitron', sans-serif; font-weight: 900; font-size: 2.8rem; color: #fff; letter-spacing: 6px; text-transform: uppercase;">CONQUER THE REALM. REBORN.</h1>
            </div>
            <div class="type-row">
                <div class="type-meta">SUBHEADINGS / BUTTONS — Orbitron Bold 700 (Letter-spacing: 2px)</div>
                <h3 style="font-family: 'Orbitron', sans-serif; font-weight: 700; font-size: 1.6rem; color: var(--dr-primary-light); letter-spacing: 2px; text-transform: uppercase;">NEXT-GENERATION TOURNAMENT MATCHMAKING</h3>
            </div>
            <div class="type-row">
                <div class="type-meta">BODY COPY — Rajdhani Semi-Bold 600 (Line-height: 1.7)</div>
                <p style="font-family: 'Rajdhani', sans-serif; font-weight: 600; font-size: 1.2rem; color: #bbb; max-width: 900px;">Engineered with aerospace-grade precision and ultra-low latency architecture. Dark Reborn 3D delivers unparalleled competitive edge across all global esports arenas and creator ecosystems.</p>
            </div>
            <div class="type-row">
                <div class="type-meta">MONOSPACE / SYSTEM DATA — JetBrains Mono Regular 400</div>
                <p style="font-family: 'JetBrains Mono', monospace; font-size: 0.95rem; color: #8892a4;">SYSTEM STATUS: ONLINE // EDGE_NODES: 128 // PING: 12ms // PACKET_LOSS: 0.00%</p>
            </div>
        </div>
    </section>

    <!-- 5. REAL-WORLD PRODUCT & BATTLESTATION MOCKUPS -->
    <section class="guide-section" id="mockups">
        <div class="section-header-wrap">
            <span class="section-num">05 / Product Applications</span>
            <h2 class="section-heading">Photorealistic Mockups</h2>
            <p class="section-lead">Studio-rendered mockups showcasing the brand applied to gaming battlestations, apparel, and wide cinematic headers.</p>
        </div>

        <div class="mockups-grid">
            <div class="mockup-item">
                <div class="mockup-img-wrap">
                    <img src="06_merch_and_mockups/mockup_battlestation_desk_setup.png" alt="Battlestation Desk Setup">
                </div>
                <div class="mockup-desc">
                    <h4 class="mockup-title">Cyberpunk Gaming Battlestation</h4>
                    <p style="color:#8f96a3; font-size:0.95rem;">Curved OLED ultrawide monitor displaying the Dark Reborn UI with custom LED liquid cooling PC.</p>
                </div>
            </div>

            <div class="mockup-item">
                <div class="mockup-img-wrap">
                    <img src="06_merch_and_mockups/mockup_esports_jersey_hoodie.png" alt="Esports Jersey & Hoodie">
                </div>
                <div class="mockup-desc">
                    <h4 class="mockup-title">Official Performance Apparel</h4>
                    <p style="color:#8f96a3; font-size:0.95rem;">Black athletic esports jersey and heavyweight hoodie with 3D metallic red chrome chest print.</p>
                </div>
            </div>

            <div class="mockup-item" style="grid-column: span 2;">
                <div class="mockup-img-wrap">
                    <img src="06_merch_and_mockups/mockup_cinematic_5k_header.jpg" alt="5K Wide Cinematic Header">
                </div>
                <div class="mockup-desc">
                    <h4 class="mockup-title">5K Ultra-HD Cinematic Hero Header</h4>
                    <p style="color:#8f96a3; font-size:0.95rem;">5792×2896 master wide banner for full-screen hero headers, conference keynotes, and esports stages.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. CODE & DESIGN TOKENS -->
    <section class="guide-section" id="code">
        <div class="section-header-wrap">
            <span class="section-num">06 / Developer & Designer Handoff</span>
            <h2 class="section-heading">Design Tokens & Code Snippets</h2>
            <p class="section-lead">Ready-to-use JSON design tokens, CSS variables, and Tailwind CSS configuration.</p>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
            <div>
                <h4 style="font-family: var(--dr-font-display); color:#fff; margin-bottom: 15px;">brand_tokens.json</h4>
                <pre class="token-code-box">{
  "brandName": "Dark Reborn 3D",
  "colors": {
    "primary": "#b81414",
    "primaryLight": "#ff263b",
    "titanium3D": "#8f96a3",
    "backgroundBase": "#060709",
    "surfaceCard": "#0f1218"
  },
  "fonts": {
    "display": "'Orbitron', sans-serif",
    "body": "'Rajdhani', sans-serif"
  }
}</pre>
                <div style="margin-top: 15px;">
                    <a href="07_design_tokens_and_code/brand_tokens.json" download class="btn-download">Download JSON Tokens ↓</a>
                </div>
            </div>

            <div>
                <h4 style="font-family: var(--dr-font-display); color:#fff; margin-bottom: 15px;">tailwind.config.js Preset</h4>
                <pre class="token-code-box">module.exports = {
  theme: {
    extend: {
      colors: {
        reborn: {
          red: '#b81414',
          scarlet: '#ff263b',
          titanium: '#8f96a3',
          obsidian: '#060709'
        }
      }
    }
  }
}</pre>
                <div style="margin-top: 15px;">
                    <a href="07_design_tokens_and_code/brand_styles.css" download class="btn-download">Download CSS Stylesheet ↓</a>
                </div>
            </div>
        </div>
    </section>

</main>

<footer>
    <p>© 2026 DARK REBORN 3D Brand System. Created and stored in <code>G:\Venice\reborn_3d_brand_system</code>.</p>
</footer>

</body>
</html>
"""

with open(os.path.join(brand_sys, "BRAND_GUIDEBOOK.html"), "w", encoding="utf-8") as f:
    f.write(guidebook_html)

# Also place a copy at root for immediate convenience
with open(os.path.join(base_dir, "BRAND_GUIDEBOOK.html"), "w", encoding="utf-8") as f:
    f.write(guidebook_html)

print("BRAND_GUIDEBOOK.html generated!")

# 2. Flagship reborn_prime_landing_page.html
prime_landing_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DARK REBORN 3D — Flagship Competitive Gaming & Esports Platform</title>
    <link rel="icon" type="image/png" href="reborn_3d_brand_system/03_app_icons_favicons/favicon-32x32.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;800;900&family=Rajdhani:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="reborn_3d_brand_system/07_design_tokens_and_code/brand_styles.css">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body {
            font-family: var(--dr-font-body);
            background: var(--dr-bg-base);
            color: #e2e6f0;
            overflow-x: hidden;
            font-size: 18px;
            line-height: 1.6;
        }

        /* Top Announcement / Guidebook Bar */
        .top-bar {
            background: #040507;
            border-bottom: 1px solid var(--dr-border);
            padding: 8px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: var(--dr-font-display);
            font-size: 0.78rem;
            letter-spacing: 1.5px;
        }
        .top-bar a {
            color: var(--dr-primary-light);
            text-decoration: none;
            font-weight: 700;
        }
        .top-bar a:hover {
            text-decoration: underline;
        }

        /* Navigation */
        .navbar {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(6, 7, 9, 0.94);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--dr-border);
            padding: 0 50px;
            height: 80px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .nav-brand img {
            height: 42px;
            filter: drop-shadow(0 0 10px var(--dr-primary-glow));
        }
        .nav-links {
            display: flex;
            gap: 35px;
        }
        .nav-links a {
            color: #9aa2b4;
            text-decoration: none;
            font-family: var(--dr-font-display);
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            transition: color 0.25s;
        }
        .nav-links a:hover {
            color: #fff;
        }

        /* HERO */
        .hero {
            position: relative;
            padding: 90px 40px 120px;
            min-height: 95vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            overflow: hidden;
        }
        .hero-bg {
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at 50% 30%, rgba(184, 20, 20, 0.25) 0%, rgba(6, 7, 9, 0.98) 75%);
            z-index: 1;
        }
        .hero-grid {
            position: absolute;
            inset: 0;
            background-image: linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                              linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
            background-size: 60px 60px;
            z-index: 2;
        }
        .hero-content {
            position: relative;
            z-index: 10;
            max-width: 1200px;
            margin: 0 auto;
        }
        .hero-banner-frame {
            width: 100%;
            max-width: 960px;
            margin: 0 auto 35px;
            border-radius: 18px;
            padding: 12px;
            background: rgba(22, 26, 35, 0.6);
            border: 1px solid var(--dr-border);
            box-shadow: 0 0 60px var(--dr-primary-glow);
            backdrop-filter: blur(12px);
        }
        .hero-banner-frame img {
            width: 100%;
            max-height: 420px;
            object-fit: contain;
            border-radius: 12px;
            display: block;
        }
        .hero-title {
            font-family: var(--dr-font-display);
            font-size: clamp(2.8rem, 6.5vw, 5.2rem);
            font-weight: 900;
            letter-spacing: 12px;
            text-transform: uppercase;
            color: #ffffff;
            margin-bottom: 15px;
            text-shadow: 0 0 35px var(--dr-primary-glow);
        }
        .hero-tagline {
            font-size: 1.5rem;
            color: #9aa2b4;
            letter-spacing: 6px;
            text-transform: uppercase;
            font-weight: 600;
            margin-bottom: 45px;
        }
        .hero-buttons {
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
            margin-bottom: 60px;
        }
        .btn-secondary {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--dr-border);
            color: #fff;
            padding: 16px 36px;
            border-radius: 8px;
            font-family: var(--dr-font-display);
            font-size: 0.9rem;
            letter-spacing: 2px;
            text-transform: uppercase;
            text-decoration: none;
            font-weight: 700;
            transition: var(--dr-transition);
        }
        .btn-secondary:hover {
            border-color: var(--dr-primary);
            color: var(--dr-primary-light);
            transform: translateY(-2px);
        }

        /* HARDWARE & SETUP SECTION */
        .battlestation-sec {
            padding: 120px 50px;
            background: var(--dr-bg-surface);
            border-top: 1px solid var(--dr-border);
            border-bottom: 1px solid var(--dr-border);
        }
        .sec-header {
            text-align: center;
            max-width: 800px;
            margin: 0 auto 60px;
        }
        .sec-label {
            color: var(--dr-primary-light);
            font-family: var(--dr-font-display);
            text-transform: uppercase;
            letter-spacing: 3px;
            font-size: 0.85rem;
            font-weight: 700;
            margin-bottom: 10px;
            display: inline-block;
        }
        .sec-title {
            font-family: var(--dr-font-display);
            font-size: clamp(2.2rem, 4.5vw, 3.4rem);
            font-weight: 900;
            color: #fff;
            text-transform: uppercase;
            letter-spacing: 3px;
            margin-bottom: 15px;
        }
        .sec-desc {
            color: #8f96a3;
            font-size: 1.15rem;
        }

        .showcase-dual {
            display: grid;
            grid-template-columns: 1.2fr 0.8fr;
            gap: 40px;
            max-width: 1400px;
            margin: 0 auto;
            align-items: center;
        }
        .showcase-media {
            border-radius: 20px;
            overflow: hidden;
            border: 1px solid var(--dr-border);
            box-shadow: var(--dr-shadow-glow);
        }
        .showcase-media img {
            width: 100%;
            height: auto;
            display: block;
        }
        .showcase-content h3 {
            font-family: var(--dr-font-display);
            font-size: 2rem;
            color: #fff;
            margin-bottom: 15px;
            text-transform: uppercase;
        }
        .showcase-content p {
            color: #8f96a3;
            line-height: 1.8;
            margin-bottom: 25px;
        }
        .spec-list {
            list-style: none;
            margin-bottom: 30px;
        }
        .spec-list li {
            padding: 10px 0;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 1rem;
        }
        .spec-list li strong {
            color: #fff;
            font-family: var(--dr-font-display);
            font-size: 0.9rem;
        }

        /* APPAREL & MERCH SECTION */
        .apparel-sec {
            padding: 120px 50px;
            background: var(--dr-bg-base);
        }

        /* FOOTER */
        .footer {
            background: #040507;
            padding: 80px 50px 40px;
            border-top: 2px solid var(--dr-primary);
        }
        .footer-grid {
            max-width: 1400px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1fr;
            gap: 50px;
        }
        .footer-brand img {
            height: 48px;
            margin-bottom: 20px;
        }
        .footer-links h4 {
            font-family: var(--dr-font-display);
            color: var(--dr-primary-light);
            font-size: 0.95rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 20px;
        }
        .footer-links ul { list-style: none; }
        .footer-links li { margin-bottom: 10px; }
        .footer-links a {
            color: #888;
            text-decoration: none;
            transition: color 0.2s;
        }
        .footer-links a:hover {
            color: #fff;
        }
        .footer-bottom {
            max-width: 1400px;
            margin: 50px auto 0;
            padding-top: 30px;
            border-top: 1px solid rgba(255,255,255,0.05);
            display: flex;
            justify-content: space-between;
            color: #555;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>

<div class="top-bar">
    <div>
        <span>BRAND ARCHITECTURE 2.0 // DARK REBORN 3D</span>
    </div>
    <div>
        <a href="BRAND_GUIDEBOOK.html">📖 View Interactive Brand Guidebook & Download Center →</a>
    </div>
</div>

<nav class="navbar">
    <a href="#" class="nav-brand">
        <img src="reborn_3d_brand_system/01_vectors_svg/logo_horizontal_wordmark.svg" alt="Dark Reborn 3D">
    </a>
    <div class="nav-links">
        <a href="#hardware">Battlestation Setup</a>
        <a href="#apparel">Merchandise</a>
        <a href="BRAND_GUIDEBOOK.html">Brand Kit</a>
        <a href="index.html">All Site Variants</a>
    </div>
    <a href="BRAND_GUIDEBOOK.html" class="dr-btn-primary">Download Brand Kit</a>
</nav>

<section class="hero">
    <div class="hero-bg"></div>
    <div class="hero-grid"></div>
    <div class="hero-content">
        <div class="hero-banner-frame">
            <img src="reborn_3d_brand_system/06_merch_and_mockups/mockup_cinematic_5k_header.jpg" alt="Dark Reborn 3D 5K Header">
        </div>
        <h1 class="hero-title">DARK REBORN</h1>
        <p class="hero-tagline">Play. Build. Conquer. Reborn.</p>
        <div class="hero-buttons">
            <a href="BRAND_GUIDEBOOK.html" class="dr-btn-primary">Open Brand Design System →</a>
            <a href="#hardware" class="btn-secondary">Explore Battlestation</a>
        </div>
    </div>
</section>

<!-- BATTLESTATION HARDWARE -->
<section class="battlestation-sec" id="hardware">
    <div class="sec-header">
        <span class="sec-label">Physical Hardware Ecosystem</span>
        <h2 class="sec-title">The Ultimate Battlestation</h2>
        <p class="sec-desc">Engineered for esports arenas and professional creator streaming rigs.</p>
    </div>

    <div class="showcase-dual">
        <div class="showcase-media">
            <img src="reborn_3d_brand_system/06_merch_and_mockups/mockup_battlestation_desk_setup.png" alt="Battlestation Desk Setup">
        </div>
        <div class="showcase-content">
            <h3>Precision Engineered Rigs</h3>
            <p>From custom CNC-machined titanium PC enclosures with crimson laser cooling lines to low-friction magnetic desk surfaces emblazoned with the faceted 3D GR shield.</p>
            <ul class="spec-list">
                <li>🔴 <strong>OLED Ultrawide Interface:</strong> Custom 240Hz calibrated dashboard HUD</li>
                <li>🛡️ <strong>Titanium CNC Enclosure:</strong> Ruby liquid cooling perimeter</li>
                <li>⌨️ <strong>Optical Hall-Effect Keyboard:</strong> Sub-0.1ms rapid trigger switch latency</li>
            </ul>
            <a href="BRAND_GUIDEBOOK.html#mockups" class="dr-btn-primary">View Full Render Specs</a>
        </div>
    </div>
</section>

<!-- APPAREL MERCH -->
<section class="apparel-sec" id="apparel">
    <div class="sec-header">
        <span class="sec-label">Pro Wear & Streetwear</span>
        <h2 class="sec-title">Official Apparel Collection</h2>
        <p class="sec-desc">High-grade performance esports textiles and luxury heavyweight cotton hoodies.</p>
    </div>

    <div class="showcase-dual" style="grid-template-columns: 0.8fr 1.2fr;">
        <div class="showcase-content">
            <h3>Championship-Grade Merch</h3>
            <p>Featuring heat-pressed high-gloss chrome 3D emblem transfers with reactive laser red edge piping engineered for international stage tournaments.</p>
            <ul class="spec-list">
                <li>✨ <strong>Chrome 3D Chest Crest:</strong> Impact-resistant high-gloss polymer</li>
                <li>🧵 <strong>Breathable Aero-Mesh:</strong> Anti-static tournament jersey blend</li>
                <li>🖤 <strong>Heavyweight 450GSM Hoodie:</strong> Deep obsidian matte cotton</li>
            </ul>
            <a href="BRAND_GUIDEBOOK.html#mockups" class="dr-btn-primary">Download Merch Mockups</a>
        </div>
        <div class="showcase-media">
            <img src="reborn_3d_brand_system/06_merch_and_mockups/mockup_esports_jersey_hoodie.png" alt="Apparel Collection">
        </div>
    </div>
</section>

<footer class="footer">
    <div class="footer-grid">
        <div class="footer-brand">
            <img src="reborn_3d_brand_system/01_vectors_svg/logo_horizontal_wordmark.svg" alt="Dark Reborn">
            <p style="color:#777; font-size:0.95rem; max-width:360px;">The next-generation competitive brand identity system designed for esports championships, gaming hardware, and creator ecosystems.</p>
        </div>
        <div class="footer-links">
            <h4>Brand Package</h4>
            <ul>
                <li><a href="BRAND_GUIDEBOOK.html#vectors">Vector SVGs</a></li>
                <li><a href="BRAND_GUIDEBOOK.html#pngs">4K Transparent PNGs</a></li>
                <li><a href="BRAND_GUIDEBOOK.html#colors">Color Specs & Pantone</a></li>
                <li><a href="BRAND_GUIDEBOOK.html#social">Social Media Kit</a></li>
            </ul>
        </div>
        <div class="footer-links">
            <h4>Site Variants</h4>
            <ul>
                <li><a href="reborn_prime_landing_page.html">Flagship Dark Reborn</a></li>
                <li><a href="variant1_orange_hex.html">Orange Ember Cyber</a></li>
                <li><a href="variant2_red_shield.html">Crimson Shield Esports</a></li>
                <li><a href="index.html">Master Hub</a></li>
            </ul>
        </div>
        <div class="footer-links">
            <h4>Ecosystem</h4>
            <ul>
                <li><a href="#">Tournament Ladder</a></li>
                <li><a href="#">Hardware Store</a></li>
                <li><a href="#">Discord Server</a></li>
                <li><a href="#">Press Kit</a></li>
            </ul>
        </div>
    </div>
    <div class="footer-bottom">
        <p>© 2026 DARK REBORN 3D. All brand rights reserved.</p>
        <p><a href="BRAND_GUIDEBOOK.html" style="color:var(--dr-primary-light); text-decoration:none;">Open Official Brand Guidebook →</a></p>
    </div>
</footer>

</body>
</html>
"""

with open(os.path.join(base_dir, "reborn_prime_landing_page.html"), "w", encoding="utf-8") as f:
    f.write(prime_landing_html)

print("reborn_prime_landing_page.html generated!")
