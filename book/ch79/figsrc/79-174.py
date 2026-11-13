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

fig, ax = canvas(80)
Y = [8, 22, 36, 50, 64]
for x, vals, role in [(16, ['1', '2', '4', '12', '60'], 'sujet'), (64, ['1', '2', '4', '8', '16'], 'varie')]:
    for i in range(4): cedge(ax, (x, Y[i]), (x, Y[i + 1]), 4.6, role, 1.4)
    for y, s in zip(Y, vals): disc(ax, x, y, 4.6, role, label=s, size='s')
arrow(ax, (64, Y[4] + 5), (64, 76), 'limite', lw=1.4)
text(ax, 16, 74, 'diviseurs de 60', 'sujet', 's'); text(ax, 62, 78.5, 'entiers positifs', 'varie', 's')
text(ax, 38, 36, 'au plus 5', 'sujet', 's'); text(ax, 38, 31, 'éléments', 'sujet', 's')
text(ax, 77, 70, 'sans fin', 'limite', 's')
save(fig, '79-174')
