import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role='varie', lw=1.1):
    n = max(4, int(abs(a1 - a0) / 2)); pts = [P(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw); arrow(ax, pts[-4], pts[-1], role, lw=lw)
fig, ax = canvas(68)
cx, cy, r = 54, 34, 19
disc(ax, cx, cy, r, 'fixe', fill=False)
for k in range(6):
    p = P(cx, cy, r, 60 * k)
    role = {2: 'sujet', 4: 'autre'}.get(k, 'fixe')
    disc(ax, p[0], p[1], 2.0 if k in (2, 4) else 1.2, role)
text(ax, cx + r + 4, cy - 3.5, '1', 'fixe')
arc(ax, cx, cy, r + 5, 3, 58); arc(ax, cx, cy, r + 5, 63, 118)
q = P(cx, cy, r + 10, 30); text(ax, q[0], q[1], '1', 'varie', 's')
q = P(cx, cy, r + 10, 90); text(ax, q[0], q[1], '2', 'varie', 's')
text(ax, 38, 56, r'$\zeta_6^2$ : 2 pas, 120°', 'sujet', 's', ha='right')
text(ax, 38, 12, r'$\zeta_6^4$ : 4 pas, 240°', 'autre', 's', ha='right')
text(ax, 18, 34, '1 pas =\n60°', 'varie', 's')
save(fig, '66-023')
