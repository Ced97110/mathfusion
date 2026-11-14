import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cx, cy, R = 28, 42, 21
cl = ['sujet', 'varie', 'resultat']
for h in range(12):
    x, y = cx + R * math.sin(math.pi * h / 6), cy + R * math.cos(math.pi * h / 6)
    disc(ax, x, y, 3.4, cl[h % 3], label=str(h), size='s')
text(ax, cx, 8, r'$\mathbb{Z}/12\mathbb{Z}$', 'encre', 'm')
arrow(ax, (54, 42), (64, 42), 'fixe')
for k in range(3):
    disc(ax, 76, 62 - k * 20, 5.5, cl[k])
text(ax, 76, 8, r'$\mathbb{Z}/3\mathbb{Z}$', 'encre', 'm')
text(ax, 76, 12, '', 'encre', 's') if False else None
save(fig, '48-174')
