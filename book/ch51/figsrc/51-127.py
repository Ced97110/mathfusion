import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cx, cy, R = 44, 42, 20
def P(r, k):
    a = math.radians(90 - k * 360 / 7); return (cx + r * math.cos(a), cy + r * math.sin(a))
def sh(p, q, d):
    L = math.hypot(q[0] - p[0], q[1] - p[1]); return (p[0] + (q[0] - p[0]) * d / L, p[1] + (q[1] - p[1]) * d / L)
for k in range(7):
    p = P(R, k); disc(ax, p[0], p[1], 3, 'resultat' if k == 0 else 'sujet', label=str(k), size='m')
for k in range(7):
    p, q = P(R, k), P(R, (k + 1) % 7); last = k == 6
    arrow(ax, sh(p, q, 3.4), sh(q, p, 3.4), 'resultat' if last else 'varie', lw=1.8 if last else 1.0, curve=0.0)
text(ax, cx, cy + 3, '+1 à chaque pas', 'varie', 's'); text(ax, cx, cy - 3, '7 pas = un tour', 'varie', 's')
text(ax, 44, 4, 'septième pas : retour à 0', 'resultat', 's', weight='bold')
save(fig, '51-127')
