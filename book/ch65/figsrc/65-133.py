import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
x0, y0, s = 10, 30, 28
V = {1: (x0, y0), 2: (x0 + s, y0), 3: (x0 + s, y0 + s), 4: (x0, y0 + s)}
poly(ax, [V[1], V[2], V[3], V[4]], 'sujet')
line(ax, [(x0 - 5, y0 + s + 5), (x0 + s + 5, y0 - 5)], 'varie', lw=1.0, dash=True)
text(ax, x0 + s + 4, y0 - 13, 'axe par 2 et 4', 'varie', 's', ha='center')
for k, (x, y) in V.items():
    off = (-4, -4) if k == 1 else (4, -4) if k == 2 else (4, 4) if k == 3 else (-4, 4)
    text(ax, x + off[0], y + off[1], str(k), 'sujet', 'm')
arrow(ax, (x0 + 8, y0 + 14), (x0 + 12, y0 + 20), 'varie', curve=-0.9)
text(ax, x0 + s / 2, y0 + s + 9, 'quart de tour', 'varie', 's')
# 8 symétries sur 24 permutations
text(ax, 66, 66, '24 permutations', 'fixe', 's')
for i in range(24):
    c, r = i % 4, i // 4
    role = 'sujet' if i < 8 else 'fixe'
    box(ax, 50 + c * 8.5, 56 - r * 8.5, 7, 7, role, r=0.5)
text(ax, 66, 4, r'8 forment $D$', 'sujet', 's')
text(ax, 66, 10, '16 restent hors de $D$', 'fixe', 's')
save(fig, '65-133')
