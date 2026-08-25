import vtracer
import inspect

try:
    print(inspect.signature(vtracer.convert_image_to_svg_py))
except Exception as e:
    print("Sig error:", e)

# Test run on one image
try:
    vtracer.convert_image_to_svg_py(
        r"G:\Venice\brand_assets\dark_reborn\01_primary_3d_shield.jpg",
        r"G:\Venice\test_trace.svg",
        colormode="color",        # ["color"] or "binary"
        hierarchical="stacked",   # ["stacked"] or "cutout"
        mode="spline",           # ["spline"], "polygon", "none"
        filter_speckle=4,        # default: 4
        color_precision=8,       # default: 6, max: 8
        layer_difference=16,     # default: 16
        corner_threshold=60,     # default: 60
        length_threshold=4.0,    # default: 4.0
        max_iterations=10,       # default: 10
        splice_threshold=45,     # default: 45
        path_precision=3         # default: 8
    )
    print("Vtracer test succeeded!")
except Exception as e:
    print("Vtracer run error:", e)
