with open(r'D:\code\coffieart\css\styles.css', 'r') as f:
    content = f.read()

# Add grid-column to hero__body
old_body = '''.hero__body {
    position: relative;
    z-index: 10;
    padding: 80px 20px;
    max-width: 100%;
}'''
new_body = '''.hero__body {
    position: relative;
    z-index: 10;
    padding: 80px 20px;
    max-width: 100%;
    grid-column: 1;
}'''
if old_body in content:
    content = content.replace(old_body, new_body)
    print('Added grid-column to hero__body')

# Add grid-column to hero__media
old_media = '''.hero__media {
    position: relative;
    width: 100%;
    min-height: 300px;
    background: var(--surface-subtle);
    overflow: hidden;
}'''
new_media = '''.hero__media {
    position: relative;
    width: 100%;
    min-height: 300px;
    background: var(--surface-subtle);
    overflow: hidden;
    grid-column: 1;
}'''
if old_media in content:
    content = content.replace(old_media, new_media)
    print('Added grid-column to hero__media')

# Add grid-column to hero__media media query
old_media_mq = '''@media (min-width: 768px) {
    .hero__media {
        min-height: 100svh;
        background: var(--surface-cream);
    }
}'''
new_media_mq = '''@media (min-width: 768px) {
    .hero__media {
        min-height: 100svh;
        background: var(--surface-cream);
        grid-column: 2;
    }
}'''
if old_media_mq in content:
    content = content.replace(old_media_mq, new_media_mq)
    print('Added grid-column to hero__media media query')

# Add grid-column to hero__scroll
old_scroll = '''.hero__scroll {
    position: absolute;
    bottom: 32px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 10;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    opacity: 0.4;
    animation: scrollBounce 2s ease-in-out infinite;
}'''
new_scroll = '''.hero__scroll {
    position: absolute;
    bottom: 32px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 10;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    opacity: 0.4;
    animation: scrollBounce 2s ease-in-out infinite;
    grid-column: 1 / -1;
}'''
if old_scroll in content:
    content = content.replace(old_scroll, new_scroll)
    print('Added grid-column to hero__scroll')

# Add media query for hero__scroll
old_scroll_end = '.hero__scroll span {'
new_scroll_mq = '''@media (min-width: 768px) {
    .hero__scroll {
        bottom: 40px;
    }
}
.hero__scroll span {'''
if old_scroll_end in content and '@media (min-width: 768px) {' not in content.split('.hero__scroll span')[0].split('.hero__scroll')[-1]:
    content = content.replace(old_scroll_end, new_scroll_mq)
    print('Added media query for hero__scroll')

# Add decorative gradient to hero__media-slot
old_slot = '''.hero__media-slot {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}'''
new_slot = '''.hero__media-slot {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    background: linear-gradient(135deg, var(--surface-subtle) 0%, var(--surface-cream) 100%);
}
.hero__media-slot::after {
    content: '';
    position: absolute;
    inset: 0;
    background: var(--brand-gradient);
    opacity: 0.08;
    pointer-events: none;
}'''
if old_slot in content:
    content = content.replace(old_slot, new_slot)
    print('Added decorative gradient to hero__media-slot')

with open(r'D:\code\coffieart\css\styles.css', 'w') as f:
    f.write(content)
print(f'Done. File length: {len(content.splitlines())} lines')
