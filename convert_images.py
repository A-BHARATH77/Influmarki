import os
import urllib.parse
from PIL import Image

renames = {
    "Hero.jpeg": "hero.webp",
    "herobackground.jpeg": "hero-background.webp",
    "influmarki.png": "influmarki.webp",
    "About/Brand Architects.png": "About/brand-architects.webp",
    "About/Reel Directors.png": "About/reel-directors.webp",
    "About/Web Architects.png": "About/web-architects.webp",
    "Works/Coffee.JPG": "Works/coffee.webp",
    "Works/DSC01259.JPEG": "Works/dsc01259.webp",
    "Works/Newrizz.png": "Works/newrizz.webp",
    "Works/lagom brochure.png": "Works/lagom-brochure.webp",
    "Works/watch mockup.png": "Works/watch-mockup.webp",
    "Works/work.JPG.jpeg": "Works/work.webp",
    "Clients/MGM.webp": "Clients/mgm.webp",
    "Clients/REDPANDA.webp": "Clients/redpanda.webp",
    "Clients/backstory.webp": "Clients/backstory.webp",
    "Clients/herbivore.webp": "Clients/herbivore.webp",
    "Clients/ignna.webp": "Clients/ignna.webp",
    "Clients/kaidi kitchen.webp": "Clients/kaidi-kitchen.webp",
    "Clients/lagom.webp": "Clients/lagom.webp",
    "Clients/mirosh.webp": "Clients/mirosh.webp",
    "Clients/the bleu label 5.webp": "Clients/the-bleu-label-5.webp",
}

for old_path, new_path in renames.items():
    if os.path.exists(old_path) and old_path != new_path:
        try:
            with Image.open(old_path) as img:
                # Convert to RGB if it's RGBA and format doesn't support alpha, but webp supports alpha
                img.save(new_path, "WEBP")
            print(f"Converted {old_path} to {new_path}")
            os.remove(old_path)
        except Exception as e:
            print(f"Error converting {old_path}: {e}")

with open("index.html", "r") as f:
    content = f.read()

# additional html mappings because of case insensitivity or existing usage
html_replacements = {
    "Clients/mgm.webp": "Clients/mgm.webp",
    "Clients/REDPANDA.webp": "Clients/redpanda.webp"
}

for old_path, new_path in renames.items():
    content = content.replace(old_path, new_path)
    old_url = urllib.parse.quote(old_path)
    if old_url != old_path:
        content = content.replace(old_url, new_path)

for old_path, new_path in html_replacements.items():
    content = content.replace(old_path, new_path)

with open("index.html", "w") as f:
    f.write(content)

print("HTML updated successfully.")
