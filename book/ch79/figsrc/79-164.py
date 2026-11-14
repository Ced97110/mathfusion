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
hw, hh = 6, 4
N = {'0': (44, 26), 'a': (14, 44), 'c': (44, 44), 'b': (74, 44), '1': (44, 62)}
for m in 'acb':
    redge(ax, N['0'], (hw, hh), N[m], (hw, hh)); redge(ax, N[m], (hw, hh), N['1'], (hw, hh))
rol = {'0': 'fixe', '1': 'fixe', 'a': 'sujet', 'b': 'sujet', 'c': 'varie'}
for k, c in N.items(): nbox(ax, c, hw, hh, rol[k], '$%s$' % k)
text(ax, 44, 12, r'$a\wedge c=b\wedge c=0$', 'resultat', 's')
text(ax, 44, 5, r'$a\vee c=b\vee c=1$', 'resultat', 's')
text(ax, 76, 62, r'$a\neq b$', 'limite', 'l')
save(fig, '79-164')
