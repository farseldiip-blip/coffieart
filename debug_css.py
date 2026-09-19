# Debug CSS file state
with open(r'D:\code\coffieart\css\styles.css', 'rb') as f:
    content = f.read()

print(f"Current file size: {len(content)} bytes")
print(f"First 300 bytes: {content[:300]!r}")
print(f"Last 300 bytes: {content[-300:]!r}")

# Check for key sections
checks = ['box-sizing', 'overflow-x', '@keyframes', '.hero {', '.hairline', '.brand-gradient-text', '.btn-primary', '.section-label', '.display-xl', '.container']
for c in checks:
    found = c.encode() in content
    print(f"  Contains '{c}': {found}")