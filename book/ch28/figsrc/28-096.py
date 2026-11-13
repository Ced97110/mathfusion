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
base(); mirror(False)
seg((cx + R, cy - R - 2), (cx + R, cy + R + 2), 'fixe', 0.8, True)
seg((cx + R, cy), (cx + R, cy + R), 'sujet', 1.8); seg((cx + R, cy), (cx + R, cy - R), 'resultat', 1.8)
ray(45, 'sujet', r=R * 1.4142); ray(-45, 'resultat', r=R * 1.4142)
dot(45, 'sujet', '', 3.2); dot(-45, 'resultat', '', 3.2); text(ax, P(45)[0] - 3.5, P(45)[1] + 3, r'$P$', 'sujet', 'm'); text(ax, P(-45)[0] - 3.5, P(-45)[1] - 3, r'$S$', 'resultat', 'm')
panel([('tan 45° = 1', 'sujet'), ('tan 315° = −1', 'resultat'), ('$x$ pareil, $y$ opposé', 'varie'), ('quotient opposé', 'encre')], 47)
save(fig, '28-096')
