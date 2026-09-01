import os
import shutil
from PIL import Image, ImageOps, ImageEnhance, ImageDraw, ImageFilter
import numpy as np

base_dir = r"G:\Venice"
brain_dir = r"C:\Users\HACK\.gemini\antigravity-cli\brain\37d32ccb-8f73-4081-ba27-e40e886e8ba6"
brand_sys = os.path.join(base_dir, "reborn_3d_brand_system")

# Create folder hierarchy
folders = [
    "01_vectors_svg",
    "02_transparent_png",
    "03_app_icons_favicons",
    "04_social_media_kit",
    "05_wallpapers_4k",
    "06_merch_and_mockups",
    "07_design_tokens_and_code"
]
for f in folders:
    os.makedirs(os.path.join(brand_sys, f), exist_ok=True)

# 1. Copy generated AI mockups
for fname in os.listdir(brain_dir):
    if fname.startswith("reborn_desk_setup") and fname.endswith(".png"):
        shutil.copy(os.path.join(brain_dir, fname), os.path.join(brand_sys, "06_merch_and_mockups", "mockup_battlestation_desk_setup.png"))
    if fname.startswith("reborn_apparel_hoodie") and fname.endswith(".png"):
        shutil.copy(os.path.join(brain_dir, fname), os.path.join(brand_sys, "06_merch_and_mockups", "mockup_esports_jersey_hoodie.png"))

# Copy 5K wide banner
shutil.copy(os.path.join(base_dir, "VeniceAI_AxpbSjr1OzMubz_1.jpeg"), os.path.join(brand_sys, "06_merch_and_mockups", "mockup_cinematic_5k_header.jpg"))

print("Mockups copied!")

# 2. Transparent PNG extraction & generation
# Primary 3D Shield
im_shield = Image.open(os.path.join(base_dir, "VeniceAI_AxpbSjr1OzMubz_0.jpeg")).convert("RGBA")
# Convert near-black background to transparent
arr = np.array(im_shield)
# Check luminance
r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
# Luminance
lum = 0.299 * r + 0.587 * g + 0.114 * b
# Smooth alpha mask for dark background cutout
alpha = np.clip((lum - 8) * 4.0, 0, 255).astype(np.uint8)
# Replace alpha where black
arr[:,:,3] = alpha
im_transparent = Image.fromarray(arr)

# Save 4K, 2K, 1K transparent PNGs
im_transparent.save(os.path.join(brand_sys, "02_transparent_png", "primary_logo_4k_transparent.png"))
im_2k = im_transparent.resize((2048, 2048), Image.Resampling.LANCZOS)
im_2k.save(os.path.join(brand_sys, "02_transparent_png", "primary_logo_2k_transparent.png"))
im_1k = im_transparent.resize((1024, 1024), Image.Resampling.LANCZOS)
im_1k.save(os.path.join(brand_sys, "02_transparent_png", "primary_logo_1k_transparent.png"))

# Monochrome Black and White
gray = ImageOps.grayscale(im_shield.convert("RGB"))
enhancer = ImageEnhance.Contrast(gray)
mono_white = ImageOps.colorize(enhancer.enhance(2.5), black=(0,0,0), white=(255,255,255))
mono_white.save(os.path.join(brand_sys, "02_transparent_png", "monochrome_white.png"))

mono_black = ImageOps.colorize(enhancer.enhance(2.5), black=(255,255,255), white=(15,15,15))
mono_black.save(os.path.join(brand_sys, "02_transparent_png", "monochrome_black.png"))

# Copy horizontal & crest assets
shutil.copy(os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_2.png"), os.path.join(brand_sys, "02_transparent_png", "horizontal_nav_lockup.png"))
shutil.copy(os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_0.png"), os.path.join(brand_sys, "02_transparent_png", "crest_shield.png"))
shutil.copy(os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_1.png"), os.path.join(brand_sys, "02_transparent_png", "metallic_wordmark.png"))
shutil.copy(os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_3.png"), os.path.join(brand_sys, "02_transparent_png", "cyber_wing_badge.png"))

print("Transparent PNGs & marks created!")

# 3. App Icons & Favicons
icon_sizes = [16, 32, 48, 64, 128, 256, 512, 1024]
im_icon_base = im_1k.crop((100, 100, 924, 924))

# Create Squircle iOS/Android icon
app_canvas = Image.new("RGBA", (1024, 1024), (10, 11, 14, 255))
draw = ImageDraw.Draw(app_canvas)
# Rounded squircle
draw.rounded_rectangle([20, 20, 1004, 1004], radius=220, fill=(14, 16, 20), outline=(200, 25, 25), width=10)
# Paste logo centered
logo_thumb = im_icon_base.resize((760, 760), Image.Resampling.LANCZOS)
app_canvas.paste(logo_thumb, (132, 132), mask=logo_thumb)
app_canvas.save(os.path.join(brand_sys, "03_app_icons_favicons", "app_icon_ios_squircle_1024.png"))

# Android 512 & 192
app_512 = app_canvas.resize((512, 512), Image.Resampling.LANCZOS)
app_512.save(os.path.join(brand_sys, "03_app_icons_favicons", "android-chrome-512x512.png"))
app_192 = app_canvas.resize((192, 192), Image.Resampling.LANCZOS)
app_192.save(os.path.join(brand_sys, "03_app_icons_favicons", "android-chrome-192x192.png"))

# Apple touch icon 180
app_180 = app_canvas.resize((180, 180), Image.Resampling.LANCZOS)
app_180.save(os.path.join(brand_sys, "03_app_icons_favicons", "apple-touch-icon.png"))

# Favicon .ico bundle
ico_imgs = [im_icon_base.resize((s, s), Image.Resampling.LANCZOS) for s in [16, 32, 48, 64, 128, 256]]
ico_imgs[0].save(os.path.join(brand_sys, "03_app_icons_favicons", "favicon.ico"), format="ICO", sizes=[(s,s) for s in [16, 32, 48, 64, 128, 256]])
im_icon_base.resize((32, 32)).save(os.path.join(brand_sys, "03_app_icons_favicons", "favicon-32x32.png"))
im_icon_base.resize((16, 16)).save(os.path.join(brand_sys, "03_app_icons_favicons", "favicon-16x16.png"))

print("App icons and favicons created!")

# 4. Social Media Kit
def make_social(dim, out_name, logo_scale=0.6, pos="center"):
    canvas = Image.new("RGB", dim, (8, 9, 12))
    draw = ImageDraw.Draw(canvas)
    
    # Background glowing grid & laser lines
    w, h = dim
    # Laser red grid
    for x in range(0, w, 80):
        draw.line([(x, 0), (x, h)], fill=(20, 22, 28), width=1)
    for y in range(0, h, 80):
        draw.line([(y, 0), (w, y)], fill=(20, 22, 28), width=1)
        
    # Central glow
    glow_color = (190, 20, 20)
    center_x = w // 2 if pos == "center" else w // 3
    center_y = h // 2
    for r in range(min(w, h)//2, 0, -15):
        alpha = int(25 * (1 - r/(min(w, h)//2)))
        draw.ellipse([center_x-r, center_y-r, center_x+r, center_y+r], fill=(glow_color[0], glow_color[1], glow_color[2]))
    
    # Overlay logo
    target_h = int(h * logo_scale)
    target_w = target_h
    logo_res = im_icon_base.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    paste_x = (w - target_w) // 2 if pos == "center" else 100
    paste_y = (h - target_h) // 2
    canvas.paste(logo_res, (paste_x, paste_y), mask=logo_res)
    canvas.save(os.path.join(brand_sys, "04_social_media_kit", out_name), quality=95)

make_social((1500, 500), "twitter_x_header_1500x500.jpg", logo_scale=0.75, pos="left")
make_social((2560, 1440), "youtube_banner_2560x1440.jpg", logo_scale=0.55, pos="center")
make_social((1920, 1080), "twitch_offline_banner_1920x1080.jpg", logo_scale=0.6, pos="center")
make_social((960, 540), "discord_server_banner_960x540.jpg", logo_scale=0.7, pos="center")
make_social((1200, 630), "facebook_linkedin_cover_1200x630.jpg", logo_scale=0.65, pos="left")
make_social((1080, 1080), "instagram_square_post_1080x1080.jpg", logo_scale=0.7, pos="center")
make_social((1080, 1920), "instagram_story_1080x1920.jpg", logo_scale=0.45, pos="center")
app_512.save(os.path.join(brand_sys, "04_social_media_kit", "discord_avatar_512x512.png"))

print("Social Media Kit generated!")

# 5. Wallpapers 4K & Ultrawide
make_social((3840, 2160), "../05_wallpapers_4k/desktop_4k_wallpaper_3840x2160.jpg", logo_scale=0.5, pos="center")
make_social((5120, 2160), "../05_wallpapers_4k/ultrawide_5k_wallpaper_5120x2160.jpg", logo_scale=0.55, pos="center")
make_social((1080, 2400), "../05_wallpapers_4k/mobile_oled_wallpaper_1080x2400.jpg", logo_scale=0.45, pos="center")

print("Wallpapers generated!")
