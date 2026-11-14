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

fig, ax = canvas(66)
y1, y2 = 42, 18
box(ax, 2, y1 - 5, 22, 10, 'sujet', label=r'$(4+8)$'); text(ax, 30, y1, r'$+\ 8$')
arrow(ax, (36, y1), (44, y1), 'fixe'); box(ax, 46, y1 - 5, 20, 10, 'fixe', label=r'$0+8$')
arrow(ax, (67, y1), (73, y1), 'fixe'); box(ax, 74, y1 - 5, 12, 10, 'resultat', label='8')
text(ax, 5, y2, r'$4+$'); box(ax, 10, y2 - 5, 22, 10, 'sujet', label=r'$(8+8)$')
arrow(ax, (34, y2), (44, y2), 'fixe'); box(ax, 46, y2 - 5, 20, 10, 'fixe', label=r'$4+4$')
arrow(ax, (67, y2), (73, y2), 'fixe'); box(ax, 74, y2 - 5, 12, 10, 'resultat', label='8')
text(ax, 3, 30, 'on regroupe autrement', 'fixe', 's', ha='left')
text(ax, 80, 30, '=', 'resultat', 'l')
text(ax, 44, 5, r'tout reste dans $\{0,4,8\}$', 'sujet', 's')
box(ax, 2, 54, 84, 10, 'resultat', label=r'associativité : vraie dans tout $G$', size='s')
text(ax, 44, 48.5, r'donc dans $H$ : rien à contrôler', 'resultat', 's')
save(fig, '46-029')
