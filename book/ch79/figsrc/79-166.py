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

fig, ax = canvas(96)
L = [r'$a$', r'$a\wedge(a\vee c)$', r'$a\wedge(b\vee c)$', r'$b\vee(a\wedge c)$', r'$b\vee(b\wedge c)$', r'$b$']
R = [r'$6$', r'$6\wedge30=6$', r'$6\wedge10=2$', r'$2\vee1=2$', r'$2\vee1=2$', r'$2$']
yb = [4 + (5 - i) * 13 for i in range(6)]
for i in range(6):
    box(ax, 3, yb[i], 42, 8, 'varie' if i in (2, 3) else 'fixe', label=L[i], size='s')
    box(ax, 56, yb[i], 29, 8, 'sujet' if i < 2 else 'varie', label=R[i], size='s')
for i in range(5):
    y0, y1 = yb[i], yb[i + 1] + 8
    arrow(ax, (24, y0), (24, y1), 'varie' if i == 2 else ('limite' if i == 1 else 'fixe'), lw=1.1)
    arrow(ax, (70, y0), (70, y1), 'limite' if i == 1 else 'fixe', lw=1.1)
text(ax, 36, (yb[2] + yb[3] + 8) / 2, 'loi $M$', 'varie', 's')
text(ax, 44, 87, '$a=6,\\ b=2,\\ c=5$\nétape 2 : $a\\vee c = b\\vee c$ ?\nnon : $30 \\neq 10$', 'limite', 's')
save(fig, '79-166')
