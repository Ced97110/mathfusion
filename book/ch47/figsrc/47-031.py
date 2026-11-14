import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pt(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def sq(ax, cx, cy, s, role='fixe'):
    poly(ax, [(cx-s, cy-s), (cx+s, cy-s), (cx+s, cy+s), (cx-s, cy+s)], role)
def grid(ax, x0, y0, cw, ch, gap, rows, cols, roles):
    cells = []
    for i in range(rows):
        for j in range(cols):
            x = x0 + j*(cw+gap); y = y0 + (rows-1-i)*(ch+gap)
            box(ax, x, y, cw, ch, roles[i], r=0.6)
            cells.append((x, y))
    return cells

fig, ax = canvas(60)
disc(ax, 14, 36, 3.5, 'sujet', label=r'$P$', size='s'); disc(ax, 74, 36, 3.5, 'sujet', label=r'$Q$', size='s')
arrow(ax, (18, 38), (70, 38), 'varie')
text(ax, 44, 42.5, r'$r$ : un quart de tour', 'varie', 's')
arrow(ax, (70, 34), (18, 34), 'resultat')
text(ax, 44, 29.5, r'$r^{-1}$ : trois quarts de tour', 'resultat', 's')
text(ax, 44, 52, r'$Q = r(P)$', 'varie', 'm')
text(ax, 44, 19, "l'inverse défait le quart de tour", 'resultat', 's')
box(ax, 20, 4.5, 48, 9, 'resultat', label=r'$r^{-1}$ est dans $G$ : $Q$ lié à $P$', size='s')
save(fig, '47-031')
