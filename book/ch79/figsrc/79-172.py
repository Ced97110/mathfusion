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

fig, ax = canvas(68)
data = [(14, '1', '2', 'sujet'), (44, '3', '6', 'fixe'), (74, '15', '30', 'autre')]
for cx, lo, hi, role in data:
    box(ax, cx - 7, 14, 14, 34, role)
    text(ax, cx, 44, hi, role, 'l'); text(ax, cx, 18, lo, role, 'l')
for x in (29, 59):
    for y in (44, 18): arrow(ax, (x - 6.5, y), (x + 6.5, y), 'varie')
arrow(ax, (14, 50), (74, 50), 'resultat', lw=1.3, curve=-0.22)
arrow(ax, (14, 12), (74, 12), 'resultat', lw=1.3, curve=0.22)
text(ax, 44, 62, 'composé : isomorphisme', 'resultat', 's')
save(fig, '79-172')
