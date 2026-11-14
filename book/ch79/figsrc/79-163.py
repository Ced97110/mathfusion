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

fig, ax = canvas(92)
cw, ch = 12, 9
xs = [24, 36]; ys = [64, 54]
text(ax, 36, 86, r'$C$', 'autre', 'm'); text(ax, 9, 63.5, r'$B$', 'sujet', 'm')
for x, s in zip(xs, ['e', 't']): text(ax, x + cw/2, 78, '$%s$' % s, 'autre', 'm')
for y, s in zip(ys, ['e', 's']): text(ax, 19, y + ch/2, '$%s$' % s, 'sujet', 'm')
for (iy, ix), s in {(0, 0): 'e', (0, 1): 't', (1, 0): 's', (1, 1): 'st'}.items():
    box(ax, xs[ix], ys[iy], cw, ch, 'sujet', label='$%s$' % s)
box(ax, 54, 55, 32, 11, 'limite', label=r'$ts\notin BC$')
for i in range(8):
    disc(ax, 10 + i*9.5, 32, 3.4, 'sujet' if i < 4 else 'fixe')
brace(ax, 6, 42, 28, 'sujet', 'produits : 4')
brace(ax, 46, 82, 28, 'fixe', 'en plus : 4')
brace(ax, 6, 82, 38, 'resultat', 'sup : 8 éléments', down=False)
save(fig, '79-163')
