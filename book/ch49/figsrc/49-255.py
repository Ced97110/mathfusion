import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle

def corners(cx, cy, h):
    return [(cx - h, cy + h), (cx + h, cy + h), (cx + h, cy - h), (cx - h, cy - h)]  # A B C D

def square(ax, cx, cy, h, roles, names=None, rd=3.0):
    P = corners(cx, cy, h)
    poly(ax, P, 'fixe', fill=False)
    for i, (p, ro) in enumerate(zip(P, roles)):
        disc(ax, p[0], p[1], rd, ro, label=(names[i] if names else None), size='s')
    return P

def arr(ax, p, q, rd=3.0, role='varie', curve=0.0, both=False, lw=1.0):
    dx, dy = q[0] - p[0], q[1] - p[1]; n = math.hypot(dx, dy); ux, uy = dx / n, dy / n
    s = (p[0] + ux * (rd + 0.7), p[1] + uy * (rd + 0.7)); e = (q[0] - ux * (rd + 0.7), q[1] - uy * (rd + 0.7))
    arrow(ax, s, e, role, lw=lw, curve=curve, both=both)

def rect(ax, x, y, w, h, role, fill=True, lw=0.6):
    ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role] if fill else 'none', lw=lw, zorder=2))

fig, ax = canvas(70)
text(ax, 44, 66, '$4^{c(g)}$ par ligne', 'encre', 's')
rows = [('neutre',256,1,'256'),(r'$r,\ r^3$',4,2,'4 + 4'),(r'$r^2$',16,1,'16'),('diagonales',64,2,'64 + 64'),('médianes',16,2,'16 + 16')]
sc = 0.14
for k, (lab, v, c, txt) in enumerate(rows):
    y = 55 - 8 * k
    text(ax, 2, y + 2.5, lab, 'encre', 's', ha='left')
    x = 24
    for j in range(c):
        rect(ax, x, y, max(v * sc, 0.6), 5, 'sujet' if j == 0 else 'autre'); x += max(v * sc, 0.6) + 0.8
    text(ax, x + 2, y + 2.5, txt, 'encre', 's', ha='left')
text(ax, 44, 17, 'total : 440', 'encre', 's')
text(ax, 44, 8, '$440\\div8=55$', 'resultat', 'l')
save(fig, '49-255')
