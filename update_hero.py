import re

with open(r'D:\code\coffieart\index.html', 'r') as f:
    content = f.read()

# Replace the hero section
old_hero = '''<!-- ===== HERO ===== -->
<section class="hero">
<div class="hero-bg absolute inset-0"></div>
<div class="hero-overlay absolute inset-0"></div>
<div class="hero-content relative z-10 w-full px-margin-mobile md:px-margin-desktop md:max-w-container-max md:mx-auto">
<div class="grid grid-cols-1 md:grid-cols-2 gap-0 min-h-[80vh] items-center">
<div class="md:col-span-1 md:pl-0 md:pr-16">
<p class="section-label mb-6 reveal-left">Speciality Coffee</p>
<h1 class="display-xl text-on-surface leading-none mb-0 reveal-left stagger-1">
KOFFIE<br/><span class="brand-gradient-text italic font-normal" style="font-style: italic;">ART</span>
</h1>
<div class="hairline-hairline mt-8 mb-8 reveal-left stagger-2" style="width:80px; height:1px; background:var(--accent);"></div>
<p class="body-lg text-on-surface-variant max-w-md mb-8 reveal-left stagger-2">
A destination for specialty coffee in Mansoura. Where craft meets atmosphere — curated for observation, reflection, and taste.
</p>
<div class="flex flex-col sm:flex-row gap-4 reveal-left stagger-3">
<a href="menu.html" class="btn-primary">Explore Menu</a>
<a href="#visit" class="btn-outline">Visit Us</a>
</div>
</div>
<div class="hidden md:block md:col-span-1"></div>
</div>
</div>
<div class="absolute bottom-8 left-1/2 -translate-x-1/2 scroll-indicator z-10">
<span>Scroll</span>
</div>
</section>'''

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
</section>'''

if old_hero in content:
    content = content.replace(old_hero, new_hero)
    print('Hero replaced successfully')
else:
    print('ERROR: Old hero not found')
    # Try to find the hero section
    import re
    match = re.search(r'<!-- ===== HERO ===== -->.*?</section>', content, re.DOTALL)
    if match:
        print('Found hero section at positions', match.start(), match.end())
        print('Content:', repr(content[match.start():match.start()+200]))

# Fix editorial-block typo
content = content.replace('editorial-block', 'editor-block')
print('Fixed editorial-block -> editor-block:', 'editorial-block' not in content)

# Fix hairline-hairline typo
content = content.replace('hairline-hairline', 'hairline')
print('Fixed hairline-hairline -> hairline:', 'hairline-hairline' not in content)

with open(r'D:\code\coffieart\index.html', 'w') as f:
    f.write(content)
print('index.html updated, total lines:', len(content.splitlines()))
