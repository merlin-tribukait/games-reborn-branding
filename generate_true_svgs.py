import os
import base64
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import numpy as np

base_dir = r"G:\Venice"
brand_sys = os.path.join(base_dir, "reborn_3d_brand_system")
svg_dir = os.path.join(brand_sys, "01_vectors_svg")
png_dir = os.path.join(brand_sys, "02_transparent_png")

def extract_alpha_cutout(img_path, threshold=12, feather=2.5):
    """
    Extracts transparent alpha channel from black background with edge feathering and glow preservation.
    """
    im = Image.open(img_path).convert("RGBA")
    arr = np.array(im, dtype=np.float32)
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    # Calculate luminance / max color intensity
    intensity = np.maximum(np.maximum(r, g), b)
    # Smooth alpha calculation
    alpha = np.clip((intensity - threshold) / (threshold * feather) * 255.0, 0, 255).astype(np.uint8)
    arr[:,:,3] = alpha
    return Image.fromarray(arr.astype(np.uint8))

# 1. Generate clean transparent PNGs for all Dark Reborn 3D assets
print("Extracting clean transparent alpha cutouts...")
cutout_shield = extract_alpha_cutout(os.path.join(base_dir, "VeniceAI_AxpbSjr1OzMubz_0.jpeg"), threshold=10, feather=3.0)
cutout_shield.save(os.path.join(png_dir, "primary_logo_4k_transparent.png"))
cutout_shield_2k = cutout_shield.resize((2048, 2048), Image.Resampling.LANCZOS)
cutout_shield_2k.save(os.path.join(png_dir, "primary_logo_2k_transparent.png"))
cutout_shield_1k = cutout_shield.resize((1024, 1024), Image.Resampling.LANCZOS)
cutout_shield_1k.save(os.path.join(png_dir, "primary_logo_1k_transparent.png"))

cutout_crest = extract_alpha_cutout(os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_0.png"), threshold=12, feather=2.5)
cutout_crest.save(os.path.join(png_dir, "crest_shield.png"))

cutout_wordmark = extract_alpha_cutout(os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_1.png"), threshold=12, feather=2.5)
cutout_wordmark.save(os.path.join(png_dir, "metallic_wordmark.png"))

cutout_nav = extract_alpha_cutout(os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_2.png"), threshold=12, feather=2.5)
cutout_nav.save(os.path.join(png_dir, "horizontal_nav_lockup.png"))

cutout_wing = extract_alpha_cutout(os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_3.png"), threshold=12, feather=2.5)
cutout_wing.save(os.path.join(png_dir, "cyber_wing_badge.png"))

print("Clean alpha cutouts saved!")

# 2. Build High-Fidelity Photorealistic 3D SVGs
# Embedding the lossless high-res alpha-transparent cutout inside scalable vector containers with SVG filters
def make_photorealistic_svg(png_image, out_svg_path, view_w, view_h, desc="Dark Reborn 3D Asset"):
    import io
    buffered = io.BytesIO()
    # Save as high quality PNG
    png_image.save(buffered, format="PNG", optimize=True)
    b64_data = base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {view_w} {view_h}" width="100%" height="100%">
  <!-- {desc} - Dark Reborn 3D Official Master Asset -->
  <defs>
    <filter id="drRedGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="12" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  <g id="dr-brand-layer" filter="url(#drRedGlow)">
    <image width="{view_w}" height="{view_h}" xlink:href="data:image/png;base64,{b64_data}"/>
  </g>
</svg>"""
    with open(out_svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated photorealistic SVG: {os.path.basename(out_svg_path)} ({view_w}x{view_h})")

# Generate photorealistic SVGs
make_photorealistic_svg(cutout_shield_1k, os.path.join(svg_dir, "logo_primary_3d_lockup.svg"), 1024, 1024, "Primary 3D Metallic Shield Lockup")
make_photorealistic_svg(cutout_nav, os.path.join(svg_dir, "logo_horizontal_wordmark.svg"), 1536, 768, "Horizontal Header Wordmark")
make_photorealistic_svg(cutout_crest, os.path.join(svg_dir, "logo_crest_shield.svg"), 1536, 1536, "Angular Cyber Crest")
make_photorealistic_svg(cutout_wordmark, os.path.join(svg_dir, "logo_metallic_wordmark.svg"), 1536, 768, "3D Metallic Wordmark")
make_photorealistic_svg(cutout_wing, os.path.join(svg_dir, "logo_cyber_wing.svg"), 768, 768, "Cyber Wing Badge")

# Monogram Icon SVG
app_icon_png = Image.open(os.path.join(brand_sys, "03_app_icons_favicons", "android-chrome-512x512.png"))
make_photorealistic_svg(app_icon_png, os.path.join(svg_dir, "logo_monogram_icon.svg"), 512, 512, "App Icon Monogram")

# 3. Clean Vector Monochrome White and Black (0 artifacts, crisp clean lines)
# Crop shield center for clean vector silhouette
im_gray = cutout_shield_1k.convert("L")
arr_g = np.array(im_gray)
# Threshold mask
mask = arr_g > 40

# Create pure clean vector monochrome SVGs
svg_mono_white = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="100%" height="100%">
  <!-- Pure Monochrome White Vector Wireframe / Silhouette -->
  <g fill="none" stroke="#ffffff" stroke-linejoin="round" stroke-linecap="round">
    <!-- Outer Shield Crest -->
    <path d="M 512 80 L 890 270 L 890 540 L 512 940 L 134 540 L 134 270 Z" stroke-width="24"/>
    <path d="M 512 140 L 840 305 L 840 515 L 512 870 L 184 515 L 184 305 Z" stroke-width="12" stroke-dasharray="16 8"/>
    <!-- Inner Beveled Plates -->
    <path d="M 512 210 L 780 345 L 780 490 L 512 790 L 244 490 L 244 345 Z" stroke-width="18"/>
    <!-- Monogram G Segment -->
    <path d="M 470 330 L 320 405 L 320 560 L 480 650 L 480 550 L 400 510 L 400 470 L 470 435 Z" fill="#ffffff" stroke-width="6"/>
    <!-- Monogram R Segment -->
    <path d="M 550 330 L 700 405 L 700 495 L 600 545 L 710 680 L 620 680 L 530 570 L 530 660 L 500 660 L 500 330 Z" fill="#ffffff" stroke-width="6"/>
    <polygon points="550,390 630,430 630,470 550,510" fill="#060709"/>
    <!-- Center Core Diamond -->
    <polygon points="512,430 535,460 512,490 489,460" fill="#ffffff"/>
  </g>
  <text x="512" y="990" font-family="'Orbitron', sans-serif" font-weight="900" font-size="44" letter-spacing="16" fill="#ffffff" text-anchor="middle">GAMES-REBORN</text>
</svg>"""

with open(os.path.join(svg_dir, "logo_monochrome_white.svg"), "w", encoding="utf-8") as f:
    f.write(svg_mono_white)

svg_mono_black = svg_mono_white.replace('#ffffff', '#0a0b0e').replace('#060709', '#ffffff')
with open(os.path.join(svg_dir, "logo_monochrome_black.svg"), "w", encoding="utf-8") as f:
    f.write(svg_mono_black)

print("Monochrome SVGs saved with clean geometry!")
