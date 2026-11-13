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

fig, ax = canvas(62)
text(ax, 44, 57, "avec l'identité 1", 'resultat', 'm')
disc(ax, 14, 45, 3.5, 'resultat', label=r'$P$', size='s'); disc(ax, 74, 45, 3.5, 'resultat', label=r'$P$', size='s')
arrow(ax, (18, 45), (70, 45), 'resultat')
text(ax, 44, 49, r'$1$ : ne rien faire', 'resultat', 's')
text(ax, 44, 40, r'$1$ est dans $G$', 'resultat', 's')
line(ax, [(4, 33), (84, 33)], 'fixe', dash=True)
text(ax, 44, 27, 'sans identité, avec seulement r', 'limite', 'm')
disc(ax, 14, 15, 3.5, 'limite', label=r'$P$', size='s'); disc(ax, 74, 15, 3.5, 'limite', label=r'$Q$', size='s')
arrow(ax, (18, 15), (70, 15), 'limite')
text(ax, 44, 19, r'$r$ : un quart de tour', 'limite', 's')
text(ax, 44, 8, r'$Q \neq P$ : $P$ ne revient pas sur $P$', 'limite', 's')
save(fig, '47-030')
