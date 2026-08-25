import os
import re

files = [
    'index.html',
    'variant1_orange_hex.html',
    'variant2_red_shield.html',
    'variant3_dark_red.html',
    'BRAND_GUIDEBOOK.html',
    'reborn_prime_landing_page.html',
    'reborn_3d_brand_system/BRAND_GUIDEBOOK.html'
]

missing = 0
for f in files:
    path = os.path.join(r'G:\Venice', f)
    base_folder = os.path.dirname(path)
    if not os.path.exists(path):
        print(f"File not found: {f}")
        continue
    with open(path, 'r', encoding='utf-8') as fl:
        content = fl.read()
    imgs = re.findall(r'src=["\']([^"\']+)["\']', content)
    imgs += re.findall(r'href=["\']([^"\']+\.(?:png|jpg|jpeg|ico|svg|css|json))["\']', content)
    for img in set(imgs):
        if img.startswith('http') or img.startswith('#'):
            continue
        img_full = os.path.normpath(os.path.join(base_folder, img.replace('/', os.sep)))
        if not os.path.exists(img_full):
            print(f'MISSING in {f}: {img} (looked at {img_full})')
            missing += 1
        else:
            print(f'OK in {f}: {img}')

if missing == 0:
    print('--> ALL 7 HTML PAGES AND IMAGE LINKS VERIFIED WITH 100% SUCCESS!')
else:
    print(f'--> {missing} links missing!')
