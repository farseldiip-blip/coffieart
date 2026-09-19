with open(r'D:\code\coffieart\index.html', 'r') as f:
    lines = f.readlines()

# Find the start and end of the hero section
start_idx = None
end_idx = None
for i, line in enumerate(lines):
    if '<!-- ===== HERO ===== -->' in line:
        start_idx = i
    if start_idx is not None and i > start_idx and line.strip() == '</section>':
        end_idx = i
        break

print(f'Hero section: lines {start_idx+1} to {end_idx+1}')

# New hero content
new_hero_lines = [
    '<!-- ===== HERO ===== -->\n',
    '<section class="hero">\n',
    '<div class="hero__body">\n',
    '<p class="hero__tagline reveal-left">Speciality Coffee</p>\n',
    '<h1 class="display-xl text-on-surface leading-none mb-0 reveal-left stagger-1">\n',
    'KOFFIE<br/><span class="brand-gradient-text">ART</span>\n',
    '</h1>\n',
    '<div class="hairline mt-8 mb-8 reveal-left stagger-2" style="width:80px; background:var(--accent);"></div>\n',
    '<p class="hero__subtitle body-lg text-on-surface-variant mb-8 reveal-left stagger-2">\n',
    'A destination for specialty coffee in Mansoura. Where craft meets atmosphere — curated for observation, reflection, and taste.\n',
    '</p>\n',
    '<div class="hero__actions reveal-left stagger-3">\n',
    '<a href="menu.html" class="btn-primary">Explore Menu</a>\n',
    '<a href="#visit" class="btn-outline">Visit Us</a>\n',
    '</div>\n',
    '</div>\n',
    '<div class="hero__media">\n',
    '<div class="hero__media-slot">\n',
    '</div>\n',
    '</div>\n',
    '<div class="hero__scroll">\n',
    '<span>Scroll</span>\n',
    '</div>\n',
    '</section>\n',
]

if start_idx is not None and end_idx is not None:
    lines = lines[:start_idx] + new_hero_lines + lines[end_idx+1:]
    print('Hero replaced')
else:
    print('ERROR: Could not find hero section')

with open(r'D:\code\coffieart\index.html', 'w') as f:
    f.writelines(lines)
print(f'Done. Lines: {len(lines)}')
