import re

with open(r'G:\Venice\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The original index.html has a sandbox wrapper.
# Let's extract everything from the first '<!DOCTYPE html>\n<html lang="en">' to the closing '</html>' just before '</div><style>'
start_idx = content.find('<!DOCTYPE html>\n<html lang="en">')
end_idx = content.rfind('</html>\n</div><style>')
if start_idx != -1 and end_idx != -1:
    content = content[start_idx:end_idx+7]
else:
    # try another way
    match = re.search(r'(<!DOCTYPE html>\s*<html lang="en">.*</html>)', content, re.DOTALL)
    if match:
        content = match.group(1)

# Clean up any duplicate doctypes if we messed up
content = re.sub(r'<!DOCTYPE html>\s*<!DOCTYPE html>', '<!DOCTYPE html>', content)

variants = [
    {
        'filename': 'variant1_orange_hex.html',
        'logo': 'VeniceAI_pTh5a9ZX4r0uFk_0.png',
        'primary_color': '#ff8c00', # Dark orange
        'secondary_color': '#ff4500',
        'title': 'GAMES-REBORN (Orange Hex Variant)'
    },
    {
        'filename': 'variant2_red_shield.html',
        'logo': 'VeniceAI_Ao8KtvaJevhlKn_1.png',
        'primary_color': '#dc143c', # Crimson red
        'secondary_color': '#ff0000',
        'title': 'GAMES-REBORN (Red Shield Variant)'
    },
    {
        'filename': 'variant3_dark_red.html',
        'logo': 'VeniceAI_Ao8KtvaJevhlKn_0.png',
        'primary_color': '#8a0303', # Blood red
        'secondary_color': '#b30000',
        'title': 'GAMES-REBORN (Dark Red Variant)'
    }
]

for var in variants:
    var_content = content
    
    # Replace colors
    var_content = var_content.replace('#ff0000', var['primary_color'])
    var_content = var_content.replace('#ff6600', var['secondary_color'])
    
    # Replace title
    var_content = re.sub(r'<title>.*?</title>', f"<title>{var['title']}</title>", var_content)
    
    # Replace nav logo
    nav_logo_html = f'<img src="{var["logo"]}" alt="Games Reborn" style="height: 40px; width: auto; border-radius: 5px;">'
    var_content = re.sub(r'<div class="nav-logo">GAMES-REBORN</div>', nav_logo_html, var_content)
    
    # Replace hero logo
    hero_logo_html = f'<img src="{var["logo"]}" alt="Hero Logo" style="width: 250px; height: 250px; margin: 0 auto 40px; border-radius: 20px; box-shadow: 0 0 60px {var["primary_color"]}40; display: block;">'
    var_content = re.sub(r'<div class="hero-logo">GR</div>', hero_logo_html, var_content)
    
    # Replace footer logo
    footer_logo_html = f'<img src="{var["logo"]}" alt="Footer Logo" style="height: 60px; width: auto; margin-bottom: 20px; border-radius: 5px;">'
    var_content = re.sub(r'<div class="footer-logo">GAMES-REBORN</div>', footer_logo_html, var_content)
    
    # Save the variant
    with open(rf'G:\Venice\{var["filename"]}', 'w', encoding='utf-8') as f:
        f.write(var_content)

print("Recreated 3 variant HTML files.")
