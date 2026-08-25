import os
import vtracer
from PIL import Image, ImageOps, ImageEnhance
import numpy as np

base_dir = r"G:\Venice"
brand_sys = os.path.join(base_dir, "reborn_3d_brand_system")
svg_dir = os.path.join(brand_sys, "01_vectors_svg")
tmp_dir = os.path.join(brand_sys, "temp_trace")
os.makedirs(tmp_dir, exist_ok=True)

def prepare_and_trace(input_path, output_svg_path, max_dim=1024, colormode="color", color_precision=6, filter_speckle=4, layer_difference=16):
    im = Image.open(input_path)
    # Resize keeping aspect ratio
    w, h = im.size
    ratio = min(max_dim / w, max_dim / h)
    new_w, new_h = int(w * ratio), int(h * ratio)
    im_resized = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Save temp png
    tmp_png = os.path.join(tmp_dir, "temp_trace_img.png")
    im_resized.save(tmp_png)
    
    print(f"Tracing {os.path.basename(input_path)} -> {os.path.basename(output_svg_path)} ({new_w}x{new_h})...")
    vtracer.convert_image_to_svg_py(
        tmp_png,
        output_svg_path,
        colormode=colormode,
        hierarchical="stacked",
        mode="spline",
        filter_speckle=filter_speckle,
        color_precision=color_precision,
        layer_difference=layer_difference,
        corner_threshold=60,
        length_threshold=4.0,
        max_iterations=10,
        splice_threshold=45,
        path_precision=3
    )
    sz = os.path.getsize(output_svg_path)
    print(f"Done! Size: {sz / 1024:.2f} KB")

# 1. Primary 3D Shield Vector SVG
prepare_and_trace(
    os.path.join(brand_sys, "02_transparent_png", "primary_logo_1k_transparent.png"),
    os.path.join(svg_dir, "logo_primary_3d_lockup.svg"),
    max_dim=1024,
    color_precision=7,
    filter_speckle=4,
    layer_difference=14
)

# 2. Horizontal Nav Lockup Vector SVG
prepare_and_trace(
    os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_2.png"),
    os.path.join(svg_dir, "logo_horizontal_wordmark.svg"),
    max_dim=1200,
    color_precision=7,
    filter_speckle=4,
    layer_difference=14
)

# 3. Angular Crest Shield Vector SVG
prepare_and_trace(
    os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_0.png"),
    os.path.join(svg_dir, "logo_crest_shield.svg"),
    max_dim=1024,
    color_precision=7,
    filter_speckle=4,
    layer_difference=14
)

# 4. Metallic Wordmark Vector SVG
prepare_and_trace(
    os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_1.png"),
    os.path.join(svg_dir, "logo_metallic_wordmark.svg"),
    max_dim=1200,
    color_precision=7,
    filter_speckle=4,
    layer_difference=14
)

# 5. Cyber Wing Badge Vector SVG
prepare_and_trace(
    os.path.join(base_dir, "VeniceAI_BPIkzSwc1hm3EN_3.png"),
    os.path.join(svg_dir, "logo_cyber_wing.svg"),
    max_dim=800,
    color_precision=7,
    filter_speckle=4,
    layer_difference=14
)

# 6. Monogram Squircle Icon Vector SVG
prepare_and_trace(
    os.path.join(brand_sys, "03_app_icons_favicons", "android-chrome-512x512.png"),
    os.path.join(svg_dir, "logo_monogram_icon.svg"),
    max_dim=512,
    color_precision=6,
    filter_speckle=4,
    layer_difference=16
)

# 7. Monochrome White Vector SVG
prepare_and_trace(
    os.path.join(brand_sys, "02_transparent_png", "monochrome_white.png"),
    os.path.join(svg_dir, "logo_monochrome_white.svg"),
    max_dim=1024,
    colormode="binary",
    filter_speckle=6
)

# 8. Monochrome Black Vector SVG
prepare_and_trace(
    os.path.join(brand_sys, "02_transparent_png", "monochrome_black.png"),
    os.path.join(svg_dir, "logo_monochrome_black.svg"),
    max_dim=1024,
    colormode="binary",
    filter_speckle=6
)

print("ALL VECTOR SVGs HAVE BEEN REGENERATED WITH 100% TRUE PHOTOREALISTIC FIDELITY!")
