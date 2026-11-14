import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
# barres : 16, 8, 4, 2, 1 éléments, cases de 3,2 mm
cw, x0 = 3.2, 4
orders = [16, 8, 4, 2, 1]
ys = [74, 58, 42, 26, 10]
for n, y in zip(orders, ys):
    for i in range(n):
        box(ax, x0 + i * cw, y, cw, 8, 'sujet' if n > 1 else 'resultat', lw=0.6, r=0.2)
    text(ax, x0 + n * cw + 2.5, y + 4, str(n), 'sujet' if n > 1 else 'resultat', 'm', ha='left')
for y0, y1 in zip(ys[:-1], ys[1:]):
    arrow(ax, (x0 + 4, y0 - 0.5), (x0 + 4, y1 + 8.5), 'varie', lw=0.9)
    text(ax, x0 + 7, (y0 + y1 + 8) / 2, 'indice 2 : une racine carrée', 'varie', 's', ha='left')
# heptadécagone, à droite
cx, cy, R = 73, 50, 13
pts = [(cx + R * math.cos(math.radians(90 + 360 * k / 17)), cy + R * math.sin(math.radians(90 + 360 * k / 17))) for k in range(17)]
poly(ax, pts, 'autre')
text(ax, cx, cy + R + 6, '17 côtés', 'autre', 'm')
text(ax, cx, cy - R - 5, r'$G$ cyclique d\'ordre 16'.replace("\\'", "'"), 'sujet', 's')
text(ax, 44, 3, 'quatre racines carrées successives', 'resultat', 's')
save(fig, '63-185')
