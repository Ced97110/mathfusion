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

fig, ax = canvas(60)
data = [(14, '1', '2', r'$I[1,2]$', 'sujet'), (44, '3', '6', r'$I[3,6]$', 'fixe'), (74, '15', '30', r'$I[15,30]$', 'autre')]
for cx, lo, hi, nm, role in data:
    box(ax, cx - 8, 12, 16, 34, role)
    text(ax, cx, 42, hi, role, 'l'); text(ax, cx, 16, lo, role, 'l')
    line(ax, [(cx, 21), (cx, 37)], role, lw=1.0); text(ax, cx, 52, nm, role, 'm')
for x, s in [(30, '1re'), (60, '2e')]:
    arrow(ax, (x - 5.5, 29), (x + 5.5, 29), 'varie'); text(ax, x, 33, s, 'varie', 's')
brace(ax, 6, 82, 10, 'varie', 'deux transpositions')
save(fig, '79-171')
