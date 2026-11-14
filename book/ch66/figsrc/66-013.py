import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role='varie', lw=1.1):
    n = max(4, int(abs(a1 - a0) / 2)); pts = [P(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw); arrow(ax, pts[-4], pts[-1], role, lw=lw)
fig, ax = canvas(66)
cx, cy, r = 27, 33, 21
disc(ax, cx, cy, r, 'fixe', fill=False)
for k in range(5):
    p = P(cx, cy, r, 72 * k)
    disc(ax, p[0], p[1], 2.0 if k == 1 else 1.3, 'sujet' if k == 1 else 'fixe')
text(ax, cx + r + 4, cy - 3.5, '1', 'fixe')
z = P(cx, cy, r, 72); text(ax, z[0] - 3.5, z[1] + 3, r'$\zeta$', 'sujet')
arc(ax, cx, cy, r + 5, 4, 62)
q = P(cx, cy, r + 10.5, 36); text(ax, q[0] + 2, q[1] + 1, r'72° = $2\pi/5$', 'varie', 's')
text(ax, 27, 5, 'sens inverse des aiguilles', 'varie', 's')
text(ax, 70, 38, r'$\zeta$', 'sujet', 'xl', weight='bold')
text(ax, 70, 29, '« dzêta »', 'sujet', 's')
text(ax, 70, 19, 'premier sommet\naprès 1', 'fixe', 's')
save(fig, '66-013')
