import os

master_hub_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GAMES-REBORN | Brand Identity System & Site Variants</title>
    <link rel="icon" type="image/png" href="brand_assets/crimson_shield/favicon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;800;900&family=Rajdhani:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #060709;
            --surface: #0d0f14;
            --surface-card: #131720;
            --border: rgba(255, 255, 255, 0.08);
            --text-main: #f0f2f5;
            --text-muted: #8e95a5;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Rajdhani', sans-serif;
            background: var(--bg);
            color: var(--text-main);
            overflow-x: hidden;
            font-size: 17px;
        }

        /* HEADER */
        .hub-header {
            padding: 80px 40px 60px;
            text-align: center;
            background: radial-gradient(circle at 50% 20%, rgba(220, 20, 60, 0.15) 0%, rgba(6, 7, 9, 0.98) 70%);
            border-bottom: 1px solid var(--border);
            position: relative;
        }
        .hub-badge {
            display: inline-block;
            font-family: 'Orbitron', sans-serif;
            font-size: 0.82rem;
            letter-spacing: 3px;
            text-transform: uppercase;
            padding: 6px 18px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border);
            border-radius: 30px;
            color: #ff3344;
            margin-bottom: 20px;
        }
        .hub-title {
            font-family: 'Orbitron', sans-serif;
            font-size: clamp(2.5rem, 5vw, 4.2rem);
            font-weight: 900;
            letter-spacing: 6px;
            color: #fff;
            margin-bottom: 15px;
            text-transform: uppercase;
        }
        .hub-subtitle {
            color: var(--text-muted);
            font-size: 1.25rem;
            max-width: 800px;
            margin: 0 auto 35px;
        }

        /* VARIANTS GRID */
        .variants-container {
            max-width: 1400px;
            margin: -30px auto 80px;
            padding: 0 30px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
            gap: 30px;
            position: relative;
            z-index: 10;
        }
        .variant-card {
            background: var(--surface-card);
            border: 1px solid var(--border);
            border-radius: 20px;
            overflow: hidden;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex;
            flex-direction: column;
            position: relative;
        }
        .variant-card:hover {
            transform: translateY(-8px);
        }
        .variant-card.var-orange:hover {
            border-color: #ff8c00;
            box-shadow: 0 20px 45px rgba(255, 140, 0, 0.25);
        }
        .variant-card.var-crimson:hover {
            border-color: #dc143c;
            box-shadow: 0 20px 45px rgba(220, 20, 60, 0.25);
        }
        .variant-card.var-darkred:hover {
            border-color: #b81414;
            box-shadow: 0 20px 45px rgba(184, 20, 20, 0.3);
        }

        .variant-hero-preview {
            height: 250px;
            background: #090a0d;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 25px;
            border-bottom: 1px solid var(--border);
            position: relative;
            overflow: hidden;
        }
        .variant-hero-preview img {
            max-width: 90%;
            max-height: 90%;
            object-fit: contain;
            transition: transform 0.3s ease;
        }
        .variant-card:hover .variant-hero-preview img {
            transform: scale(1.06);
        }

        .variant-body {
            padding: 30px;
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .variant-meta {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 15px;
        }
        .variant-tag {
            font-family: 'Orbitron', sans-serif;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            padding: 4px 12px;
            border-radius: 6px;
        }
        .var-orange .variant-tag { background: rgba(255, 140, 0, 0.15); color: #ff8c00; border: 1px solid rgba(255, 140, 0, 0.3); }
        .var-crimson .variant-tag { background: rgba(220, 20, 60, 0.15); color: #ff3355; border: 1px solid rgba(220, 20, 60, 0.3); }
        .var-darkred .variant-tag { background: rgba(184, 20, 20, 0.2); color: #ff4d4d; border: 1px solid rgba(184, 20, 20, 0.3); }

        .asset-count {
            font-size: 0.85rem;
            color: #888;
        }
        .variant-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.6rem;
            color: #fff;
            margin-bottom: 10px;
        }
        .variant-desc {
            color: var(--text-muted);
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: 25px;
        }

        .variant-assets-preview-row {
            display: flex;
            gap: 10px;
            margin-bottom: 25px;
            background: rgba(0,0,0,0.3);
            padding: 10px;
            border-radius: 10px;
            border: 1px solid var(--border);
        }
        .thumb-mini {
            width: 48px;
            height: 48px;
            object-fit: contain;
            background: #000;
            border-radius: 6px;
            padding: 4px;
            border: 1px solid rgba(255,255,255,0.06);
        }

        .btn-launch {
            display: block;
            text-align: center;
            padding: 16px;
            border-radius: 10px;
            font-family: 'Orbitron', sans-serif;
            font-size: 0.9rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
            text-decoration: none;
            color: #fff;
            transition: all 0.3s ease;
        }
        .var-orange .btn-launch {
            background: linear-gradient(135deg, #ff8c00, #ff4500);
            box-shadow: 0 4px 20px rgba(255, 140, 0, 0.3);
        }
        .var-crimson .btn-launch {
            background: linear-gradient(135deg, #dc143c, #ff1e42);
            box-shadow: 0 4px 20px rgba(220, 20, 60, 0.3);
        }
        .var-darkred .btn-launch {
            background: linear-gradient(135deg, #b81414, #e62222);
            box-shadow: 0 4px 20px rgba(184, 20, 20, 0.35);
        }
        .btn-launch:hover {
            transform: translateY(-2px);
            filter: brightness(1.15);
        }

        /* DIRECTORY MATRIX SECTION */
        .matrix-section {
            padding: 60px 40px;
            max-width: 1400px;
            margin: 0 auto;
        }
        .matrix-header {
            text-align: center;
            margin-bottom: 40px;
        }
        .matrix-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 2.2rem;
            color: #fff;
            text-transform: uppercase;
            margin-bottom: 10px;
        }
        .matrix-desc {
            color: var(--text-muted);
            font-size: 1.1rem;
        }

        .matrix-table-wrap {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 16px;
            overflow-x: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            text-align: left;
        }
        th, td {
            padding: 18px 24px;
            border-bottom: 1px solid var(--border);
        }
        th {
            font-family: 'Orbitron', sans-serif;
            font-size: 0.82rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            color: #aaa;
            background: rgba(255,255,255,0.02);
        }
        td {
            font-size: 0.95rem;
        }
        tr:hover td {
            background: rgba(255,255,255,0.02);
        }
        .asset-link {
            color: #fff;
            text-decoration: none;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        .asset-link:hover {
            color: #ff3344;
            text-decoration: underline;
        }

        footer {
            text-align: center;
            padding: 50px 20px;
            color: #666;
            font-size: 0.9rem;
            border-top: 1px solid var(--border);
        }
    </style>
</head>
<body>

<header class="hub-header">
    <span class="hub-badge">Brand Architecture & Design System</span>
    <h1 class="hub-title">GAMES-REBORN Brand Hub</h1>
    <p class="hub-subtitle">Three comprehensive site brandings, customized dark/orange/red logo suites, brand guideline systems, and interactive dummy landing pages.</p>
</header>

<main class="variants-container">
    <!-- VARIANT 1: ORANGE EMBER -->
    <div class="variant-card var-orange">
        <div class="variant-hero-preview">
            <img src="brand_assets/orange_ember/01_primary_logo.png" alt="Orange Ember Primary Mark">
        </div>
        <div class="variant-body">
            <div>
                <div class="variant-meta">
                    <span class="variant-tag">Site Variant 1</span>
                    <span class="asset-count">8 Brand Assets</span>
                </div>
                <h2 class="variant-title">Orange Ember Cyber</h2>
                <p class="variant-desc">High-energy cybernetic aesthetic utilizing radiant amber neon, hexagon geometry, and high-visibility digital esports branding.</p>
                <div class="variant-assets-preview-row">
                    <img src="brand_assets/orange_ember/01_primary_logo.png" class="thumb-mini" title="Primary Logo">
                    <img src="brand_assets/orange_ember/04_shield_crest.png" class="thumb-mini" title="Shield Crest">
                    <img src="brand_assets/orange_ember/05_horizontal_wordmark.png" class="thumb-mini" title="Nav Wordmark">
                    <img src="brand_assets/orange_ember/06_roundel_badge.png" class="thumb-mini" title="Roundel Badge">
                    <img src="brand_assets/orange_ember/02_app_icon.png" class="thumb-mini" title="App Icon">
                    <img src="brand_assets/orange_ember/03_monochrome_white.png" class="thumb-mini" title="Monochrome">
                </div>
            </div>
            <a href="variant1_orange_hex.html" class="btn-launch">Launch Orange Ember Site →</a>
        </div>
    </div>

    <!-- VARIANT 2: CRIMSON SHIELD -->
    <div class="variant-card var-crimson">
        <div class="variant-hero-preview">
            <img src="brand_assets/crimson_shield/01_primary_logo.png" alt="Crimson Shield Primary Mark">
        </div>
        <div class="variant-body">
            <div>
                <div class="variant-meta">
                    <span class="variant-tag">Site Variant 2</span>
                    <span class="asset-count">11 Brand Assets</span>
                </div>
                <h2 class="variant-title">Crimson Shield Esports</h2>
                <p class="variant-desc">Aggressive tournament styling with glowing scarlet shields, spiky crown emblems, business card stationery, and apparel mockups.</p>
                <div class="variant-assets-preview-row">
                    <img src="brand_assets/crimson_shield/01_primary_logo.png" class="thumb-mini" title="Primary Shield">
                    <img src="brand_assets/crimson_shield/04_spiky_crest.png" class="thumb-mini" title="Spiky Crest">
                    <img src="brand_assets/crimson_shield/05_horizontal_wordmark.png" class="thumb-mini" title="Horizontal Wordmark">
                    <img src="brand_assets/crimson_shield/08_winged_badge.png" class="thumb-mini" title="Winged Badge">
                    <img src="brand_assets/crimson_shield/07_business_card_mockup.png" class="thumb-mini" title="Business Card">
                    <img src="brand_assets/crimson_shield/09_apparel_tshirt_mockup.png" class="thumb-mini" title="T-Shirt Merch">
                </div>
            </div>
            <a href="variant2_red_shield.html" class="btn-launch">Launch Crimson Shield Site →</a>
        </div>
    </div>

    <!-- VARIANT 3: DARK REBORN 3D -->
    <div class="variant-card var-darkred">
        <div class="variant-hero-preview">
            <img src="brand_assets/dark_reborn/01_primary_3d_shield.jpg" alt="Dark Reborn 3D Shield">
        </div>
        <div class="variant-body">
            <div>
                <div class="variant-meta">
                    <span class="variant-tag">Site Variant 3</span>
                    <span class="asset-count">9 Brand Assets</span>
                </div>
                <h2 class="variant-title">Dark Reborn 3D Metallic</h2>
                <p class="variant-desc">Ultra-premium brushed steel, beveled 3D lockups, cinematic full-width 5K hero headers, and gothic cyberpunk dark red accents.</p>
                <div class="variant-assets-preview-row">
                    <img src="brand_assets/dark_reborn/01_primary_3d_shield.jpg" class="thumb-mini" title="3D Shield">
                    <img src="brand_assets/dark_reborn/05_metallic_crest.png" class="thumb-mini" title="Metallic Crest">
                    <img src="brand_assets/dark_reborn/06_metallic_wordmark.png" class="thumb-mini" title="3D Wordmark">
                    <img src="brand_assets/dark_reborn/07_horizontal_lockup.png" class="thumb-mini" title="Horizontal 3D">
                    <img src="brand_assets/dark_reborn/08_wing_badge.png" class="thumb-mini" title="Wing Badge">
                    <img src="brand_assets/dark_reborn/02_app_icon.png" class="thumb-mini" title="App Icon">
                </div>
            </div>
            <a href="variant3_dark_red.html" class="btn-launch">Launch Dark Reborn 3D Site →</a>
        </div>
    </div>
</main>

<section class="matrix-section">
    <div class="matrix-header">
        <h2 class="matrix-title">Asset Inventory & Direct Links</h2>
        <p class="matrix-desc">Comprehensive index of all generated landing pages, logo suites, and high-resolution brand artifacts.</p>
    </div>

    <div class="matrix-table-wrap">
        <table>
            <thead>
                <tr>
                    <th>Brand Variant</th>
                    <th>Landing Page</th>
                    <th>Primary Color</th>
                    <th>Key Logo Assets</th>
                    <th>Quick Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Orange Ember</strong></td>
                    <td><a href="variant1_orange_hex.html" class="asset-link">variant1_orange_hex.html ↗</a></td>
                    <td><span style="color:#ff8c00; font-weight:700;">#ff8c00 (Amber)</span></td>
                    <td>Hexagon Mark, Shield Crest, Nav Wordmark, Roundel Seal, App Icon, Banner</td>
                    <td><a href="variant1_orange_hex.html#brand-kit" class="asset-link">View Suite →</a></td>
                </tr>
                <tr>
                    <td><strong>Crimson Shield</strong></td>
                    <td><a href="variant2_red_shield.html" class="asset-link">variant2_red_shield.html ↗</a></td>
                    <td><span style="color:#dc143c; font-weight:700;">#dc143c (Crimson)</span></td>
                    <td>Crimson Shield, Spiky Crown, Header Wordmark, Winged Crest, Card & Shirt Mockups</td>
                    <td><a href="variant2_red_shield.html#brand-kit" class="asset-link">View Suite →</a></td>
                </tr>
                <tr>
                    <td><strong>Dark Reborn 3D</strong></td>
                    <td><a href="variant3_dark_red.html" class="asset-link">variant3_dark_red.html ↗</a></td>
                    <td><span style="color:#b81414; font-weight:700;">#b81414 (Dark Red)</span></td>
                    <td>3D Metallic Shield, 5K Wide Header, 3D Logotype, Angular Crest, Cyber Wing</td>
                    <td><a href="variant3_dark_red.html#brand-kit" class="asset-link">View Suite →</a></td>
                </tr>
            </tbody>
        </table>
    </div>
</section>

<footer>
    <p>© 2026 GAMES-REBORN Branding System. All brand files generated and hosted in <code>G:\Venice</code>.</p>
</footer>

</body>
</html>
"""

with open(r"G:\Venice\index.html", "w", encoding="utf-8") as f:
    f.write(master_hub_html)

print("Master Hub index.html created successfully!")
