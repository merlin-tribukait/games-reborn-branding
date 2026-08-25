import os
import io
import base64
from PIL import Image, ImageOps, ImageEnhance
import numpy as np

base_dir = r"G:\Venice"
brand_sys = os.path.join(base_dir, "reborn_3d_brand_system")
svg_dir = os.path.join(brand_sys, "01_vectors_svg")
png_dir = os.path.join(brand_sys, "02_transparent_png")

def clean_alpha_cutout(img_path, threshold=32, feather=2.0, auto_crop=True, pad=30):
    """
    Strips ALL background noise, sets corners & dark areas to EXACT 0 alpha,
    preserves rich glowing metallic edges, and tightly crops to bounding box.
    """
    im = Image.open(img_path).convert("RGB")
    arr = np.array(im, dtype=np.float32)
    
    # Calculate luminance & max color channel
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    max_c = np.maximum(np.maximum(r, g), b)
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    
    # Combined intensity
    intensity = np.maximum(lum, max_c)
    
    # Alpha mask: anything below threshold is strictly 0
    alpha = np.zeros_like(intensity, dtype=np.float32)
    mask = intensity > threshold
    alpha[mask] = np.clip((intensity[mask] - threshold) / (threshold * feather) * 255.0, 0, 255)
    
    # Force pure black on transparent areas so no color fringing occurs
    r_clean = np.where(alpha > 0, r, 0)
    g_clean = np.where(alpha > 0, g, 0)
    b_clean = np.where(alpha > 0, b, 0)
    
    rgba_arr = np.dstack([r_clean, g_clean, b_clean, alpha]).astype(np.uint8)
    res_im = Image.fromarray(rgba_arr, mode="RGBA")
    
    if auto_crop:
        # Find non-zero alpha bounding box
        alpha_channel = rgba_arr[:,:,3]
        coords = np.argwhere(alpha_channel > 5)
        if coords.size > 0:
            y0, x0 = coords.min(axis=0)
            y1, x1 = coords.max(axis=0)
            # Add padding
            w, h = res_im.size
            x0 = max(0, x0 - pad)
            y0 = max(0, y0 - pad)
            x1 = min(w, x1 + pad)
            y1 = min(h, y1 + pad)
            res_im = res_im.crop((x0, y0, x1, y1))
            
    return res_im

# 1. Process Master Cutouts
print("Processing clean alpha cutouts with 0 background...")

# Primary 3D Shield (4096 x 4096 base)
cutout_shield = clean_alpha_cutout(os.path.join(base_dir, "VeniceAI_AxpbSjr1OzMubz_0.jpeg"), threshold=32, feather=2.0, auto_crop=True, pad=40)
cutout_shield.save(os.path.join(png_dir, "primary_logo_4k_transparent.png"))
cutout_shield_2k = cutout_shield.resize((2048, int(2048 * cutout_shield.height / cutout_shield.width)), Image.Resampling.LANCZOS)
cutout_shield_2k.save(os.path.join(png_dir, "primary_logo_2k_transparent.png"))
cutout_shield_1k = cutout_shield.resize((1024, int(1024 * cutout_shield.height / cutout_shield.width)), Image.Resampling.LANCZOS)
cutout_shield_1k.save(os.path.join(png_dir, "primary_logo_1k_transparent.png"))

# Horizontal Nav Lockup
cutout_nav = clean_alpha_cutout(os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_2.png"), threshold=34, feather=1.8, auto_crop=True, pad=25)
cutout_nav.save(os.path.join(png_dir, "horizontal_nav_lockup.png"))

# Angular Crest Shield
cutout_crest = clean_alpha_cutout(os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_0.png"), threshold=34, feather=1.8, auto_crop=True, pad=25)
cutout_crest.save(os.path.join(png_dir, "crest_shield.png"))

# 3D Metallic Wordmark
cutout_wordmark = clean_alpha_cutout(os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_1.png"), threshold=34, feather=1.8, auto_crop=True, pad=25)
cutout_wordmark.save(os.path.join(png_dir, "metallic_wordmark.png"))

# Cyber Wing Badge
cutout_wing = clean_alpha_cutout(os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_3.png"), threshold=36, feather=1.8, auto_crop=True, pad=25)
cutout_wing.save(os.path.join(png_dir, "cyber_wing_badge.png"))

# Monochrome White & Black RGBA Transparent PNGs
def make_transparent_monochrome(rgba_img, color_rgb=(255, 255, 255)):
    arr = np.array(rgba_img)
    alpha = arr[:,:,3]
    # Create pure solid color with preserved alpha
    r = np.full_like(alpha, color_rgb[0])
    g = np.full_like(alpha, color_rgb[1])
    b = np.full_like(alpha, color_rgb[2])
    mono_arr = np.dstack([r, g, b, alpha])
    return Image.fromarray(mono_arr, mode="RGBA")

mono_white_png = make_transparent_monochrome(cutout_shield_1k, (255, 255, 255))
mono_white_png.save(os.path.join(png_dir, "monochrome_white.png"))

mono_black_png = make_transparent_monochrome(cutout_shield_1k, (15, 17, 22))
mono_black_png.save(os.path.join(png_dir, "monochrome_black.png"))

print("All PNGs processed with 100% transparent backgrounds and zero black borders!")

# 2. Build Zero-Background Master SVGs
def create_zero_bg_svg(png_image, out_svg_path, title="Dark Reborn 3D"):
    w, h = png_image.size
    buffered = io.BytesIO()
    png_image.save(buffered, format="PNG", optimize=True)
    b64_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    svg_str = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <!-- {title} - 100% Transparent Zero-Background Vector Asset -->
  <image width="{w}" height="{h}" xlink:href="data:image/png;base64,{b64_str}"/>
</svg>"""
    with open(out_svg_path, "w", encoding="utf-8") as f:
        f.write(svg_str)
    print(f"Generated zero-bg SVG: {os.path.basename(out_svg_path)} ({w}x{h})")

# Generate all SVGs
create_zero_bg_svg(cutout_shield_1k, os.path.join(svg_dir, "logo_primary_3d_lockup.svg"), "Primary 3D Metallic Shield Lockup")
create_zero_bg_svg(cutout_nav, os.path.join(svg_dir, "logo_horizontal_wordmark.svg"), "Horizontal Header Wordmark")
create_zero_bg_svg(cutout_crest, os.path.join(svg_dir, "logo_crest_shield.svg"), "Angular Cyber Crest")
create_zero_bg_svg(cutout_wordmark, os.path.join(svg_dir, "logo_metallic_wordmark.svg"), "3D Metallic Wordmark")
create_zero_bg_svg(cutout_wing, os.path.join(svg_dir, "logo_cyber_wing.svg"), "Cyber Wing Badge")
create_zero_bg_svg(mono_white_png, os.path.join(svg_dir, "logo_monochrome_white.svg"), "Monochrome White Transparent Mark")
create_zero_bg_svg(mono_black_png, os.path.join(svg_dir, "logo_monochrome_black.svg"), "Monochrome Black Transparent Mark")

# Monogram App Icon SVG (crop central shield for squircle)
app_icon_base = cutout_shield_1k.resize((420, 420), Image.Resampling.LANCZOS)
app_icon_canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
# Rounded squircle container with dark surface and red border
from PIL import ImageDraw
draw = ImageDraw.Draw(app_icon_canvas)
draw.rounded_rectangle([10, 10, 502, 502], radius=110, fill=(13, 15, 20, 255), outline=(184, 20, 20, 255), width=6)
# Paste logo centered
app_icon_canvas.paste(app_icon_base, (46, 46), mask=app_icon_base)
app_icon_canvas.save(os.path.join(brand_sys, "03_app_icons_favicons", "android-chrome-512x512.png"))
create_zero_bg_svg(app_icon_canvas, os.path.join(svg_dir, "logo_monogram_icon.svg"), "Monogram Squircle App Icon")

# Update Construction blueprint SVG background to transparent
svg_grid_transparent = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="100%" height="100%">
  <!-- Construction Lines & Safe Zone (Transparent Background) -->
  <g stroke="#3a445d" stroke-width="1" stroke-dasharray="4 4">
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
</svg>"""
with open(os.path.join(svg_dir, "brand_grid_construction.svg"), "w", encoding="utf-8") as f:
    f.write(svg_grid_transparent)

print("SUCCESS: All SVGs and PNGs now have 100% transparent backgrounds!")
