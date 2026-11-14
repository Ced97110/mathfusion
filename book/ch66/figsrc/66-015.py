import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role='varie', lw=1.1):
    n = max(4, int(abs(a1 - a0) / 2)); pts = [P(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw); arrow(ax, pts[-4], pts[-1], role, lw=lw)
fig, ax = canvas(68)
cx, cy, r = 28, 34, 20
disc(ax, cx, cy, r, 'fixe', fill=False)
for k in range(5):
    p = P(cx, cy, r, 72 * k)
    role = 'sujet' if k in (1, 2) else 'fixe'
    disc(ax, p[0], p[1], 1.6 if k in (1, 2) else 1.2, role)
for k in (1, 2):
    line(ax, [(cx, cy), P(cx, cy, r, 72 * k)], 'fixe')
text(ax, cx + 14, cy - 3, '1', 'fixe')
q = P(cx, cy, 13, 72); text(ax, q[0] - 1, q[1] + 2, r'$\zeta$', 'sujet')
q = P(cx, cy, 13, 144); text(ax, q[0] - 1, q[1] + 1, r'$\zeta^2$', 'sujet')
arc(ax, cx, cy, r + 5, 4, 69); arc(ax, cx, cy, r + 5, 76, 141)
q = P(cx, cy, r + 10, 36); text(ax, q[0] + 1, q[1] + 1, '72°', 'varie', 's')
q = P(cx, cy, r + 10, 108); text(ax, q[0] - 1, q[1] + 1, '+ 72°', 'varie', 's')
text(ax, 70, 44, '72° + 72° = 144°', 'resultat', 's')
text(ax, 70, 34, r'$\zeta\times\zeta=\zeta^2$', 'sujet', 'm')
text(ax, 70, 24, 'les angles\ns\'additionnent', 'fixe', 's')
save(fig, '66-015')
