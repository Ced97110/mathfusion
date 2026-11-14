import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
# pentagone régulier et cos 72°
cx, cy, R = 24, 42, 21
pts = [(cx + R * math.cos(math.radians(72 * k)), cy + R * math.sin(math.radians(72 * k))) for k in range(5)]
poly(ax, pts, 'sujet')
for p in pts: line(ax, [(cx, cy), p], 'fixe', lw=0.5)
wx, wy = pts[1]
line(ax, [(wx, wy), (wx, cy)], 'varie', dash=True)
line(ax, [(cx, cy - 1.5), (wx, cy - 1.5)], 'resultat', lw=1.8)
text(ax, (cx + wx) / 2, cy - 5, r'$\cos 72°$', 'resultat', 's')
text(ax, cx + 6, cy + 4.5, '72°', 'fixe', 's')
text(ax, cx, 70, 'pentagone régulier', 'sujet', 'm')
text(ax, cx, 8, 'constructible', 'resultat', 'm')
# chaîne de corps, deux étages de degré 2
bx, bw = 56, 28
box(ax, bx, 6, bw, 11, 'autre', label=r'$\mathbb{Q}$')
box(ax, bx, 32, bw, 16, 'resultat')
text(ax, bx + bw / 2, 42, r'$\mathbb{Q}(\sqrt{5})$', 'resultat', 'm')
text(ax, bx + bw / 2, 36, 'contient cos 72°', 'resultat', 's')
box(ax, bx, 62, bw, 11, 'autre', label=r'$\mathbb{Q}(\omega)$')
arrow(ax, (bx + bw / 2, 18), (bx + bw / 2, 31), 'varie')
arrow(ax, (bx + bw / 2, 49), (bx + bw / 2, 61), 'varie')
text(ax, bx + bw / 2 + 2, 24.5, 'degré 2', 'varie', 's', ha='left')
text(ax, bx + bw / 2 + 2, 55, 'degré 2', 'varie', 's', ha='left')
save(fig, '63-173')
