import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def redge(ax, c1, s1, c2, s2, role="fixe", lw=1.0, dash=False):
    dx, dy = c2[0]-c1[0], c2[1]-c1[1]
    def t(s):
        return min(s[0]/abs(dx) if dx else 1e9, s[1]/abs(dy) if dy else 1e9)
    t1, t2 = t(s1), t(s2)
    line(ax, [(c1[0]+dx*t1, c1[1]+dy*t1), (c2[0]-dx*t2, c2[1]-dy*t2)], role, lw, dash)

def nbox(ax, c, hw, hh, role, label, size="m"):
    box(ax, c[0]-hw, c[1]-hh, 2*hw, 2*hh, role, label=label, size=size)

def cedge(ax, p, q, r, role="fixe", lw=1.0, dash=False):
    d = math.hypot(q[0]-p[0], q[1]-p[1]); ux, uy = (q[0]-p[0])/d, (q[1]-p[1])/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw, dash)

fig, ax = canvas(70)
Lv = [4, 12, 20, 60]; Rv = [2, 6, 10, 30]
for i in range(4):
    y = 4 + i * 13
    box(ax, 8, y, 18, 8, 'sujet', label=str(Lv[i])); box(ax, 62, y, 18, 8, 'autre', label=str(Rv[i]))
    arrow(ax, (27, y + 4), (61, y + 4), 'varie')
    if i < 3:
        line(ax, [(17, y + 8), (17, y + 13)], 'sujet', lw=1.2); line(ax, [(71, y + 8), (71, y + 13)], 'autre', lw=1.2)
text(ax, 44, 57, 'PGCD avec 30', 'varie', 's')
text(ax, 17, 64, r'$I[4,60]$', 'sujet', 'm'); text(ax, 71, 64, r'$I[2,30]$', 'autre', 'm')
save(fig, '79-168')
