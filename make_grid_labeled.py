import os
from PIL import Image, ImageDraw, ImageFont

folder = r"G:\Venice"
files = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpeg', '.jpg')) and f != "grid.jpg"]
files.sort()

thumbs = []
for f in files:
    path = os.path.join(folder, f)
    try:
        img = Image.open(path)
        img = img.resize((200, 200))
        thumbs.append((f, img))
    except Exception as e:
        print(f"Error loading {f}: {e}")

cols = 5
rows = (len(thumbs) + cols - 1) // cols

grid_w = cols * 200
grid_h = rows * 200

grid = Image.new('RGB', (grid_w, grid_h), color=(255, 255, 255))
draw = ImageDraw.Draw(grid)

for i, (name, img) in enumerate(thumbs):
    r = i // cols
    c = i % cols
    x = c * 200
    y = r * 200
    grid.paste(img, (x, y))
    
    # Draw text background
    draw.rectangle([x, y, x+200, y+20], fill=(0,0,0,128))
    # Draw text
    draw.text((x+5, y+2), name[:15], fill=(255,255,255))

grid.save(r"G:\Venice\grid_labeled.jpg")
print("Grid saved to G:\Venice\grid_labeled.jpg")
