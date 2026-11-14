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

fig, ax = canvas(88)
Y = [8, 22, 36, 50, 64]
blue = [(44, Y[0], '1'), (30, Y[1], '2'), (20, Y[2], '4'), (30, Y[3], '12'), (44, Y[4], '60')]
orng = [(44, Y[0], '1'), (58, Y[1], '5'), (68, Y[2], '15'), (58, Y[3], '30'), (44, Y[4], '60')]
for path, role in [(orng, 'varie'), (blue, 'sujet')]:
    for p, q in zip(path, path[1:]): cedge(ax, p[:2], q[:2], 4.6, role, 1.6)
    for x, y, s in path: disc(ax, x, y, 4.6, role, label=(None if (role == 'varie' and s in ('1', '60')) else s), size='s')
text(ax, 20, 77, r'$\times2,\ \times2,\ \times3,\ \times5$', 'sujet', 'm')
text(ax, 68, 77, r'$\times5,\ \times3,\ \times2,\ \times2$', 'varie', 'm')
text(ax, 44, 84, 'de bas en haut', 'fixe', 's')
save(fig, '79-173')
