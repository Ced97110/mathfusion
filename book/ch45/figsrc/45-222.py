import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 20, 74, 'écriture complète', 'fixe', 's')
for i in range(4):
    text(ax, 20, 62 - i * 11, rf'${i}\mapsto{(i + 1) % 4}$', 'fixe', 'm')
text(ax, 64, 74, 'écriture abrégée', 'sujet', 's')
cx, cy, R = 64, 40, 15
pos = [(cx + R * math.sin(math.radians(90 * i)), cy + R * math.cos(math.radians(90 * i))) for i in range(4)]
for i, (x, y) in enumerate(pos):
    disc(ax, x, y, 4, 'sujet', label=str(i))
for i in range(4):
    (x1, y1), (x2, y2) = pos[i], pos[(i + 1) % 4]
    d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
    arrow(ax, (x1 + 4.6 * ux, y1 + 4.6 * uy), (x2 - 4.6 * ux, y2 - 4.6 * uy), 'resultat' if i == 3 else 'varie', curve=-0.25)
text(ax, 64, 14, r'$(0\ 1\ 2\ 3)$', 'sujet', 'xl')
text(ax, 64, 6, 'le dernier revient au premier', 'resultat', 's')
save(fig, '45-222')
