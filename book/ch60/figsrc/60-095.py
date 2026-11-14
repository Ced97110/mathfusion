import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cx, cy, R = 20, 36, 9
for k in range(6):
    a = math.radians(90 - 60 * k)
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 2.0, 'sujet')
text(ax, 20, 56, r'tor $M=\mathbb{Z}/6$', 'sujet', 'm')
text(ax, 20, 14, '6 éléments', 'sujet', 's')
text(ax, 40, 36, '⊕', 'encre', 'l')
for y in (46, 26):
    arrow(ax, (47, y), (83, y), 'autre', both=True)
    for k in range(6):
        disc(ax, 52 + 5 * k, y, 1.5, 'autre')
    text(ax, 45, y + 5, r'$\mathbb{Z}$', 'autre', 'l')
text(ax, 65, 56, 'partie libre', 'autre', 'm')
text(ax, 65, 14, 'rang 2 : 2 copies', 'autre', 's')
save(fig, '60-095')
