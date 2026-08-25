import os
import shutil

base_dir = r"G:\Venice"

# Remove scratch files
for temp_file in ["index (2).html", "test_trace.svg"]:
    p = os.path.join(base_dir, temp_file)
    if os.path.exists(p):
        os.remove(p)
        print(f"Removed temp file: {temp_file}")

tmp_trace_dir = os.path.join(base_dir, "reborn_3d_brand_system", "temp_trace")
if os.path.exists(tmp_trace_dir):
    shutil.rmtree(tmp_trace_dir)
    print("Removed temp_trace dir.")

# Create .gitignore
gitignore_content = """# Python & System caches
__pycache__/
*.py[cod]
*$py.class
.DS_Store
Thumbs.db
*.tmp
temp_trace/
"""

with open(os.path.join(base_dir, ".gitignore"), "w", encoding="utf-8") as f:
    f.write(gitignore_content)
print("Created .gitignore")

# Create comprehensive README.md
readme_content = """# GAMES REBORN Brand Identity & Design System

Official Brand Identity, Vector Graphics Suite, Design Tokens, and Asset Kit for the **GAMES REBORN Network**.

---

## 🚀 Quick Navigation & Interactive Portals

* **[`BRAND_GUIDEBOOK.html`](./BRAND_GUIDEBOOK.html)**: Interactive Brand Guidebook, live vector previewer, color palette inspector, and asset download hub.
* **[`reborn_prime_landing_page.html`](./reborn_prime_landing_page.html)**: Flagship Dark Reborn 3D landing page.
* **[`index.html`](./index.html)**: Master brand portal hub connecting all brand design variants.

---

## 📦 Brand System Directory Map

```
GAMES-Reborn-Network/branding/
├── reborn_3d_brand_system/             <-- Core Flagship Brand System
│   ├── BRAND_GUIDEBOOK.html            (Master Interactive Guidebook & Asset Center)
│   ├── 01_vectors_svg/                 (100% Transparent Scalable Vector SVGs)
│   │   ├── logo_primary_3d_lockup.svg  (Primary 3D Metallic Shield Lockup)
│   │   ├── logo_horizontal_wordmark.svg(Horizontal Header & Stream Overlay Lockup)
│   │   ├── logo_crest_shield.svg       (Angular Cyber Crest)
│   │   ├── logo_metallic_wordmark.svg  (3D Metallic GAMES REBORN Logotype)
│   │   ├── logo_cyber_wing.svg         (Cyber Wing Championship Badge)
│   │   ├── logo_monogram_icon.svg      (Squircle App Icon Monogram)
│   │   ├── logo_monochrome_white.svg   (Pure White Vector for Dark Print & Laser Etch)
│   │   ├── logo_monochrome_black.svg   (Pure Black Vector for Light Documents)
│   │   └── brand_grid_construction.svg (Geometric Blueprint & Clearspace Guide)
│   │
│   ├── 02_transparent_png/             (32-Bit Alpha Channel Cutouts - 0 Background)
│   │   ├── primary_logo_4k_transparent.png (4096×4096 Master Cutout)
│   │   ├── primary_logo_2k_transparent.png (2048×2048 Cutout)
│   │   ├── primary_logo_1k_transparent.png (1024×1024 Cutout)
│   │   ├── horizontal_nav_lockup.png
│   │   ├── crest_shield.png
│   │   ├── metallic_wordmark.png
│   │   ├── cyber_wing_badge.png
│   │   ├── monochrome_white.png
│   │   └── monochrome_black.png
│   │
│   ├── 03_app_icons_favicons/          (Multi-Resolution App Icons & Favicons)
│   │   ├── favicon.ico                 (16, 32, 48, 64, 128, 256px multi-size bundle)
│   │   ├── favicon-16x16.png & 32x32.png
│   │   ├── apple-touch-icon.png        (180×180 iOS)
│   │   ├── android-chrome-192x192.png & 512x512.png
│   │   └── app_icon_ios_squircle_1024.png
│   │
│   ├── 04_social_media_kit/            (Pixel-Calibrated Social Media Graphics)
│   │   ├── twitter_x_header_1500x500.jpg
│   │   ├── youtube_banner_2560x1440.jpg
│   │   ├── twitch_offline_banner_1920x1080.jpg
│   │   ├── discord_server_banner_960x540.jpg
│   │   ├── discord_avatar_512x512.png
│   │   ├── facebook_linkedin_cover_1200x630.jpg
│   │   ├── instagram_square_post_1080x1080.jpg
│   │   └── instagram_story_1080x1920.jpg
│   │
│   ├── 05_wallpapers_4k/               (High-Density Displays)
│   │   ├── desktop_4k_wallpaper_3840x2160.jpg
│   │   ├── ultrawide_5k_wallpaper_5120x2160.jpg
│   │   └── mobile_oled_wallpaper_1080x2400.jpg
│   │
│   ├── 06_merch_and_mockups/           (Real-World Product Mockups)
│   │   ├── mockup_battlestation_desk_setup.png
│   │   ├── mockup_esports_jersey_hoodie.png
│   │   └── mockup_cinematic_5k_header.jpg
│   │
│   └── 07_design_tokens_and_code/      (Developer Handoff Tokens)
│       ├── brand_tokens.json           (JSON Design Tokens)
│       ├── brand_styles.css            (CSS Custom Properties & Glow Utilities)
│       └── tailwind_config_snippet.js  (Tailwind CSS Preset)
│
├── brand_assets/                       <-- Alternative Theme Suites (Orange Ember, Crimson Shield)
└── variant1_orange_hex.html, variant2_red_shield.html, variant3_dark_red.html
```

---

## 🎨 Calibrated Color Palette

| Color Name | HEX | RGB | CMYK | Pantone | Usage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ruby Laser Red** | `#b81414` | `184, 20, 20` | `10, 98, 95, 20` | `PMS 186 C` | Primary Accent / Actions |
| **Electric Scarlet Flare** | `#ff263b` | `255, 38, 59` | `0, 85, 77, 0` | `PMS Warm Red C` | Glow & Laser Highlights |
| **Brushed Titanium 3D** | `#8f96a3` | `143, 150, 163` | `35, 25, 20, 10` | `Cool Gray 8 C` | Chrome Bevels & Metal Trim |
| **Obsidian Deep** | `#060709` | `6, 7, 9` | `75, 68, 65, 90` | `Black 6 C` | Interface Background |

---

## 💻 Developer Quickstart

### CSS Variables
```css
@import url('reborn_3d_brand_system/07_design_tokens_and_code/brand_styles.css');

.hero-cta {
  background: var(--dr-primary);
  box-shadow: var(--dr-shadow-glow);
  font-family: var(--dr-font-display);
}
```

### Tailwind Config Preset
```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        reborn: {
          red: '#b81414',
          scarlet: '#ff263b',
          titanium: '#8f96a3',
          obsidian: '#060709',
        }
      }
    }
  }
}
```

---

© 2026 GAMES REBORN Network. All rights reserved.
"""

with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)
print("Created README.md")
