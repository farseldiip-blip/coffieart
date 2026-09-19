with open(r'D:\code\coffieart\css\styles.css', 'r') as f:
    lines = f.readlines()

# Find the Hero section start and end
start_idx = None
end_idx = None
for i, line in enumerate(lines):
    if '/* ── Hero ── */' in line:
        start_idx = i
    if start_idx is not None:
        # End is the next section comment or end of file
        if i > start_idx and '/* ──' in line and i > start_idx + 2:
            # Check if this is a new section
            for j in range(start_idx + 1, i):
                if '/*' in lines[j]:
                    end_idx = j
                    break
        if end_idx is None and i == len(lines) - 1:
            end_idx = i + 1

print(f'Hero section: lines {start_idx+1} to {end_idx if end_idx else "end"}')

# New Hero CSS content
new_hero = [
    '/* ── Hero ── */\n',
    '.hero {\n',
    '    position: relative;\n',
    '    width: 100%;\n',
    '    min-height: 60svh;\n',
    '    display: grid;\n',
    '    grid-template-columns: 1fr;\n',
    '    align-items: center;\n',
    '    overflow: hidden;\n',
    '    gap: 40px;\n',
    '}\n',
    '@media (min-width: 768px) {\n',
    '    .hero {\n',
    '        min-height: 50vh;\n',
    '        grid-template-columns: 1fr 1fr;\n',
    '        gap: 80px;\n',
    '    }\n',
    '}\n',
    '.hero__body {\n',
    '    position: relative;\n',
    '    z-index: 10;\n',
    '    padding: 40px 20px;\n',
    '    max-width: 100%;\n',
    '    display: flex;\n',
    '    flex-direction: column;\n',
    '    justify-content: center;\n',
    '}\n',
    '@media (min-width: 768px) {\n',
    '    .hero__body {\n',
    '        padding: 60px;\n',
    '        flex-direction: row;\n',
    '        justify-content: flex-start;\n',
    '    }\n',
    '}\n',
    '.hero__media {\n',
    '    position: relative;\n',
    '    width: 100%;\n',
    '    min-height: 200px;\n',
    '    background: var(--surface-subtle);\n',
    '    overflow: hidden;\n',
    '    grid-column: 1;\n',
    '}\n',
    '@media (min-width: 768px) {\n',
    '    .hero__media {\n',
    '        min-height: 400px;\n',
    '        grid-column: 2;\n',
    '    }\n',
    '}\n',
    '.hero__media-slot {\n',
    '    width: 100%;\n',
    '    height: 100%;\n',
    '    display: flex;\n',
    '    align-items: center;\n',
    '    justify-content: center;\n',
    '    position: relative;\n',
    '    background: linear-gradient(135deg, var(--surface-subtle) 0%, var(--surface-cream) 100%);\n',
    '}\n',
    '.hero__media-slot::after {\n',
    '    content: "";\n',
    '    position: absolute;\n',
    '    inset: 0;\n',
    '    background: var(--brand-gradient);\n',
    '    opacity: 0.08;\n',
    '    pointer-events: none;\n',
    '}\n',
    '.hero__scroll {\n',
    '    position: absolute;\n',
    '    bottom: 24px;\n',
    '    left: 50%;\n',
    '    transform: translateX(-50%);\n',
    '    z-index: 10;\n',
    '    display: flex;\n',
    '    flex-direction: column;\n',
    '    align-items: center;\n',
    '    gap: 4px;\n',
    '    opacity: 0.4;\n',
    '    animation: scrollBounce 2s ease-in-out infinite;\n',
    '    grid-column: 1 / -1;\n',
    '}\n',
    '@media (min-width: 768px) {\n',
    '    .hero__scroll {\n',
    '        bottom: 32px;\n',
    '    }\n',
    '}\n',
    '@keyframes scrollBounce {\n',
    '    0%, 100% { transform: translateX(-50%) translateY(0); }\n',
    '    50% { transform: translateX(-50%) translateY(4px); }\n',
    '}\n',
    '.hero__tagline {\n',
    '    font-family: \'Manrope\', sans-serif;\n',
    '    font-size: clamp(10px, 1.2vw, 12px);\n',
    '    font-weight: 700;\n',
    '    letter-spacing: 0.3em;\n',
    '    text-transform: uppercase;\n',
    '    color: var(--accent);\n',
    '    margin-bottom: 8px;\n',
    '}\n',
    '.hero__subtitle {\n',
    '    font-size: clamp(14px, 1.2vw, 16px);\n',
    '    line-height: 1.6;\n',
    '    font-weight: 400;\n',
    '    color: var(--on-surface-variant);\n',
    '    max-width: 420px;\n',
    '    margin-bottom: 24px;\n',
    '}\n',
    '.hero__actions {\n',
    '    display: flex;\n',
    '    flex-direction: column;\n',
    '    gap: 12px;\n',
    '    margin-top: auto;\n',
    '}\n',
    '@media (min-width: 480px) {\n',
    '    .hero__actions {\n',
    '        flex-direction: row;\n',
    '        gap: 16px;\n',
    '    }\n',
    '}\n',
    '.hero__deco {\n',
    '    position: absolute;\n',
    '    inset: 0;\n',
    '    background: var(--brand-gradient);\n',
    '    background-size: 200% 200%;\n',
    '    animation: gradientShift 8s ease infinite;\n',
    '    opacity: 0.08;\n',
    '    pointer-events: none;\n',
    '}\n',
]

if start_idx is not None and end_idx is not None:
    lines = lines[:start_idx] + new_hero + lines[end_idx:]
    print(f'Replaced Hero CSS, now {len(lines)} lines')
else:
    print(f'Could not find Hero section: start={start_idx}, end={end_idx}')

with open(r'D:\code\coffieart\css\styles.css', 'w') as f:
    f.writelines(lines)
print(f'Done. File now has {len(lines)} lines')