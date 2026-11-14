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

fig, ax = canvas(70)
cx, cy, s = 44, 34, 20
sq(ax, cx, cy, s)
R = 0.9*s
p = pt(cx, cy, R, 55); q = pt(cx, cy, R, 145)
disc(ax, *p, 2.2, 'sujet'); disc(ax, *q, 2.2, 'sujet')
text(ax, p[0]+4, p[1]+3, r'$P$', 'sujet', 's'); text(ax, q[0]-4, q[1]+3, r'$Q$', 'sujet', 's')
arrow(ax, (p[0]-3.5, p[1]+1.5), (q[0]+3.5, q[1]+1.5), 'resultat', curve=-0.3)
text(ax, 44, 60, r'$r$ est dans $\{1, r\}$', 'resultat', 's')
arrow(ax, (q[0]+2.5, q[1]-3), (p[0]-2.5, p[1]-3), 'limite', curve=0.5)
text(ax, 44, 22, 'retour : trois quarts de tour', 'limite', 's')
text(ax, 44, 17.5, "absent de l'ensemble", 'limite', 's')
text(ax, 44, 5, r'$\{1, r\}$ : pas un groupe', 'encre', 's')
save(fig, '47-029')
