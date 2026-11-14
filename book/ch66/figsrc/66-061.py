import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, R = 24, 29, 14
box(ax, 1, 3, 46, 56, 'sujet', fill=True)
text(ax, 24, 54, r'$\mathbb{Q}(i)$', 'sujet', 'l')
disc(ax, cx, cy, R, 'fixe', fill=False)
line(ax, [(cx - R - 2, cy), (cx + R + 2, cy)], 'fixe', lw=0.5)
line(ax, [(cx, cy - R - 2), (cx, cy + R + 2)], 'fixe', lw=0.5)
pts = [(cx + R, cy, r'$1$', (cx + R + 4.5, cy)), (cx, cy + R, r'$i$', (cx, cy + R + 3)),
       (cx - R, cy, r'$-1$', (cx - R - 4.5, cy)), (cx, cy - R, r'$-i$', (cx, cy - R - 3))]
for x, y, s, p in pts:
    disc(ax, x, y, 1.6, 'resultat')
    text(ax, p[0], p[1], s, 'resultat', 's')
text(ax, 69, 54, r'les 4 racines de $x^4-1$', 'encre', 's')
rows = [r'$1\in\mathbb{Q}(i)$', r'$i\in\mathbb{Q}(i)$', r'$i^2=-1\in\mathbb{Q}(i)$', r'$-i\in\mathbb{Q}(i)$']
for k, s in enumerate(rows):
    box(ax, 52, 40 - k * 11, 34, 8, 'resultat', label=s, size='s')
save(fig, '66-061')
