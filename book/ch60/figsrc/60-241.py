import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(70)
text(ax, 24, 65, 'diviseurs élémentaires', 'fixe', 's')
text(ax, 59, 65, 'facteur invariant', 'resultat', 's')
for x, v in ((3, '4'), (19, '27'), (35, '5')):
    box(ax, x, 52, 10, 9, 'sujet', label=v)
text(ax, 16, 56.5, r'$\times$'); text(ax, 32, 56.5, r'$\times$')
arrow(ax, (46, 56.5), (51.5, 56.5), 'varie')
box(ax, 52, 52, 14, 9, 'resultat', label='540')
cx, cy, R = 44, 22, 14
disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.6)
for k in range(12):
    a = math.radians(90 - 30 * k)
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 1.3, 'varie' if k == 1 else 'sujet')
for k, s in ((0, '0'), (1, '1'), (11, '539')):
    a = math.radians(90 - 30 * k)
    text(ax, cx + 18.5 * math.cos(a), cy + 18 * math.sin(a), s, 'varie' if k == 1 else 'sujet', 's')
text(ax, cx, cy, r'$\mathbb{Z}/540$', 'sujet', 'l')
text(ax, cx, 3, '1 engendre : ordre 540', 'varie', 's')
save(fig, '60-241')
