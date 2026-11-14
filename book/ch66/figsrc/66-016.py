import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role='varie', lw=1.1):
    n = max(4, int(abs(a1 - a0) / 2)); pts = [P(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw); arrow(ax, pts[-4], pts[-1], role, lw=lw)
fig, ax = canvas(76)
cx, cy, r = 42, 40, 24
disc(ax, cx, cy, r, 'fixe', fill=False)
for k in range(5):
    p = P(cx, cy, r, 72 * k)
    disc(ax, p[0], p[1], 1.5, 'resultat' if k == 0 else 'sujet')
    arc(ax, cx, cy, r, 72 * k + 9, 72 * k + 63)
    q = P(cx, cy, 15.5, 72 * k)
    text(ax, q[0], q[1], '%d°' % (72 * (k if k else 5)), 'varie', 's')
    q = P(cx, cy, r + 6.5, 72 * k)
    if k == 0: text(ax, q[0] + 1, q[1] + 3, r'$\zeta^5=1$', 'resultat', 's')
    else: text(ax, q[0], q[1], r'$\zeta^{%d}$' % k if k > 1 else r'$\zeta$', 'sujet')
text(ax, 44, 6, r'$5\times72°=360°$ : un tour', 'resultat', 'm')
save(fig, '66-016')
