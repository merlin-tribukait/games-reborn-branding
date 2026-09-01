import os
import json

base_dir = r"G:\Venice"
brand_sys = os.path.join(base_dir, "reborn_3d_brand_system")
svg_dir = os.path.join(brand_sys, "01_vectors_svg")
token_dir = os.path.join(brand_sys, "07_design_tokens_and_code")

# 1. Primary Vector Logo (SVG)
svg_primary = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="100%" height="100%">
  <defs>
    <!-- Metallic Titanium Gradients -->
    <linearGradient id="metalLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="25%" stop-color="#d0d5dd"/>
      <stop offset="50%" stop-color="#8a92a0"/>
      <stop offset="75%" stop-color="#474e5d"/>
      <stop offset="100%" stop-color="#1f242f"/>
    </linearGradient>
    
    <linearGradient id="metalDark" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#98a2b3"/>
      <stop offset="40%" stop-color="#344054"/>
      <stop offset="80%" stop-color="#1d2939"/>
      <stop offset="100%" stop-color="#0c111d"/>
    </linearGradient>

    <!-- Ruby Laser Red Glow Gradients -->
    <linearGradient id="laserRed" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff3344"/>
      <stop offset="50%" stop-color="#dc143c"/>
      <stop offset="100%" stop-color="#800010"/>
    </linearGradient>
    
    <radialGradient id="neonGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ff1a35" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#dc143c" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#800010" stop-opacity="0"/>
    </radialGradient>

    <filter id="glowEffect" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="16" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect width="100%" height="100%" fill="#07080b" rx="24"/>

  <!-- Background Ambient Glow -->
  <circle cx="400" cy="400" r="300" fill="url(#neonGlow)"/>

  <!-- Outer Shield Aura Border -->
  <path d="M 400 120 L 660 270 L 660 480 L 400 680 L 140 480 L 140 270 Z" 
        fill="none" stroke="url(#laserRed)" stroke-width="4" filter="url(#glowEffect)" opacity="0.9"/>

  <!-- Secondary Outer Shield Facet -->
  <path d="M 400 140 L 635 275 L 635 465 L 400 650 L 165 465 L 165 275 Z" 
        fill="#0d0f14" stroke="url(#metalLight)" stroke-width="6"/>

  <!-- Beveled 3D Shield Shell -->
  <!-- Top Left Bevel -->
  <polygon points="400,140 400,200 200,310 165,275" fill="url(#metalLight)"/>
  <!-- Top Right Bevel -->
  <polygon points="400,140 400,200 600,310 635,275" fill="url(#metalDark)"/>
  <!-- Bottom Left Bevel -->
  <polygon points="165,465 200,440 400,600 400,650" fill="url(#metalDark)"/>
  <!-- Bottom Right Bevel -->
  <polygon points="635,465 600,440 400,600 400,650" fill="url(#metalLight)"/>

  <!-- Inner Dark Core Plate -->
  <path d="M 400 200 L 600 310 L 600 440 L 400 600 L 200 440 L 200 310 Z" 
        fill="#090b10" stroke="url(#laserRed)" stroke-width="5"/>

  <!-- Monogram GR / Apex 3D Emblem Geometry -->
  <!-- G Segment Left -->
  <path d="M 370 260 L 260 320 L 260 440 L 380 510 L 380 430 L 320 395 L 320 365 L 370 335 Z" 
        fill="url(#metalLight)" stroke="#ff2233" stroke-width="3" filter="url(#glowEffect)"/>

  <!-- G Inner Shading -->
  <path d="M 370 260 L 320 290 L 280 340 L 280 420 L 360 470 L 360 435 L 320 410 Z" 
        fill="url(#metalDark)"/>

  <!-- R Segment Right -->
  <path d="M 430 260 L 540 320 L 540 390 L 460 430 L 550 540 L 480 540 L 410 450 L 410 520 L 430 520 L 410 540 L 390 540 L 390 260 Z" 
        fill="url(#metalLight)" stroke="#ff2233" stroke-width="3" filter="url(#glowEffect)"/>

  <!-- R Inner Counter & Lower Leg -->
  <polygon points="430,310 490,340 490,375 430,400" fill="#07080b"/>
  <polygon points="440,320 480,345 480,365 440,385" fill="url(#laserRed)"/>
  <polygon points="460,430 550,540 500,540 430,450" fill="url(#metalDark)"/>

  <!-- Center Laser Core Diamond -->
  <polygon points="400,340 415,360 400,380 385,360" fill="#ffffff" filter="url(#glowEffect)"/>

  <!-- Subtitle Logotype -->
  <text x="400" y="735" font-family="'Orbitron', sans-serif" font-weight="900" font-size="34" letter-spacing="12" fill="#ffffff" text-anchor="middle">GAMES-REBORN</text>
</svg>
"""

with open(os.path.join(svg_dir, "logo_primary_3d_lockup.svg"), "w", encoding="utf-8") as f:
    f.write(svg_primary)

# 2. Horizontal Nav SVG
svg_horizontal = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 240" width="100%" height="100%">
  <defs>
    <linearGradient id="metalH" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="50%" stop-color="#98a2b3"/>
      <stop offset="100%" stop-color="#344054"/>
    </linearGradient>
    <linearGradient id="laserH" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff3344"/>
      <stop offset="100%" stop-color="#990011"/>
    </linearGradient>
    <filter id="redGlowH">
      <feGaussianBlur stdDeviation="8" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Icon Mark on Left -->
  <g transform="translate(40, 20) scale(0.25)">
    <path d="M 400 120 L 660 270 L 660 480 L 400 680 L 140 480 L 140 270 Z" fill="#0d0f14" stroke="url(#laserH)" stroke-width="12" filter="url(#redGlowH)"/>
    <path d="M 400 140 L 635 275 L 635 465 L 400 650 L 165 465 L 165 275 Z" fill="none" stroke="url(#metalH)" stroke-width="16"/>
    <!-- GR Letters -->
    <path d="M 370 260 L 260 320 L 260 440 L 380 510 L 380 430 L 320 395 L 320 365 L 370 335 Z" fill="url(#metalH)"/>
    <path d="M 430 260 L 540 320 L 540 390 L 460 430 L 550 540 L 480 540 L 410 450 L 410 520 L 390 520 L 390 260 Z" fill="url(#metalH)"/>
    <polygon points="400,340 415,360 400,380 385,360" fill="#ffffff" filter="url(#redGlowH)"/>
  </g>

  <!-- Typography -->
  <text x="280" y="110" font-family="'Orbitron', sans-serif" font-weight="900" font-size="54" letter-spacing="8" fill="#ffffff">GAMES</text>
  <text x="560" y="110" font-family="'Orbitron', sans-serif" font-weight="900" font-size="54" letter-spacing="8" fill="url(#laserH)" filter="url(#redGlowH)">REBORN</text>
  <text x="285" y="160" font-family="'Rajdhani', sans-serif" font-weight="700" font-size="20" letter-spacing="10" fill="#8892a4">COMPETITIVE ESPORTS ECOSYSTEM</text>
  
  <!-- Underline Laser Accent -->
  <rect x="280" y="180" width="640" height="3" fill="url(#laserH)"/>
</svg>
"""
with open(os.path.join(svg_dir, "logo_horizontal_wordmark.svg"), "w", encoding="utf-8") as f:
    f.write(svg_horizontal)

# 3. Monogram Icon SVG
svg_monogram = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <linearGradient id="mG" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="50%" stop-color="#98a2b3"/>
      <stop offset="100%" stop-color="#1d2939"/>
    </linearGradient>
    <linearGradient id="lG" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff3344"/>
      <stop offset="100%" stop-color="#b80015"/>
    </linearGradient>
  </defs>
  <rect width="512" height="512" rx="110" fill="#0d0f14" stroke="#252a35" stroke-width="4"/>
  <circle cx="256" cy="256" r="180" fill="none" stroke="url(#lG)" stroke-width="3" opacity="0.6"/>
  <!-- GR Monogram -->
  <g transform="translate(56, 56) scale(0.5)">
    <path d="M 400 120 L 660 270 L 660 480 L 400 680 L 140 480 L 140 270 Z" fill="#131720" stroke="url(#lG)" stroke-width="12"/>
    <path d="M 370 260 L 260 320 L 260 440 L 380 510 L 380 430 L 320 395 L 320 365 L 370 335 Z" fill="url(#mG)"/>
    <path d="M 430 260 L 540 320 L 540 390 L 460 430 L 550 540 L 480 540 L 410 450 L 410 520 L 390 520 L 390 260 Z" fill="url(#mG)"/>
    <polygon points="400,340 415,360 400,380 385,360" fill="#ffffff"/>
  </g>
</svg>
"""
with open(os.path.join(svg_dir, "logo_monogram_icon.svg"), "w", encoding="utf-8") as f:
    f.write(svg_monogram)

# 4. Monochrome White and Black SVGs
svg_mono_white = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="100%" height="100%">
  <path d="M 400 120 L 660 270 L 660 480 L 400 680 L 140 480 L 140 270 Z" fill="none" stroke="#ffffff" stroke-width="16"/>
  <path d="M 370 260 L 260 320 L 260 440 L 380 510 L 380 430 L 320 395 L 320 365 L 370 335 Z" fill="#ffffff"/>
  <path d="M 430 260 L 540 320 L 540 390 L 460 430 L 550 540 L 480 540 L 410 450 L 410 520 L 390 520 L 390 260 Z" fill="#ffffff"/>
  <polygon points="400,340 415,360 400,380 385,360" fill="#ffffff"/>
  <text x="400" y="735" font-family="'Orbitron', sans-serif" font-weight="900" font-size="34" letter-spacing="12" fill="#ffffff" text-anchor="middle">GAMES-REBORN</text>
</svg>
"""
with open(os.path.join(svg_dir, "logo_monochrome_white.svg"), "w", encoding="utf-8") as f:
    f.write(svg_mono_white)

svg_mono_black = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="100%" height="100%">
  <path d="M 400 120 L 660 270 L 660 480 L 400 680 L 140 480 L 140 270 Z" fill="none" stroke="#000000" stroke-width="16"/>
  <path d="M 370 260 L 260 320 L 260 440 L 380 510 L 380 430 L 320 395 L 320 365 L 370 335 Z" fill="#000000"/>
  <path d="M 430 260 L 540 320 L 540 390 L 460 430 L 550 540 L 480 540 L 410 450 L 410 520 L 390 520 L 390 260 Z" fill="#000000"/>
  <polygon points="400,340 415,360 400,380 385,360" fill="#000000"/>
  <text x="400" y="735" font-family="'Orbitron', sans-serif" font-weight="900" font-size="34" letter-spacing="12" fill="#000000" text-anchor="middle">GAMES-REBORN</text>
</svg>
"""
with open(os.path.join(svg_dir, "logo_monochrome_black.svg"), "w", encoding="utf-8") as f:
    f.write(svg_mono_black)

# 5. Construction Grid SVG
svg_grid = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="100%" height="100%">
  <rect width="800" height="800" fill="#090b10"/>
  <!-- Construction Lines -->
  <g stroke="#2a3245" stroke-width="1" stroke-dasharray="4 4">
    <line x1="0" y1="400" x2="800" y2="400"/>
    <line x1="400" y1="0" x2="400" y2="800"/>
    <circle cx="400" cy="400" r="300" fill="none"/>
    <circle cx="400" cy="400" r="200" fill="none"/>
    <circle cx="400" cy="400" r="100" fill="none"/>
    <line x1="100" y1="100" x2="700" y2="700"/>
    <line x1="700" y1="100" x2="100" y2="700"/>
  </g>
  <!-- Clearspace Boundary -->
  <rect x="80" y="80" width="640" height="640" fill="none" stroke="#ff3344" stroke-width="2" stroke-dasharray="6 6"/>
  <text x="90" y="70" font-family="monospace" font-size="14" fill="#ff3344">CLEARSPACE SAFE ZONE (X = 80px)</text>
  <!-- Logo Blueprint Outline -->
  <path d="M 400 120 L 660 270 L 660 480 L 400 680 L 140 480 L 140 270 Z" fill="none" stroke="#00d2ff" stroke-width="3"/>
  <path d="M 370 260 L 260 320 L 260 440 L 380 510 L 380 430 L 320 395 L 320 365 L 370 335 Z" fill="none" stroke="#00d2ff" stroke-width="2"/>
  <path d="M 430 260 L 540 320 L 540 390 L 460 430 L 550 540 L 480 540 L 410 450 L 410 520 L 390 520 L 390 260 Z" fill="none" stroke="#00d2ff" stroke-width="2"/>
</svg>
"""
with open(os.path.join(svg_dir, "brand_grid_construction.svg"), "w", encoding="utf-8") as f:
    f.write(svg_grid)

print("Vector SVGs generated!")

# 6. Design Tokens JSON
tokens = {
    "$schema": "https://design-tokens.github.io/community-group/format/",
    "brandName": "Dark Reborn 3D",
    "version": "2.0.0",
    "colors": {
        "primary": {
            "value": "#b81414",
            "type": "color",
            "name": "Ruby Laser Red",
            "description": "Primary action and neon accent color",
            "cmyk": "C:10 M:98 Y:95 K:20",
            "pantone": "PMS 186 C"
        },
        "primaryLight": {
            "value": "#ff263b",
            "type": "color",
            "name": "Electric Scarlet Flare"
        },
        "primaryDark": {
            "value": "#700808",
            "type": "color",
            "name": "Crimson Shadow"
        },
        "titanium3D": {
            "value": "#8f96a3",
            "type": "color",
            "name": "Brushed Steel Metallic",
            "cmyk": "C:35 M:25 Y:20 K:10",
            "pantone": "Cool Gray 8 C"
        },
        "platinumHighlight": {
            "value": "#f5f7fa",
            "type": "color",
            "name": "Platinum Bevel Highlight"
        },
        "backgroundBase": {
            "value": "#060709",
            "type": "color",
            "name": "Obsidian Deep"
        },
        "surfaceCard": {
            "value": "#0f1218",
            "type": "color",
            "name": "Graphite Plate"
        },
        "surfaceElevated": {
            "value": "#161a23",
            "type": "color",
            "name": "Armor Slate"
        },
        "borderMuted": {
            "value": "rgba(255, 255, 255, 0.08)",
            "type": "color"
        }
    },
    "typography": {
        "fontFamily": {
            "display": "'Orbitron', -apple-system, sans-serif",
            "body": "'Rajdhani', -apple-system, sans-serif",
            "code": "'JetBrains Mono', monospace"
        },
        "fontWeight": {
            "regular": 400,
            "medium": 500,
            "semibold": 600,
            "bold": 700,
            "black": 900
        }
    },
    "shadows": {
        "glowRedSm": "0 0 15px rgba(184, 20, 20, 0.35)",
        "glowRedLg": "0 0 45px rgba(184, 20, 20, 0.55)",
        "card3D": "0 20px 40px rgba(0, 0, 0, 0.6)"
    },
    "radii": {
        "sm": "6px",
        "md": "12px",
        "lg": "20px",
        "pill": "9999px"
    }
}

with open(os.path.join(token_dir, "brand_tokens.json"), "w", encoding="utf-8") as f:
    json.dump(tokens, f, indent=2)

# 7. CSS Design System Variables
brand_css = """/**
 * Dark Reborn 3D Brand System - Core CSS Variables & Utility Classes
 * Version 2.0.0
 */

:root {
  /* Brand Colors */
  --dr-primary: #b81414;
  --dr-primary-light: #ff263b;
  --dr-primary-dark: #700808;
  --dr-primary-glow: rgba(184, 20, 20, 0.45);
  
  --dr-metal-light: #f5f7fa;
  --dr-metal-mid: #8f96a3;
  --dr-metal-dark: #343c4d;

  --dr-bg-base: #060709;
  --dr-bg-surface: #0f1218;
  --dr-bg-elevated: #161a23;
  --dr-border: rgba(255, 255, 255, 0.08);
  --dr-border-focus: #b81414;

  /* Typography */
  --dr-font-display: 'Orbitron', sans-serif;
  --dr-font-body: 'Rajdhani', sans-serif;

  /* Shadows */
  --dr-shadow-glow: 0 0 35px var(--dr-primary-glow);
  --dr-shadow-card: 0 16px 32px rgba(0, 0, 0, 0.5);

  /* Transitions */
  --dr-transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Base Utility Classes */
.dr-text-glow {
  text-shadow: 0 0 20px var(--dr-primary-glow);
}

.dr-card-3d {
  background: var(--dr-bg-elevated);
  border: 1px solid var(--dr-border);
  border-radius: 16px;
  box-shadow: var(--dr-shadow-card);
  transition: var(--dr-transition);
}
.dr-card-3d:hover {
  border-color: var(--dr-primary);
  box-shadow: var(--dr-shadow-glow);
  transform: translateY(-4px);
}

.dr-btn-primary {
  background: linear-gradient(135deg, var(--dr-primary), var(--dr-primary-light));
  color: #ffffff;
  font-family: var(--dr-font-display);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2px;
  padding: 16px 36px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: var(--dr-shadow-glow);
  cursor: pointer;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 12px;
  transition: var(--dr-transition);
}
.dr-btn-primary:hover {
  transform: translateY(-2px);
  filter: brightness(1.15);
}
"""
with open(os.path.join(token_dir, "brand_styles.css"), "w", encoding="utf-8") as f:
    f.write(brand_css)

# 8. Tailwind Config Preset
tailwind_snippet = """// tailwind.config.js - Dark Reborn 3D Preset
module.exports = {
  theme: {
    extend: {
      colors: {
        reborn: {
          red: '#b81414',
          scarlet: '#ff263b',
          crimson: '#700808',
          titanium: '#8f96a3',
          platinum: '#f5f7fa',
          obsidian: '#060709',
          surface: '#0f1218',
          elevated: '#161a23'
        }
      },
      fontFamily: {
        display: ['Orbitron', 'sans-serif'],
        body: ['Rajdhani', 'sans-serif']
      },
      boxShadow: {
        'reborn-glow': '0 0 35px rgba(184, 20, 20, 0.45)',
        'reborn-laser': '0 0 15px rgba(255, 38, 59, 0.7)'
      }
    }
  }
}
"""
with open(os.path.join(token_dir, "tailwind_config_snippet.js"), "w", encoding="utf-8") as f:
    f.write(tailwind_snippet)

print("Design tokens, CSS and Tailwind configs created!")
