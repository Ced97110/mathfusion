import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def ring(cx, cy, n, sub, R=10):
    pts = [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]
    for k, (x, y) in enumerate(pts):
        disc(ax, x, y, 2.0, 'varie' if k in sub else 'sujet')
ring(16, 34, 5, [])
ring(44, 34, 6, [0, 2, 4])
ring(72, 34, 6, [0, 2, 4])
for x, t in [(16, r'$\mathbb{Z}/5$'), (44, r'$\mathbb{Z}/6$'), (72, r'$S_3$')]:
    text(ax, x, 53, t, 'sujet', 'l')
text(ax, 16, 16, 'simple', 'resultat', 'm', weight='bold')
text(ax, 44, 16, 'se découpe', 'fixe', 'm', weight='bold')
text(ax, 72, 16, 'se découpe', 'fixe', 'm', weight='bold')
text(ax, 16, 9, r'$\{e\}$ et $G$ seuls', 'encre', 's')
text(ax, 44, 9, r'normal : $\{0,2,4\}$', 'varie', 's')
text(ax, 72, 9, 'normal : 3 paires', 'varie', 's')
save(fig, '64-070')
