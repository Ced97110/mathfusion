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
for i in range(4): cedge(ax, (14, Y[i]), (14, Y[i + 1]), 4.6, 'sujet', 1.4)
for y, s in zip(Y, ['1', '2', '4', '12', '60']): disc(ax, 14, y, 4.6, 'sujet', label=s, size='s')
for i in range(4): text(ax, 27, (Y[i] + Y[i + 1]) / 2, 'rien', 'resultat', 's')
cedge(ax, (58, Y[0]), (58, Y[2]), 4.6, 'fixe', 1.4); cedge(ax, (58, Y[2]), (58, Y[4]), 4.6, 'fixe', 1.4)
for y, s in [(Y[0], '1'), (Y[2], '4'), (Y[4], '60')]: disc(ax, 58, y, 4.6, 'fixe', label=s, size='s')
disc(ax, 79, Y[1], 4.2, 'varie', label='2', size='s')
arrow(ax, (74.5, Y[1]), (59.5, Y[1]), 'varie', lw=1.2)
text(ax, 70, 38, 'on peut', 'varie', 's'); text(ax, 70, 33, 'insérer 2', 'varie', 's')
save(fig, '79-176')
