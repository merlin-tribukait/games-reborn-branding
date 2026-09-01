import os, re, glob, urllib.parse, sys

base_dir = os.path.dirname(os.path.abspath(__file__))
html_files = sorted(glob.glob(base_dir + "/**/*.html", recursive=True))

missing = 0
checked_links = 0

print(f"Verifying {len(html_files)} HTML files in {base_dir}...")

for h in html_files:
    if ".git" in h: continue
    rel_h = os.path.relpath(h, base_dir)
    file_dir = os.path.dirname(h)
    
    with open(h, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    # Check images & media
    srcs = re.findall(r"""src=[\x27\"]([^\x27\"]+)[\x27\"]""", content)
    for s in srcs:
        if s.startswith(("http://", "https://", "data:", "blob:", "javascript:")): continue
        target = os.path.normpath(os.path.join(file_dir, urllib.parse.unquote(s)))
        checked_links += 1
        if not os.path.exists(target):
            print(f"  [MISSING SRC] in {rel_h}: {s} -> {target}")
            missing += 1

    # Check stylesheets & favicons
    links = re.findall(r"""<link [^>]*href=[\x27\"]([^\x27\"]+)[\x27\"]""", content)
    for l in links:
        if l.startswith(("http://", "https://", "data:")): continue
        target = os.path.normpath(os.path.join(file_dir, urllib.parse.unquote(l)))
        checked_links += 1
        if not os.path.exists(target):
            print(f"  [MISSING LINK] in {rel_h}: {l} -> {target}")
            missing += 1

    # Check local a hrefs
    a_hrefs = re.findall(r"""<a [^>]*href=[\x27\"]([^\x27\"]+)[\x27\"]""", content)
    for a in a_hrefs:
        if a.startswith(("http://", "https://", "mailto:", "tel:", "javascript:", "#")): continue
        a_clean = a.split("#")[0]
        if not a_clean: continue
        target = os.path.normpath(os.path.join(file_dir, urllib.parse.unquote(a_clean)))
        checked_links += 1
        if not os.path.exists(target):
            print(f"  [MISSING A HREF] in {rel_h}: {a} -> {target}")
            missing += 1

print(f"\n--> Checked {checked_links} assets/links across {len(html_files)} HTML pages.")
if missing == 0:
    print("--> 100% SUCCESS: 0 BROKEN ASSETS / LINKS!")
else:
    print(f"--> FAILED: {missing} broken assets/links found.")
    sys.exit(1)
