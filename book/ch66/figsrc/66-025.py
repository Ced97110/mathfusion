import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role='varie', lw=1.1):
    n = max(4, int(abs(a1 - a0) / 2)); pts = [P(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw); arrow(ax, pts[-4], pts[-1], role, lw=lw)
fig, ax = canvas(72)
cx, cy, r = 38, 36, 21
disc(ax, cx, cy, r, 'fixe', fill=False)
for k in range(6):
    p = P(cx, cy, r, 60 * k)
    role = {1: 'sujet', 3: 'autre', 4: 'resultat'}.get(k, 'fixe')
    disc(ax, p[0], p[1], 2.0 if k in (1, 3, 4) else 1.2, role)
for k, role, lab in [(1, 'sujet', '60°'), (3, 'autre', '180°'), (4, 'resultat', '240°')]:
    q = P(cx, cy, 13.5, 60 * k); text(ax, q[0], q[1], lab, role, 's')
arc(ax, cx, cy, r + 5, 63, 236)
q = P(cx, cy, r + 10.5, 150); text(ax, q[0] + 1, q[1], '+ 180°', 'varie', 's')
text(ax, 75, 50, '60° + 180°', 'fixe', 's')
text(ax, 75, 43, '= 240°', 'resultat', 'm')
text(ax, 75, 28, 'toujours l\'un\ndes 6 sommets', 'fixe', 's')
save(fig, '66-025')
