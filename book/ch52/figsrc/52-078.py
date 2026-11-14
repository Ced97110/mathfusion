import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cx, cy, R = 25, 38, 17
disc(ax, cx, cy, R, 'fixe', fill=False)
for i in range(5):
    a = math.radians(90 - 72 * i)
    role = 'resultat' if i == 2 else 'sujet'
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 3.2, role, label=str(i), size='m')
text(ax, cx, cy + 3, r'$\mathbb{Z}/5\mathbb{Z}$', 'sujet', 'm')
text(ax, cx, cy - 4, '5 restes', 'sujet', 's')
box(ax, 53, 40, 33, 18, 'fixe', label=None)
text(ax, 69.5, 52, r'3 + 4 = 7', 'encre', 'm'); text(ax, 69.5, 45, 'reste 2', 'resultat', 'm')
box(ax, 53, 12, 33, 18, 'fixe', label=None)
text(ax, 69.5, 24, r'3 $\times$ 4 = 12', 'encre', 'm'); text(ax, 69.5, 17, 'reste 2', 'resultat', 'm')
a2 = math.radians(90 - 144)
arrow(ax, (52.5, 49), (cx + R * math.cos(a2) + 4, cy + R * math.sin(a2) + 3), 'varie', curve=-0.2)
arrow(ax, (52.5, 21), (cx + R * math.cos(a2) + 4, cy + R * math.sin(a2) - 1), 'varie', curve=0.2)
text(ax, cx, 8, 'on garde le reste par 5', 'varie', 's')
save(fig, '52-078')
