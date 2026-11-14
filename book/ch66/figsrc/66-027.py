import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
fig, ax = canvas(68)
cy, r = 34, 15
cx = 22
disc(ax, cx, cy, r, 'fixe', fill=False)
h = [P(cx, cy, r, 60 * k) for k in range(6)]
poly(ax, h, 'sujet')
for p in h: disc(ax, p[0], p[1], 1.5, 'sujet')
text(ax, cx, 57, r'$\zeta_6$ : pas de 60°', 'sujet', 's')
text(ax, cx, 10, 'atteint les 6 sommets :\nprimitive', 'sujet', 's')
cx = 66
disc(ax, cx, cy, r, 'fixe', fill=False)
h = [P(cx, cy, r, 60 * k) for k in range(6)]
poly(ax, [h[0], h[2], h[4]], 'autre')
for k, p in enumerate(h): disc(ax, p[0], p[1], 1.5, 'autre' if k % 2 == 0 else 'fixe')
text(ax, cx, 57, r'$\zeta_6^2$ : pas de 120°', 'autre', 's')
text(ax, cx, 10, 'atteint 3 sommets sur 6 :\npas primitive', 'autre', 's')
save(fig, '66-027')
