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

fig, ax = canvas(72)
P = {'0': (44, 26, 6, 'fixe', r'$0$'), 'b': (22, 38, 10, 'sujet', r'$b$ ($B$)'), 'c': (22, 50, 10, 'sujet', r'$c$ ($K$)'),
     'a': (66, 44, 10, 'autre', r'$a$ ($C$)'), '1': (44, 62, 6, 'fixe', r'$1$')}
S = lambda k: (P[k][2], 4); Cn = lambda k: (P[k][0], P[k][1])
for u, v in [('0', 'b'), ('b', 'c'), ('c', '1'), ('0', 'a'), ('a', '1')]:
    redge(ax, Cn(u), S(u), Cn(v), S(v))
for k, v in P.items(): nbox(ax, (v[0], v[1]), v[2], 4, v[3], v[4], 's')
text(ax, 44, 12, r'$b\wedge a=c\wedge a=0$', 'resultat', 's')
text(ax, 44, 5, r'$b\vee a=c\vee a=1$', 'resultat', 's')
text(ax, 76, 62, r'$b\neq c$', 'limite', 'l')
save(fig, '79-165')
