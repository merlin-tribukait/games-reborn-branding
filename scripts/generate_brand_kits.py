import os
from PIL import Image, ImageOps, ImageEnhance, ImageFilter, ImageDraw, ImageFont

base_dir = r"G:\Venice"
assets_dir = os.path.join(base_dir, "brand_assets")

os.makedirs(os.path.join(assets_dir, "orange_ember"), exist_ok=True)
os.makedirs(os.path.join(assets_dir, "crimson_shield"), exist_ok=True)
os.makedirs(os.path.join(assets_dir, "dark_reborn"), exist_ok=True)

def create_monochrome(img_path, out_path, tint=None):
    im = Image.open(img_path).convert("RGBA")
    # Convert to grayscale
    gray = ImageOps.grayscale(im.convert("RGB"))
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(gray)
    contrasted = enhancer.enhance(2.0)
    
    if tint:
        # Colorize grayscale
        colorized = ImageOps.colorize(contrasted, black=(10, 10, 10), white=tint)
        colorized.save(out_path)
    else:
        contrasted.save(out_path)

def create_app_icon(img_path, out_path, glow_color=(255, 120, 0)):
    im = Image.open(img_path).convert("RGBA")
    size = (512, 512)
    # Center crop / resize
    im.thumbnail((440, 440), Image.Resampling.LANCZOS)
    
    canvas = Image.new("RGBA", size, (15, 15, 18, 255))
    draw = ImageDraw.Draw(canvas)
    
    # Draw rounded rectangle border with subtle glow
    draw.rounded_rectangle([10, 10, 502, 502], radius=90, outline=glow_color, width=4)
    
    # Paste centered
    offset = ((size[0] - im.width) // 2, (size[1] - im.height) // 2)
    canvas.paste(im, offset, mask=im if im.mode == 'RGBA' else None)
    canvas.save(out_path)

def create_favicon(img_path, out_path):
    im = Image.open(img_path).convert("RGBA")
    im = im.resize((64, 64), Image.Resampling.LANCZOS)
    im.save(out_path)

def create_social_banner(img_path, out_path, title_text="GAMES-REBORN", subtitle="PLAY. BUILD. CONQUER.", accent_color=(255, 100, 0)):
    im = Image.open(img_path).convert("RGBA")
    banner_size = (1200, 630)
    banner = Image.new("RGBA", banner_size, (10, 10, 14, 255))
    
    # Resize image to fit nicely on the left or center
    im.thumbnail((500, 500), Image.Resampling.LANCZOS)
    
    # Draw background gradient/glow
    draw = ImageDraw.Draw(banner)
    for r in range(300, 0, -10):
        alpha = int(35 * (1 - r/300))
        draw.ellipse([300-r, 315-r, 300+r, 315+r], fill=(accent_color[0], accent_color[1], accent_color[2], alpha))
    
    # Paste logo on left
    banner.paste(im, (80, (630 - im.height)//2), mask=im if im.mode == 'RGBA' else None)
    
    # Save banner
    banner.save(out_path)

print("Processing Brand Kit 1: Orange Ember...")
# 1. Primary Logo
im_p1 = Image.open(os.path.join(base_dir, "VeniceAI_pTh5a9ZX4r0uFk_0.png"))
im_p1.save(os.path.join(assets_dir, "orange_ember", "01_primary_logo.png"))
create_app_icon(os.path.join(base_dir, "VeniceAI_pTh5a9ZX4r0uFk_0.png"), os.path.join(assets_dir, "orange_ember", "02_app_icon.png"), glow_color=(255, 140, 0))
create_favicon(os.path.join(base_dir, "VeniceAI_pTh5a9ZX4r0uFk_0.png"), os.path.join(assets_dir, "orange_ember", "favicon.png"))
create_monochrome(os.path.join(base_dir, "VeniceAI_pTh5a9ZX4r0uFk_0.png"), os.path.join(assets_dir, "orange_ember", "03_monochrome_white.png"), tint=(255, 255, 255))

# Shield Crest
im_s1 = Image.open(os.path.join(base_dir, "VeniceAI_pTh5a9ZX4r0uFk_1.png"))
im_s1.save(os.path.join(assets_dir, "orange_ember", "04_shield_crest.png"))

# Horizontal Wordmark
im_h1 = Image.open(os.path.join(base_dir, "VeniceAI_pTh5a9ZX4r0uFk_2.png"))
im_h1.save(os.path.join(assets_dir, "orange_ember", "05_horizontal_wordmark.png"))

# Roundel Badge
im_r1 = Image.open(os.path.join(base_dir, "VeniceAI_pTh5a9ZX4r0uFk_3.png"))
im_r1.save(os.path.join(assets_dir, "orange_ember", "06_roundel_badge.png"))

create_social_banner(os.path.join(base_dir, "VeniceAI_pTh5a9ZX4r0uFk_0.png"), os.path.join(assets_dir, "orange_ember", "07_social_banner.png"), accent_color=(255, 140, 0))


print("Processing Brand Kit 2: Crimson Shield...")
# Primary Logo
im_p2 = Image.open(os.path.join(base_dir, "VeniceAI_Ao8KtvaJevhlKn_1.png"))
im_p2.save(os.path.join(assets_dir, "crimson_shield", "01_primary_logo.png"))
create_app_icon(os.path.join(base_dir, "VeniceAI_Ao8KtvaJevhlKn_1.png"), os.path.join(assets_dir, "crimson_shield", "02_app_icon.png"), glow_color=(220, 20, 60))
create_favicon(os.path.join(base_dir, "VeniceAI_Ao8KtvaJevhlKn_1.png"), os.path.join(assets_dir, "crimson_shield", "favicon.png"))
create_monochrome(os.path.join(base_dir, "VeniceAI_Ao8KtvaJevhlKn_1.png"), os.path.join(assets_dir, "crimson_shield", "03_monochrome_white.png"), tint=(255, 255, 255))

# Spiky Crest
im_s2 = Image.open(os.path.join(base_dir, "VeniceAI_Ao8KtvaJevhlKn_2.png"))
im_s2.save(os.path.join(assets_dir, "crimson_shield", "04_spiky_crest.png"))

# Horizontal Wordmark
im_h2 = Image.open(os.path.join(base_dir, "VeniceAI_Ao8KtvaJevhlKn_0.png"))
im_h2.save(os.path.join(assets_dir, "crimson_shield", "05_horizontal_wordmark.png"))

# Vertical Emblem
im_v2 = Image.open(os.path.join(base_dir, "VeniceAI_Ao8KtvaJevhlKn_3.png"))
im_v2.save(os.path.join(assets_dir, "crimson_shield", "06_vertical_emblem.png"))

# Winged Badge & Merch Mockups
Image.open(os.path.join(base_dir, "VeniceAI_EZvbV5HcciNEEU_1.png")).save(os.path.join(assets_dir, "crimson_shield", "07_business_card_mockup.png"))
Image.open(os.path.join(base_dir, "VeniceAI_EZvbV5HcciNEEU_2.png")).save(os.path.join(assets_dir, "crimson_shield", "08_winged_badge.png"))
Image.open(os.path.join(base_dir, "VeniceAI_EZvbV5HcciNEEU_3.png")).save(os.path.join(assets_dir, "crimson_shield", "09_apparel_tshirt_mockup.png"))
create_social_banner(os.path.join(base_dir, "VeniceAI_Ao8KtvaJevhlKn_1.png"), os.path.join(assets_dir, "crimson_shield", "10_social_banner.png"), accent_color=(220, 20, 60))


print("Processing Brand Kit 3: Dark Reborn (Cyberpunk 3D)...")
# Primary 3D Metallic Shield
im_p3 = Image.open(os.path.join(base_dir, "VeniceAI_AxpbSjr1OzMubz_0.jpeg"))
im_p3.save(os.path.join(assets_dir, "dark_reborn", "01_primary_3d_shield.jpg"), quality=95)
create_app_icon(os.path.join(base_dir, "VeniceAI_AxpbSjr1OzMubz_0.jpeg"), os.path.join(assets_dir, "dark_reborn", "02_app_icon.png"), glow_color=(200, 30, 30))
create_favicon(os.path.join(base_dir, "VeniceAI_AxpbSjr1OzMubz_0.jpeg"), os.path.join(assets_dir, "dark_reborn", "favicon.png"))
create_monochrome(os.path.join(base_dir, "VeniceAI_AxpbSjr1OzMubz_0.jpeg"), os.path.join(assets_dir, "dark_reborn", "03_monochrome_white.png"), tint=(240, 240, 240))

# Wide Cinematic Banner
Image.open(os.path.join(base_dir, "VeniceAI_AxpbSjr1OzMubz_1.jpeg")).save(os.path.join(assets_dir, "dark_reborn", "04_cinematic_wide_banner.jpg"), quality=95)

# 3D Metallic Angular Crest
Image.open(os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_0.png")).save(os.path.join(assets_dir, "dark_reborn", "05_metallic_crest.png"))

# 3D Metallic Wordmark
Image.open(os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_1.png")).save(os.path.join(assets_dir, "dark_reborn", "06_metallic_wordmark.png"))

# Horizontal 3D Lockup
Image.open(os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_2.png")).save(os.path.join(assets_dir, "dark_reborn", "07_horizontal_lockup.png"))

# Modern Wing Badge
Image.open(os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_3.png")).save(os.path.join(assets_dir, "dark_reborn", "08_wing_badge.png"))

create_social_banner(os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_0.png"), os.path.join(assets_dir, "dark_reborn", "09_social_banner.png"), accent_color=(180, 20, 20))

print("All Brand Kits Generated Successfully!")
