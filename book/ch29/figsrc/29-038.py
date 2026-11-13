import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, R, a0, a1, role='sujet', lw=1.0, n=80):
    line(ax, [(cx + R * math.cos(a0 + (a1 - a0) * i / n), cy + R * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)], role, lw)

def rad(ax, cx, cy, R, a, role='fixe', lw=0.9, r0=0.0):
    line(ax, [(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))], role, lw)

def pol(cx, cy, R, a):
    return (cx + R * math.cos(a), cy + R * math.sin(a))

fig, ax = canvas(80)
text(ax, 44, 73, r'$\theta=s\,/\,r$', 'sujet', 'l')
steps = [('varie', r'mesurer l’arc : $s=6$ cm'), ('fixe', r'mesurer le rayon : $r=3$ cm'),
         ('sujet', r'diviser : $6\ \div\ 3$'), ('resultat', r'$\theta=2$ radians')]
for i, (role, lab) in enumerate(steps):
    y = 52 - 16 * i
    box(ax, 10, y, 68, 9, role, label=lab)
    if i < 3: arrow(ax, (44, y), (44, y - 7), 'encre')
save(fig, '29-038')
