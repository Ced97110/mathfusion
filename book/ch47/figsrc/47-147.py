import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx, cy, R = 24, 32, 19
pos = {h: (cx + R * math.cos(math.radians(90 - 30 * h)), cy + R * math.sin(math.radians(90 - 30 * h))) for h in range(12)}
sel = [1, 4, 7, 10]
line(ax, [pos[h] for h in sel] + [pos[1]], 'sujet', dash=True)
for h in range(12):
    if h in sel: disc(ax, *pos[h], 3.4, 'sujet', label=str(h), size='s')
    else: disc(ax, *pos[h], 3.0, 'fixe')
text(ax, cx, cy, 'G : 12 heures', 'fixe', 's')
box(ax, 52, 36, 34, 18, 'sujet'); text(ax, 69, 49, 'un élément de G/N', 'sujet', 's'); text(ax, 69, 41.5, '{1, 4, 7, 10}', 'sujet', 'm')
arrow(ax, (52, 45), (38.5, 47.5), 'sujet')
text(ax, 69, 28, 'un ensemble', 'sujet', 's'); text(ax, 69, 23.5, 'de quatre heures', 'sujet', 's')
box(ax, 52, 6, 34, 10, 'fixe'); text(ax, 69, 11, 'une heure de G', 'fixe', 's')
arrow(ax, (52, 12), (46.8, 30), 'fixe')
save(fig, '47-147')
