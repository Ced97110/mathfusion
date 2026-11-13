import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, R = 28, 33, 22
def P(a, r=R): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def base():
    ax.add_patch(Circle((cx, cy), R, fc='none', ec=COL['fixe'], lw=0.8, zorder=1))
    arrow(ax, (cx - R - 3, cy), (cx + R + 3, cy), 'fixe', lw=0.6)
    arrow(ax, (cx, cy - R - 3), (cx, cy + R + 3), 'fixe', lw=0.6)
def dot(a, role, lab, off=3.6):
    x, y = P(a); disc(ax, x, y, 1.1, role, fill=True)
    text(ax, *P(a, R + off), lab, role, 'm')
def ray(a, role, dash=False, r=R): line(ax, [(cx, cy), P(a, r)], role, lw=1.0, dash=dash)
def arc(a0, a1, r, role, lw=1.0):
    n = 40; line(ax, [P(a0 + (a1 - a0) * i / n, r) for i in range(n + 1)], role, lw=lw)
def seg(p, q, role, lw=1.0, dash=False): line(ax, [p, q], role, lw=lw, dash=dash)
def panel(rows, y0=47):
    for i, (s, role) in enumerate(rows): text(ax, 57, y0 - i * 7.5, s, role, 's', ha='left')
def mirror(vertical):
    if vertical: seg((cx, cy - R - 3), (cx, cy + R + 3), 'varie', 1.8)
    else: seg((cx - R - 3, cy), (cx + R + 3, cy), 'varie', 1.8)
base()
arc(0, 150, 15, 'resultat'); arc(0, 30, 9, 'sujet'); arc(150, 180, 9, 'varie')
ray(30, 'sujet'); ray(150, 'resultat')
dot(30, 'sujet', r'$P$'); dot(150, 'resultat', r'$Q$')
text(ax, *P(14, 12.5), r'$\theta$', 'sujet', 's'); text(ax, *P(166, 12.5), r'$\theta$', 'varie', 's')
text(ax, cx, cy + 10, '150°', 'resultat', 's')
panel([('P à l\'angle $\\theta$ = 30°', 'sujet'), ('Q à 180° − $\\theta$', 'resultat'), ('180° − 30° = 150°', 'resultat'), ('même $\\theta$ de l\'autre côté', 'varie')])
save(fig, '28-085')
