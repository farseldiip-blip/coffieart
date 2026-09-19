import re

with open(r'D:\code\coffieart\index.html', 'r') as f:
    content = f.read()

# Find and replace the hero section using regex
hero_pattern = r'<!-- ===== HERO ===== -->\n<section class="hero">.*?</section>\n'

new_hero = '''<!-- ===== HERO ===== -->
<section class="hero">
<div class="hero__body">
<p class="hero__tagline reveal-left">Speciality Coffee</p>
<h1 class="display-xl text-on-surface leading-none mb-0 reveal-left stagger-1">
KOFFIE<br/><span class="brand-gradient-text">ART</span>
</h1>
<div class="hairline mt-8 mb-8 reveal-left stagger-2" style="width:80px; background:var(--accent);"></div>
<p class="hero__subtitle body-lg text-on-surface-variant mb-8 reveal-left stagger-2">
A destination for specialty coffee in Mansoura. Where craft meets atmosphere — curated for observation, reflection, and taste.
</p>
<div class="hero__actions reveal-left stagger-3">
<a href="menu.html" class="btn-primary">Explore Menu</a>
<a href="#visit" class="btn-outline">Visit Us</a>
</div>
</div>
<div class="hero__media">
<div class="hero__media-slot">
</div>
</div>
<div class="hero__scroll">
<span>Scroll</span>
</div>
</section>
'''

match = re.search(hero_pattern, content)
if match:
    content = content[:match.start()] + new_hero + content[match.end():]
    print('Hero replaced via regex')
else:
    print('ERROR: Hero pattern not found')
    # Debug: show what's around the hero
    idx = content.find('<!-- ===== HERO ===== -->')
    if idx >= 0:
        print(f'Found at index {idx}')
        print(repr(content[idx:idx+500]))

with open(r'D:\code\coffieart\index.html', 'w') as f:
    f.write(content)
print('Done. Lines:', len(content.splitlines()))
