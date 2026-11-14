import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def hpos(cx, cy, R, k):
    th = math.radians(30 * k)
    return (cx + R * math.sin(th), cy + R * math.cos(th))

def clock(ax, cx, cy, R, spec, big=3.2, small=1.4):
    ax.add_patch(Circle((cx, cy), R, fill=False, ec=COL['fixe'], lw=0.5, zorder=1))
    for k in range(12):
        x, y = hpos(cx, cy, R, k)
        if k in spec:
            s = spec[k]; fill = s[2] if len(s) > 2 else True
            disc(ax, x, y, big, s[0], fill=fill, label=s[1], size='s')
        else:
            disc(ax, x, y, small, 'fixe')

def ar(ax, p, q, rr, role='sujet', curve=0.0):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    arrow(ax, (p[0] + u[0] * rr, p[1] + u[1] * rr), (q[0] - u[0] * rr, q[1] - u[1] * rr), role, curve=curve)

fig, ax = canvas(58)
text(ax, 51, 52, r'$\{0,4,8\}$', 'sujet', 'm'); text(ax, 75, 52, r'$\{0,1,11\}$', 'autre', 'm')
rows = ['contient le neutre 0', 'stable par addition', 'contient les inverses']
cells = [[('oui', 'resultat'), ('oui', 'resultat')],
         [('oui', 'resultat'), (r'non : $1+1=2$', 'limite')],
         [('oui', 'resultat'), ('oui', 'resultat')]]
for i, lab in enumerate(rows):
    y = 35 + 0 - 13 * i
    box(ax, 2, y - 5, 37, 10, 'fixe', label=lab, size='s')
    for j, (t, role) in enumerate(cells[i]):
        box(ax, 40 + 24 * j + 0, y - 5, 22, 10, role, label=t, size='s')
    y -= 0
save(fig, '46-025')
