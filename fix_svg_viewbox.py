import os
import re

svg_dir = r"G:\Venice\reborn_3d_brand_system\01_vectors_svg"
for fname in os.listdir(svg_dir):
    if fname.endswith(".svg"):
        fpath = os.path.join(svg_dir, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check if viewBox exists
        if "viewBox" not in content:
            # Extract width and height
            w_match = re.search(r'width="(\d+)"', content)
            h_match = re.search(r'height="(\d+)"', content)
            if w_match and h_match:
                w, h = w_match.group(1), h_match.group(1)
                # Add viewBox
                content = content.replace(
                    f'<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}">',
                    f'<svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">'
                )
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Added viewBox to {fname} (0 0 {w} {h})")

print("All SVGs are fully responsive with viewBox!")
