import os

def get_landing_page_html(theme):
    accent = theme["accent"]
    accent_secondary = theme["accent_secondary"]
    accent_glow = theme["accent_glow"]
    title = theme["title"]
    subtitle = theme["subtitle"]
    folder = theme["folder"]
    assets = theme["assets"]
    other_variants = theme["other_variants"]
    
    logo_cards_html = ""
    for item in assets:
        badge_tag = f'<span class="logo-type-badge">{item["type"]}</span>'
        img_class = "logo-card-img"
        if item.get("wide"):
            card_class = "logo-card wide-card"
        else:
            card_class = "logo-card"
            
        logo_cards_html += f"""
        <div class="{card_class}">
            <div class="logo-preview-box">
                <img src="{item['path']}" alt="{item['name']}" class="{img_class}" loading="lazy">
            </div>
            <div class="logo-card-info">
                <div class="logo-card-header">
                    <h4>{item['name']}</h4>
                    {badge_tag}
                </div>
                <p>{item['desc']}</p>
                <div class="logo-card-actions">
                    <span class="dimension-tag">{item['dims']}</span>
                    <a href="{item['path']}" download class="btn-download-sm">View / Download ↓</a>
                </div>
            </div>
        </div>
        """

    colors_html = ""
    for col in theme["colors"]:
        colors_html += f"""
        <div class="color-swatch-card">
            <div class="color-preview" style="background: {col['hex']};"></div>
            <div class="color-info">
                <span class="color-name">{col['name']}</span>
                <span class="color-hex" onclick="navigator.clipboard.writeText('{col['hex']}'); alert('Copied {col['hex']}');">{col['hex']} 📋</span>
                <span class="color-use">{col['use']}</span>
            </div>
        </div>
        """

    switcher_html = ""
    for v in other_variants:
        active_cls = "active" if v["active"] else ""
        switcher_html += f"""
        <a href="{v['url']}" class="variant-pill {active_cls}">
            <span class="pill-dot" style="background: {v['color']};"></span>
            {v['label']}
        </a>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Full Site Branding & Dummy Landing Page</title>
    <link rel="icon" type="image/png" href="{theme['favicon']}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;800;900&family=Rajdhani:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --accent: {accent};
            --accent-sec: {accent_secondary};
            --accent-glow: {accent_glow};
            --bg-dark: #07080a;
            --bg-surface: #0f1115;
            --bg-surface-elevated: #15181f;
            --border-color: rgba(255, 255, 255, 0.08);
            --border-hover: {accent};
            --text-main: #f0f2f5;
            --text-muted: #8e95a5;
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html {{ scroll-behavior: smooth; }}
        body {{
            font-family: 'Rajdhani', sans-serif;
            background: var(--bg-dark);
            color: var(--text-main);
            overflow-x: hidden;
            font-size: 17px;
            line-height: 1.6;
        }}

        /* Brand Variant Bar */
        .brand-switcher-bar {{
            background: rgba(5, 6, 8, 0.95);
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            padding: 10px 40px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-family: 'Orbitron', sans-serif;
            font-size: 0.78rem;
            letter-spacing: 1.5px;
            z-index: 1001;
            position: relative;
        }}
        .brand-switcher-title {{
            color: var(--text-muted);
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .brand-switcher-title strong {{
            color: var(--accent);
        }}
        .variant-pills {{
            display: flex;
            gap: 12px;
        }}
        .variant-pill {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 14px;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            color: #aaa;
            text-decoration: none;
            transition: all 0.25s ease;
        }}
        .variant-pill:hover {{
            color: #fff;
            border-color: var(--accent);
            transform: translateY(-1px);
        }}
        .variant-pill.active {{
            background: rgba(255, 255, 255, 0.08);
            border-color: var(--accent);
            color: #fff;
            box-shadow: 0 0 15px var(--accent-glow);
        }}
        .pill-dot {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
            display: inline-block;
        }}

        /* Navigation */
        .navbar {{
            position: sticky;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            background: rgba(7, 8, 10, 0.92);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border-color);
            padding: 0 50px;
            height: 80px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .nav-brand {{
            display: flex;
            align-items: center;
            gap: 15px;
            text-decoration: none;
        }}
        .nav-logo-img {{
            height: 46px;
            max-width: 200px;
            object-fit: contain;
            border-radius: 6px;
            filter: drop-shadow(0 0 8px var(--accent-glow));
        }}
        .nav-links {{
            display: flex;
            gap: 35px;
        }}
        .nav-links a {{
            color: #a0a6b5;
            text-decoration: none;
            font-family: 'Orbitron', sans-serif;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            transition: all 0.3s;
            position: relative;
        }}
        .nav-links a:hover, .nav-links a.active {{
            color: #fff;
        }}
        .nav-links a::after {{
            content: '';
            position: absolute;
            bottom: -6px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--accent);
            transition: width 0.3s ease;
        }}
        .nav-links a:hover::after {{
            width: 100%;
        }}
        .nav-cta {{
            background: linear-gradient(135deg, var(--accent), var(--accent-sec));
            color: #fff;
            padding: 12px 28px;
            border-radius: 8px;
            font-family: 'Orbitron', sans-serif;
            font-size: 0.82rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
            text-decoration: none;
            transition: all 0.3s;
            border: 1px solid rgba(255,255,255,0.2);
            cursor: pointer;
            box-shadow: 0 4px 20px var(--accent-glow);
        }}
        .nav-cta:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 30px var(--accent);
        }}

        /* Hero Section */
        .hero {{
            min-height: 90vh;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
            padding: 80px 30px;
        }}
        .hero-bg {{
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at 50% 30%, {accent_glow} 0%, rgba(7, 8, 10, 0.98) 70%);
            z-index: 1;
        }}
        .hero-grid {{
            position: absolute;
            inset: 0;
            background-image: linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                              linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
            background-size: 60px 60px;
            z-index: 2;
        }}
        .hero-content {{
            position: relative;
            z-index: 10;
            text-align: center;
            width: 100%;
            max-width: 1100px;
            margin: 0 auto;
        }}
        .hero-image-container {{
            width: 100%;
            max-width: 900px;
            margin: 0 auto 35px;
            border-radius: 16px;
            padding: 15px;
            background: rgba(15, 17, 21, 0.6);
            border: 1px solid var(--border-color);
            box-shadow: 0 0 50px var(--accent-glow);
            backdrop-filter: blur(10px);
            transition: transform 0.4s ease;
        }}
        .hero-image-container:hover {{
            transform: scale(1.01);
            border-color: var(--accent);
        }}
        .hero-image {{
            width: 100%;
            max-height: 380px;
            object-fit: contain;
            display: block;
            border-radius: 12px;
        }}
        .hero-title {{
            font-family: 'Orbitron', sans-serif;
            font-size: clamp(2.5rem, 6vw, 4.8rem);
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 12px;
            line-height: 1.1;
            background: linear-gradient(180deg, var(--text-main) 30%, var(--accent) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 18px;
            filter: drop-shadow(0 0 20px var(--accent-glow));
        }}
        .hero-tagline {{
            font-size: 1.4rem;
            color: var(--text-muted);
            letter-spacing: 6px;
            text-transform: uppercase;
            font-weight: 600;
            margin-bottom: 40px;
        }}
        .hero-buttons {{
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
            margin-bottom: 60px;
        }}
        .btn-primary {{
            background: linear-gradient(135deg, var(--accent), var(--accent-sec));
            color: #fff;
            padding: 18px 45px;
            border-radius: 10px;
            font-family: 'Orbitron', sans-serif;
            font-size: 0.95rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2.5px;
            text-decoration: none;
            transition: all 0.3s;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 6px 25px var(--accent-glow);
            display: inline-flex;
            align-items: center;
            gap: 12px;
        }}
        .btn-primary:hover {{
            transform: translateY(-3px);
            box-shadow: 0 10px 40px var(--accent);
        }}
        .btn-secondary {{
            background: rgba(255, 255, 255, 0.04);
            color: #fff;
            padding: 18px 45px;
            border-radius: 10px;
            font-family: 'Orbitron', sans-serif;
            font-size: 0.95rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2.5px;
            text-decoration: none;
            transition: all 0.3s;
            border: 1px solid var(--border-color);
        }}
        .btn-secondary:hover {{
            border-color: var(--accent);
            color: var(--accent);
            background: rgba(255, 255, 255, 0.08);
            transform: translateY(-3px);
        }}

        .hero-stats {{
            display: flex;
            gap: 50px;
            justify-content: center;
            flex-wrap: wrap;
            padding-top: 30px;
            border-top: 1px solid var(--border-color);
        }}
        .stat {{ text-align: center; }}
        .stat-number {{
            font-family: 'Orbitron', sans-serif;
            font-size: 2.8rem;
            font-weight: 800;
            color: var(--accent);
            text-shadow: 0 0 20px var(--accent-glow);
        }}
        .stat-label {{
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 2px;
            font-size: 0.9rem;
            font-weight: 600;
        }}

        /* SECTION STYLING */
        section {{
            padding: 110px 50px;
            position: relative;
        }}
        .section-header {{
            text-align: center;
            max-width: 800px;
            margin: 0 auto 60px;
        }}
        .section-label {{
            color: var(--accent);
            font-family: 'Orbitron', sans-serif;
            text-transform: uppercase;
            letter-spacing: 4px;
            font-size: 0.85rem;
            font-weight: 700;
            margin-bottom: 12px;
            display: inline-block;
            padding: 4px 14px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border-color);
            border-radius: 20px;
        }}
        .section-title {{
            font-family: 'Orbitron', sans-serif;
            font-size: clamp(2rem, 4vw, 3.2rem);
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 3px;
            color: #fff;
            margin-bottom: 15px;
        }}
        .section-desc {{
            color: var(--text-muted);
            font-size: 1.15rem;
        }}

        /* BRAND LOGO SUITE SHOWCASE SECTION */
        .brand-showcase {{
            background: linear-gradient(180deg, var(--bg-dark), var(--bg-surface) 30%, var(--bg-dark));
            border-top: 1px solid var(--border-color);
            border-bottom: 1px solid var(--border-color);
        }}
        .brand-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 30px;
            max-width: 1400px;
            margin: 0 auto 60px;
        }}
        .logo-card {{
            background: var(--bg-surface-elevated);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            overflow: hidden;
            transition: all 0.35s ease;
            display: flex;
            flex-direction: column;
        }}
        .logo-card:hover {{
            transform: translateY(-6px);
            border-color: var(--border-hover);
            box-shadow: 0 15px 35px var(--accent-glow);
        }}
        .logo-card.wide-card {{
            grid-column: 1 / -1;
        }}
        .logo-preview-box {{
            height: 240px;
            background: #090a0d;
            background-image: radial-gradient(rgba(255,255,255,0.06) 1px, transparent 1px);
            background-size: 20px 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 25px;
            border-bottom: 1px solid var(--border-color);
            position: relative;
        }}
        .logo-card.wide-card .logo-preview-box {{
            height: 340px;
        }}
        .logo-card-img {{
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
            transition: transform 0.3s ease;
        }}
        .logo-card:hover .logo-card-img {{
            transform: scale(1.05);
        }}
        .logo-card-info {{
            padding: 25px;
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .logo-card-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }}
        .logo-card-header h4 {{
            font-family: 'Orbitron', sans-serif;
            font-size: 1.15rem;
            color: #fff;
        }}
        .logo-type-badge {{
            font-size: 0.72rem;
            font-family: 'Orbitron', sans-serif;
            text-transform: uppercase;
            padding: 3px 10px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            color: var(--accent);
        }}
        .logo-card-info p {{
            color: var(--text-muted);
            font-size: 0.95rem;
            margin-bottom: 20px;
        }}
        .logo-card-actions {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 15px;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
        }}
        .dimension-tag {{
            font-size: 0.8rem;
            color: #777;
            font-family: monospace;
        }}
        .btn-download-sm {{
            color: var(--accent);
            text-decoration: none;
            font-family: 'Orbitron', sans-serif;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 1px;
            padding: 6px 14px;
            border-radius: 6px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border-color);
            transition: all 0.2s;
        }}
        .btn-download-sm:hover {{
            background: var(--accent);
            color: #fff;
            border-color: var(--accent);
        }}

        /* COLOR PALETTE & TYPOGRAPHY SECTION */
        .brand-spec-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            max-width: 1400px;
            margin: 0 auto;
        }}
        .spec-box {{
            background: var(--bg-surface-elevated);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 35px;
        }}
        .spec-box h3 {{
            font-family: 'Orbitron', sans-serif;
            font-size: 1.4rem;
            color: #fff;
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .color-palette-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 15px;
        }}
        .color-swatch-card {{
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            overflow: hidden;
        }}
        .color-preview {{
            height: 70px;
            width: 100%;
        }}
        .color-info {{
            padding: 12px;
        }}
        .color-name {{
            display: block;
            font-weight: 700;
            font-size: 0.85rem;
            color: #fff;
        }}
        .color-hex {{
            display: inline-block;
            font-family: monospace;
            font-size: 0.85rem;
            color: var(--accent);
            cursor: pointer;
            margin: 3px 0;
        }}
        .color-use {{
            display: block;
            font-size: 0.75rem;
            color: #777;
        }}

        .type-sample-row {{
            margin-bottom: 25px;
            padding-bottom: 20px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }}
        .type-sample-row:last-child {{
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }}
        .type-font-name {{
            font-size: 0.85rem;
            color: var(--accent);
            font-family: 'Orbitron', sans-serif;
            letter-spacing: 2px;
            margin-bottom: 5px;
            text-transform: uppercase;
        }}
        .type-sample-display {{
            font-family: 'Orbitron', sans-serif;
            font-size: 1.8rem;
            font-weight: 900;
            color: #fff;
            letter-spacing: 2px;
        }}
        .type-sample-body {{
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.15rem;
            color: #bbb;
        }}

        /* FEATURES SECTION */
        .features {{
            padding: 120px 50px;
            background: var(--bg-dark);
        }}
        .features-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
            gap: 30px;
            max-width: 1400px;
            margin: 0 auto;
        }}
        .feature-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 40px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }}
        .feature-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--accent), var(--accent-sec));
            transform: scaleX(0);
            transition: transform 0.3s ease;
        }}
        .feature-card:hover {{
            transform: translateY(-8px);
            border-color: var(--border-hover);
            box-shadow: 0 20px 40px var(--accent-glow);
        }}
        .feature-card:hover::before {{
            transform: scaleX(1);
        }}
        .feature-icon {{
            width: 70px;
            height: 70px;
            background: rgba(255, 255, 255, 0.03);
            border: 2px solid var(--accent);
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.2rem;
            margin-bottom: 25px;
            box-shadow: 0 0 20px var(--accent-glow);
        }}
        .feature-title {{
            font-family: 'Orbitron', sans-serif;
            font-size: 1.4rem;
            color: #fff;
            margin-bottom: 12px;
        }}
        .feature-desc {{
            color: var(--text-muted);
            line-height: 1.7;
        }}

        /* GAMES SECTION */
        .games {{
            padding: 120px 50px;
            background: var(--bg-surface);
        }}
        .games-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            max-width: 1400px;
            margin: 0 auto;
        }}
        .game-card {{
            background: var(--bg-surface-elevated);
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid var(--border-color);
            transition: all 0.3s ease;
        }}
        .game-card:hover {{
            transform: translateY(-6px);
            border-color: var(--accent);
            box-shadow: 0 15px 35px var(--accent-glow);
        }}
        .game-thumb {{
            height: 200px;
            background: #090a0d;
            display: flex;
            align-items: center;
            justify-content: center;
            border-bottom: 1px solid var(--border-color);
            position: relative;
        }}
        .game-badge {{
            font-family: 'Orbitron', sans-serif;
            font-size: 3rem;
            font-weight: 900;
            color: var(--accent);
            text-shadow: 0 0 25px var(--accent-glow);
        }}
        .game-info {{
            padding: 25px;
        }}
        .game-title {{
            font-family: 'Orbitron', sans-serif;
            font-size: 1.25rem;
            color: #fff;
            margin-bottom: 6px;
        }}
        .game-genre {{
            color: var(--accent);
            text-transform: uppercase;
            font-size: 0.8rem;
            letter-spacing: 2px;
            font-weight: 700;
            margin-bottom: 12px;
        }}
        .game-desc {{
            color: var(--text-muted);
            font-size: 0.95rem;
        }}

        /* COMMUNITY & NEWSLETTER */
        .community {{
            padding: 120px 50px;
            background: linear-gradient(180deg, var(--bg-surface), var(--bg-dark));
            text-align: center;
        }}
        .community-box {{
            max-width: 900px;
            margin: 0 auto;
            background: var(--bg-surface-elevated);
            border: 1px solid var(--border-color);
            border-radius: 20px;
            padding: 60px 40px;
            box-shadow: 0 0 50px rgba(0,0,0,0.5);
            position: relative;
            overflow: hidden;
        }}
        .community-box::before {{
            content: '';
            position: absolute;
            top: -150px;
            left: 50%;
            transform: translateX(-50%);
            width: 300px;
            height: 300px;
            background: var(--accent-glow);
            filter: blur(100px);
            border-radius: 50%;
            pointer-events: none;
        }}
        .community-title {{
            font-family: 'Orbitron', sans-serif;
            font-size: 2.8rem;
            color: #fff;
            margin-bottom: 20px;
        }}
        .community-desc {{
            color: var(--text-muted);
            font-size: 1.2rem;
            margin-bottom: 40px;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
        }}

        /* FOOTER */
        .footer {{
            background: #040507;
            padding: 80px 50px 40px;
            border-top: 2px solid var(--accent);
        }}
        .footer-content {{
            max-width: 1400px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1fr;
            gap: 50px;
        }}
        .footer-logo-img {{
            height: 50px;
            margin-bottom: 20px;
            filter: drop-shadow(0 0 10px var(--accent-glow));
        }}
        .footer-brand p {{
            color: #777;
            max-width: 380px;
            font-size: 0.95rem;
            line-height: 1.7;
        }}
        .footer-links h4 {{
            font-family: 'Orbitron', sans-serif;
            color: var(--accent);
            font-size: 0.95rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 20px;
        }}
        .footer-links ul {{ list-style: none; }}
        .footer-links li {{ margin-bottom: 12px; }}
        .footer-links a {{
            color: #888;
            text-decoration: none;
            transition: color 0.2s;
            font-size: 0.95rem;
        }}
        .footer-links a:hover {{
            color: var(--accent);
        }}
        .footer-bottom {{
            max-width: 1400px;
            margin: 50px auto 0;
            padding-top: 30px;
            border-top: 1px solid rgba(255, 255, 255, 0.06);
            display: flex;
            justify-content: space-between;
            color: #555;
            font-size: 0.88rem;
        }}

        @media (max-width: 900px) {{
            .navbar {{ padding: 0 20px; }}
            .nav-links {{ display: none; }}
            .brand-spec-grid {{ grid-template-columns: 1fr; }}
            .footer-content {{ grid-template-columns: 1fr 1fr; }}
            .hero-title {{ letter-spacing: 5px; }}
        }}
        @media (max-width: 600px) {{
            .footer-content {{ grid-template-columns: 1fr; }}
            .brand-switcher-bar {{ flex-direction: column; gap: 10px; align-items: flex-start; }}
        }}
    </style>
</head>
<body>

<!-- Brand Variant Quick Switcher -->
<div class="brand-switcher-bar">
    <div class="brand-switcher-title">
        <span>ACTIVE SITE BRANDING:</span>
        <strong>{theme['badge_name']}</strong>
    </div>
    <div class="variant-pills">
        {switcher_html}
    </div>
</div>

<!-- Navigation -->
<nav class="navbar">
    <a href="#" class="nav-brand">
        <img src="{theme['nav_logo']}" alt="{title}" class="nav-logo-img">
    </a>
    <div class="nav-links">
        <a href="#brand-kit" class="active">Brand & Logo Suite</a>
        <a href="#features">Features</a>
        <a href="#games">Games</a>
        <a href="#community">Community</a>
    </div>
    <a href="#brand-kit" class="nav-cta">View Full Brand Kit</a>
</nav>

<!-- Hero Section -->
<section class="hero">
    <div class="hero-bg"></div>
    <div class="hero-grid"></div>
    <div class="hero-content">
        <div class="hero-image-container">
            <img src="{theme['hero_image']}" alt="{title} Hero Graphic" class="hero-image">
        </div>
        <h1 class="hero-title">GAMES-REBORN</h1>
        <p class="hero-tagline">{subtitle}</p>
        <div class="hero-buttons">
            <a href="#brand-kit" class="btn-primary">Explore Full Logo Suite ↓</a>
            <a href="#games" class="btn-secondary">Browse Games</a>
        </div>
        <div class="hero-stats">
            <div class="stat">
                <div class="stat-number">3.8M+</div>
                <div class="stat-label">Active Players</div>
            </div>
            <div class="stat">
                <div class="stat-number">65+</div>
                <div class="stat-label">Esports Tournaments</div>
            </div>
            <div class="stat">
                <div class="stat-number">99.9%</div>
                <div class="stat-label">Server Uptime</div>
            </div>
        </div>
    </div>
</section>

<!-- BRAND LOGO SUITE SHOWCASE -->
<section class="brand-showcase" id="brand-kit">
    <div class="section-header">
        <span class="section-label">Brand Assets & Identity Suite</span>
        <h2 class="section-title">Complete Logo Set</h2>
        <p class="section-desc">Full spectrum of brand marks, lockups, badges, app icons, and social banners tailored for the {theme['name']} identity.</p>
    </div>

    <div class="brand-grid">
        {logo_cards_html}
    </div>

    <!-- BRAND SPECS & PALETTE -->
    <div class="brand-spec-grid">
        <div class="spec-box">
            <h3>🎨 Brand Color Palette</h3>
            <div class="color-palette-grid">
                {colors_html}
            </div>
        </div>

        <div class="spec-box">
            <h3>🔤 Typography & Voice</h3>
            <div class="type-sample-row">
                <div class="type-font-name">Primary Display Font</div>
                <div class="type-sample-display">ORBITRON 900 BLACK</div>
            </div>
            <div class="type-sample-row">
                <div class="type-font-name">Secondary & Body Font</div>
                <div class="type-sample-body">Rajdhani Semi-Bold 600 — High-legibility futuristic geometric sans-serif engineered for gaming dashboards and web UI.</div>
            </div>
        </div>
    </div>
</section>

<!-- Features Section -->
<section class="features" id="features">
    <div class="section-header">
        <span class="section-label">Core Architecture</span>
        <h2 class="section-title">Engineered For Champions</h2>
        <p class="section-desc">Uncompromising performance and modern community tooling built into every pixel.</p>
    </div>
    <div class="features-grid">
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <h3 class="feature-title">Ultra-Low Latency</h3>
            <p class="feature-desc">Global edge matchmaking network routing packets under 15ms across North America, Europe, and Asia-Pacific.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🛡️</div>
            <h3 class="feature-title">Kernel-Grade Security</h3>
            <p class="feature-desc">Next-gen anti-cheat algorithms and tamper-proof matchmaking guaranteeing 100% fair competitive play.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🏆</div>
            <h3 class="feature-title">Integrated Tournaments</h3>
            <p class="feature-desc">Automated bracket generation, cash prize escrow, and real-time leaderboard sync directly within the client.</p>
        </div>
    </div>
</section>

<!-- Games Section -->
<section class="games" id="games">
    <div class="section-header">
        <span class="section-label">Featured Roster</span>
        <h2 class="section-title">Featured Titles</h2>
        <p class="section-desc">Experience our signature competitive and story-driven gaming lineup.</p>
    </div>
    <div class="games-grid">
        <div class="game-card">
            <div class="game-thumb"><span class="game-badge">NR</span></div>
            <div class="game-info">
                <h3 class="game-title">Nemesis Rising</h3>
                <p class="game-genre">Battle Royale / Tactical</p>
                <p class="game-desc">100 operators clash across futuristic arenas with customizable exosuits and dynamic weather hazards.</p>
            </div>
        </div>
        <div class="game-card">
            <div class="game-thumb"><span class="game-badge">AF</span></div>
            <div class="game-info">
                <h3 class="game-title">Aether Front</h3>
                <p class="game-genre">Esports 5v5 Tactical FPS</p>
                <p class="game-desc">Precision gunplay meets tactical equipment in tournament-standard competitive bomb defusal modes.</p>
            </div>
        </div>
        <div class="game-card">
            <div class="game-thumb"><span class="game-badge">CS</span></div>
            <div class="game-info">
                <h3 class="game-title">Chrono Shift</h3>
                <p class="game-genre">Sci-Fi ARPG</p>
                <p class="game-desc">Manipulate time, unlock legendary artifacts, and conquer challenging raid bosses with your guild.</p>
            </div>
        </div>
    </div>
</section>

<!-- Community Box -->
<section class="community" id="community">
    <div class="community-box">
        <h2 class="community-title">Join The Reborn Syndicate</h2>
        <p class="community-desc">Connect with over 500,000 active Discord members, join weekly developer AMA sessions, and compete in community cups.</p>
        <a href="#discord" class="btn-primary" style="font-size: 1.05rem; padding: 20px 50px;">Join Official Discord →</a>
    </div>
</section>

<!-- Footer -->
<footer class="footer">
    <div class="footer-content">
        <div class="footer-brand">
            <img src="{theme['footer_logo']}" alt="{title}" class="footer-logo-img">
            <p>GAMES-REBORN is the premier competitive gaming platform and brand ecosystem designed for high-tier esports and creators.</p>
        </div>
        <div class="footer-links">
            <h4>Brand Kits</h4>
            <ul>
                <li><a href="variant1_orange_hex.html">Orange Ember Brand</a></li>
                <li><a href="variant2_red_shield.html">Crimson Shield Brand</a></li>
                <li><a href="variant3_dark_red.html">Dark Reborn 3D Brand</a></li>
                <li><a href="index.html">Master Brand Hub</a></li>
            </ul>
        </div>
        <div class="footer-links">
            <h4>Platform</h4>
            <ul>
                <li><a href="#features">Features</a></li>
                <li><a href="#games">Games</a></li>
                <li><a href="#tournaments">Tournaments</a></li>
                <li><a href="#downloads">Download Client</a></li>
            </ul>
        </div>
        <div class="footer-links">
            <h4>Community</h4>
            <ul>
                <li><a href="#discord">Discord Server</a></li>
                <li><a href="#twitch">Twitch Stream</a></li>
                <li><a href="#twitter">X / Twitter</a></li>
                <li><a href="#youtube">YouTube</a></li>
            </ul>
        </div>
    </div>
    <div class="footer-bottom">
        <p>© 2026 GAMES-REBORN Inc. All brand identity rights reserved.</p>
        <p>Branding Variant: {theme['name']} | Hex Palette: {accent}</p>
    </div>
</footer>

</body>
</html>
"""
    return html

# Define the 3 brand specifications
themes = [
    {
        "id": "variant1",
        "name": "Orange Ember Neon",
        "badge_name": "Orange Ember Cyber",
        "title": "GAMES-REBORN [Orange Ember]",
        "subtitle": "High-Energy Cyberpunk & Golden Flare",
        "accent": "#ff8c00",
        "accent_secondary": "#ff4500",
        "accent_glow": "rgba(255, 140, 0, 0.35)",
        "folder": "orange_ember",
        "favicon": "brand_assets/orange_ember/favicon.png",
        "nav_logo": "brand_assets/orange_ember/05_horizontal_wordmark.png",
        "hero_image": "brand_assets/orange_ember/04_shield_crest.png",
        "footer_logo": "brand_assets/orange_ember/05_horizontal_wordmark.png",
        "filename": "variant1_orange_hex.html",
        "other_variants": [
            {"label": "Orange Ember", "url": "variant1_orange_hex.html", "color": "#ff8c00", "active": True},
            {"label": "Crimson Shield", "url": "variant2_red_shield.html", "color": "#dc143c", "active": False},
            {"label": "Dark Reborn 3D", "url": "variant3_dark_red.html", "color": "#8a0303", "active": False},
            {"label": "Master Hub", "url": "index.html", "color": "#ffffff", "active": False}
        ],
        "colors": [
            {"name": "Amber Ember", "hex": "#ff8c00", "use": "Primary Brand Accent"},
            {"name": "Flame Red-Orange", "hex": "#ff4500", "use": "Secondary / CTA Gradient"},
            {"name": "Deep Cyber Black", "hex": "#07080a", "use": "Primary Background"},
            {"name": "Elevated Titanium", "hex": "#15181f", "use": "Card Surface Background"},
            {"name": "Pure White", "hex": "#ffffff", "use": "Headings & Contrast"}
        ],
        "assets": [
            {
                "name": "Primary Neon Hexagon Lockup",
                "type": "Primary Mark",
                "dims": "1536 x 1536 PNG",
                "path": "brand_assets/orange_ember/01_primary_logo.png",
                "desc": "Signature glowing hexagon emblem with geometric GR monogram and GAMES-REBORN subtitle."
            },
            {
                "name": "Golden Shield Crest",
                "type": "Emblem Badge",
                "dims": "1536 x 864 PNG",
                "path": "brand_assets/orange_ember/04_shield_crest.png",
                "desc": "Gilded shield emblem with radiant cybernetic aura suited for hero banners and awards."
            },
            {
                "name": "Horizontal Header Wordmark",
                "type": "Header / Navbar",
                "dims": "1536 x 384 PNG",
                "path": "brand_assets/orange_ember/05_horizontal_wordmark.png",
                "desc": "Wide horizontal lockup for navigation bars, video overlays, and sponsor banners."
            },
            {
                "name": "Roundel Seal Badge",
                "type": "Circular Stamp",
                "dims": "1536 x 1536 PNG",
                "path": "brand_assets/orange_ember/06_roundel_badge.png",
                "desc": "Circular esports badge suitable for stickers, coins, medals, and profile watermarks."
            },
            {
                "name": "Mobile & Desktop App Icon",
                "type": "App Icon (512px)",
                "dims": "512 x 512 PNG",
                "path": "brand_assets/orange_ember/02_app_icon.png",
                "desc": "High-res squircle app icon with amber rim lighting for iOS, Android, and Steam launcher."
            },
            {
                "name": "Monochrome Minimalist Mark",
                "type": "High Contrast White",
                "dims": "1536 x 1536 PNG",
                "path": "brand_assets/orange_ember/03_monochrome_white.png",
                "desc": "Clean contrast version for laser engraving, embroidery, and monochrome publishing."
            },
            {
                "name": "Social Media & Stream Banner",
                "type": "Hero Banner (16:9)",
                "dims": "1200 x 630 PNG",
                "wide": True,
                "path": "brand_assets/orange_ember/07_social_banner.png",
                "desc": "Cinematic social banner for Twitter/X headers, Twitch stream overlays, and YouTube channel art."
            }
        ]
    },
    {
        "id": "variant2",
        "name": "Crimson Shield Esports",
        "badge_name": "Crimson Shield Esports",
        "title": "GAMES-REBORN [Crimson Shield]",
        "subtitle": "Aggressive Esports Precision & Glowing Ruby Crests",
        "accent": "#dc143c",
        "accent_secondary": "#ff1e42",
        "accent_glow": "rgba(220, 20, 60, 0.38)",
        "folder": "crimson_shield",
        "favicon": "brand_assets/crimson_shield/favicon.png",
        "nav_logo": "brand_assets/crimson_shield/05_horizontal_wordmark.png",
        "hero_image": "brand_assets/crimson_shield/01_primary_logo.png",
        "footer_logo": "brand_assets/crimson_shield/05_horizontal_wordmark.png",
        "filename": "variant2_red_shield.html",
        "other_variants": [
            {"label": "Orange Ember", "url": "variant1_orange_hex.html", "color": "#ff8c00", "active": False},
            {"label": "Crimson Shield", "url": "variant2_red_shield.html", "color": "#dc143c", "active": True},
            {"label": "Dark Reborn 3D", "url": "variant3_dark_red.html", "color": "#8a0303", "active": False},
            {"label": "Master Hub", "url": "index.html", "color": "#ffffff", "active": False}
        ],
        "colors": [
            {"name": "Crimson Ruby", "hex": "#dc143c", "use": "Primary Brand Accent"},
            {"name": "Electric Scarlet", "hex": "#ff1e42", "use": "Hover Glow & Accents"},
            {"name": "Obsidian Black", "hex": "#07080a", "use": "Base Background"},
            {"name": "Graphite Dark", "hex": "#14171d", "use": "Card Surface Background"},
            {"name": "Silver Ash", "hex": "#e0e4ec", "use": "Typography & Details"}
        ],
        "assets": [
            {
                "name": "Glowing Crimson Shield",
                "type": "Primary Mark",
                "dims": "1536 x 1536 PNG",
                "path": "brand_assets/crimson_shield/01_primary_logo.png",
                "desc": "Fierce glowing shield with dual ruby neon borders and angular GR typography."
            },
            {
                "name": "Horizontal Header Wordmark",
                "type": "Header / Nav Logo",
                "dims": "1536 x 384 PNG",
                "path": "brand_assets/crimson_shield/05_horizontal_wordmark.png",
                "desc": "Wide lockup with glowing red GR monogram and modern futuristic typography."
            },
            {
                "name": "Spiky Sun Crest Emblem",
                "type": "Emblem Badge",
                "dims": "1536 x 864 PNG",
                "path": "brand_assets/crimson_shield/04_spiky_crest.png",
                "desc": "Radiant spiked crown emblem for tournament victory screens and guild crests."
            },
            {
                "name": "Vertical Shield Banner",
                "type": "Vertical Emblem",
                "dims": "864 x 1536 PNG",
                "path": "brand_assets/crimson_shield/06_vertical_emblem.png",
                "desc": "Vertical gaming banner badge for tournament rollups and mobile splash screens."
            },
            {
                "name": "Winged Esports Crest",
                "type": "Wing Badge",
                "dims": "1536 x 896 PNG",
                "path": "brand_assets/crimson_shield/08_winged_badge.png",
                "desc": "High-speed winged emblem for team jerseys and esports championships."
            },
            {
                "name": "Official Business Card Mockup",
                "type": "Stationery Mockup",
                "dims": "864 x 1536 PNG",
                "path": "brand_assets/crimson_shield/07_business_card_mockup.png",
                "desc": "Matte black luxury business card mockup with crimson foil stamp detailing."
            },
            {
                "name": "Official Apparel T-Shirt Mockup",
                "type": "Merchandise Mockup",
                "dims": "1200 x 1496 PNG",
                "path": "brand_assets/crimson_shield/09_apparel_tshirt_mockup.png",
                "desc": "Black cotton esports performance tee mockup with winged crest chest print."
            },
            {
                "name": "Crimson Social & Stream Banner",
                "type": "Hero Banner (16:9)",
                "dims": "1200 x 630 PNG",
                "wide": True,
                "path": "brand_assets/crimson_shield/10_social_banner.png",
                "desc": "Wide social banner optimized for Discord server banners, Twitter/X, and Twitch."
            }
        ]
    },
    {
        "id": "variant3",
        "name": "Dark Reborn Metallic 3D",
        "badge_name": "Dark Reborn Cyber Metallic",
        "title": "GAMES-REBORN [Dark Reborn 3D]",
        "subtitle": "Brushed Titanium, Deep Crimson & 3D Dimensional Crests",
        "accent": "#b81414",
        "accent_secondary": "#e62222",
        "accent_glow": "rgba(184, 20, 20, 0.45)",
        "folder": "dark_reborn",
        "favicon": "brand_assets/dark_reborn/favicon.png",
        "nav_logo": "brand_assets/dark_reborn/07_horizontal_lockup.png",
        "hero_image": "brand_assets/dark_reborn/04_cinematic_wide_banner.jpg",
        "footer_logo": "brand_assets/dark_reborn/07_horizontal_lockup.png",
        "filename": "variant3_dark_red.html",
        "other_variants": [
            {"label": "Orange Ember", "url": "variant1_orange_hex.html", "color": "#ff8c00", "active": False},
            {"label": "Crimson Shield", "url": "variant2_red_shield.html", "color": "#dc143c", "active": False},
            {"label": "Dark Reborn 3D", "url": "variant3_dark_red.html", "color": "#8a0303", "active": True},
            {"label": "Master Hub", "url": "index.html", "color": "#ffffff", "active": False}
        ],
        "colors": [
            {"name": "Blood Red 3D", "hex": "#b81414", "use": "Primary Brand Accent"},
            {"name": "Laser Crimson", "hex": "#e62222", "use": "Bevel & Light Accents"},
            {"name": "Dark Titanium", "hex": "#07080a", "use": "Background Base"},
            {"name": "Brushed Steel", "hex": "#8f96a3", "use": "Secondary 3D Metal"},
            {"name": "Polished Platinum", "hex": "#f5f6fa", "use": "Highlights & Text"}
        ],
        "assets": [
            {
                "name": "Cinematic 5K Wide Hero Banner",
                "type": "Full Width Banner",
                "dims": "5792 x 2896 Ultra-HD JPEG",
                "wide": True,
                "path": "brand_assets/dark_reborn/04_cinematic_wide_banner.jpg",
                "desc": "Ultra high-resolution wide header banner featuring the 3D metallic shield with crimson rim lighting."
            },
            {
                "name": "Primary 3D Metallic Shield Lockup",
                "type": "Primary Mark (4K)",
                "dims": "4096 x 4096 JPEG",
                "path": "brand_assets/dark_reborn/01_primary_3d_shield.jpg",
                "desc": "Ultra high-resolution 3D rendered brushed chrome & ruby shield mark."
            },
            {
                "name": "3D Metallic Horizontal Lockup",
                "type": "Header / Navbar",
                "dims": "1536 x 768 PNG",
                "path": "brand_assets/dark_reborn/07_horizontal_lockup.png",
                "desc": "Full 3D lockup featuring the metallic GR emblem accompanied by stylized GAMES-REBORN typography."
            },
            {
                "name": "Beveled 3D Metallic Wordmark",
                "type": "Logotype Wordmark",
                "dims": "1536 x 768 PNG",
                "path": "brand_assets/dark_reborn/06_metallic_wordmark.png",
                "desc": "Heavy 3D metallic typography with crimson 'REBORN' subline."
            },
            {
                "name": "Angular Cybernetic Crest",
                "type": "Emblem Mark",
                "dims": "1536 x 1536 PNG",
                "path": "brand_assets/dark_reborn/05_metallic_crest.png",
                "desc": "Sharp geometric layered shield with red underglow for esports avatars."
            },
            {
                "name": "Modern Cyber Wing Badge",
                "type": "Wing Icon",
                "dims": "768 x 768 PNG",
                "path": "brand_assets/dark_reborn/08_wing_badge.png",
                "desc": "Futuristic neon red cyber wing emblem suitable for app badges and status icons."
            },
            {
                "name": "Desktop & Mobile App Icon",
                "type": "App Icon (512px)",
                "dims": "512 x 512 PNG",
                "path": "brand_assets/dark_reborn/02_app_icon.png",
                "desc": "Squircle launcher icon with crimson laser perimeter for Windows, Mac, and iOS."
            },
            {
                "name": "High-Contrast Monochrome Mark",
                "type": "Minimalist White",
                "dims": "4096 x 4096 PNG",
                "path": "brand_assets/dark_reborn/03_monochrome_white.png",
                "desc": "High-contrast monochrome render for vector tracing, stamping, and single-color print."
            }
        ]
    }
]

# Generate each landing page HTML file
for theme in themes:
    html_content = get_landing_page_html(theme)
    out_path = os.path.join(r"G:\Venice", theme["filename"])
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated {theme['filename']} successfully!")

print("Generating Master Brand Hub (index.html)...")
