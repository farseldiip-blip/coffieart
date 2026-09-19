with open(r'D:\code\coffieart\css\styles.css', 'r') as f:
    content = f.read()

# Replace the entire Hero CSS section - compact version
old_hero_css = '''/* ── Hero ── */
.hero {
    position: relative;
    width: 100%;
    min-height: 100svh;
    display: grid;
    grid-template-columns: 1fr;
    align-items: center;
    overflow: hidden;
}
@media (min-width: 768px) {
    .hero {
        grid-template-columns: 1fr 1fr;
        min-height: 100svh;
    }
}
.hero__body {
    position: relative;
    z-index: 10;
    padding: 80px 20px;
    max-width: 100%;
}
@media (min-width: 768px) {
    .hero__body {
        padding: 80px 64px 80px 64px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
}
.hero__media {
    position: relative;
    width: 100%;
    min-height: 300px;
    background: var(--surface-subtle);
    overflow: hidden;
}
@media (min-width: 768px) {
    .hero__media {
        min-height: 100svh;
        background: var(--surface-cream);
    }
}
.hero__media-slot {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}
.hero__scroll {
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
}
@media (min-width: 768px) {
    .hero__scroll {
        grid-column: 1 / -1;
        bottom: 40px;
    }
}
@keyframes heroZoom {
    from { transform: scale(1); }
    to { transform: scale(1.08); }
}
@keyframes scrollBounce {
    0%, 100% { transform: translateX(-50%) translateY(0); }
    50% { transform: translateX(-50%) translateY(8px); }
}
.hero__brand {
    font-family: 'Bodoni Moda', serif;
    font-size: clamp(56px, 10vw, 120px);
    font-weight: 700;
    line-height: 0.95;
    letter-spacing: -0.03em;
    color: var(--on-surface);
}
.hero__brand span {
    background: var(--brand-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-style: italic;
    font-weight: normal;
}
.hero__tagline {
    font-family: 'Manrope', sans-serif;
    font-size: clamp(11px, 1.5vw, 13px);
    font-weight: 700;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 24px;
}
.hero__subtitle {
    font-size: clamp(16px, 1.2vw, 18px);
    line-height: 1.7;
    font-weight: 400;
    color: var(--on-surface-variant);
    max-width: 480px;
    margin-bottom: 40px;
}
.hero__actions {
    display: flex;
    flex-direction: column;
    gap: 16px;
}
@media (min-width: 480px) {
    .hero__actions {
        flex-direction: row;
        gap: 24px;
    }
}
.hero__scroll {
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
}
.hero__scroll span {
    font-size: 10px;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--on-surface-muted);
}
.hero__scroll::before {
    content: '';
    width: 1px;
    height: 40px;
    background: var(--outline);
}'''

new_hero_css = '''/* ── Hero ── */
.hero {
    position: relative;
    width: 100%;
    min-height: 60svh;
    display: grid;
    grid-template-columns: 1fr;
    align-items: center;
    overflow: hidden;
    gap: 40px;
}
@media (min-width: 768px) {
    .hero {
        min-height: 50vh;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
    }
}
.hero__body {
    position: relative;
    z-index: 10;
    padding: 40px 20px;
    max-width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
@media (min-width: 768px) {
    .hero__body {
        padding: 60px;
        flex-direction: row;
        justify-content: flex-start;
    }
}
.hero__media {
    position: relative;
    width: 100%;
    min-height: 200px;
    background: var(--surface-subtle);
    overflow: hidden;
    grid-column: 1;
}
@media (min-width: 768px) {
    .hero__media {
        min-height: 400px;
        grid-column: 2;
    }
}
.hero__media-slot {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}
.hero__scroll {
    position: absolute;
    bottom: 24px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 10;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    opacity: 0.4;
    animation: scrollBounce 2s ease-in-out infinite;
    grid-column: 1 / -1;
}
@media (min-width: 768px) {
    .hero__scroll {
        bottom: 32px;
    }
}
@keyframes scrollBounce {
    0%, 100% { transform: translateX(-50%) translateY(0); }
    50% { transform: translateX(-50%) translateY(4px); }
}
.hero__tagline {
    font-family: 'Manrope', sans-serif;
    font-size: clamp(10px, 1.2vw, 12px);
    font-weight: 700;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 8px;
}
.hero__subtitle {
    font-size: clamp(14px, 1.2vw, 16px);
    line-height: 1.6;
    font-weight: 400;
    color: var(--on-surface-variant);
    max-width: 420px;
    margin-bottom: 24px;
}
.hero__actions {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-top: auto;
}
@media (min-width: 480px) {
    .hero__actions {
        flex-direction: row;
        gap: 16px;
    }
}
.hero__deco {
    position: absolute;
    inset: 0;
    background: var(--brand-gradient);
    background-size: 200% 200%;
    animation: gradientShift 8s ease infinite;
    opacity: 0.08;
    pointer-events: none;
}'''

if old_hero_css in content:
    content = content.replace(old_hero_css, new_hero_css)
    print('Hero CSS replaced successfully')
else:
    print('ERROR: Old Hero CSS not found')
    # Debug: find what's around hero
    idx = content.find('/* ── Hero ── */')
    if idx >= 0:
        print(f'Found at index {idx}')
        print(repr(content[idx:idx+500]))

with open(r'D:\code\coffieart\css\styles.css', 'w') as f:
    f.write(content)
print(f'Done. File now has {len(content.splitlines())} lines')