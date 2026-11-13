import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
a = 0.35
s = 34.5                    # 1 m = 34,5 mm ; arche de 2,20 m = 76 mm
ox, oy = 5, 14
X = lambda t: ox + s * a * (t - math.sin(t))
Y = lambda t: oy + s * a * (1 - math.cos(t))
line(ax, [(2, oy), (86, oy)], 'fixe', lw=1.0)
line(ax, [(X(2 * math.pi * i / 400), Y(2 * math.pi * i / 400)) for i in range(401)], 'sujet', lw=1.4)
# roue à t = π/2 : C = (a t, a), I sous C, M = C + a(−sin t, −cos t)
t = math.pi / 2
cxm, cym = ox + s * a * t, oy + s * a
R = s * a
line(ax, [(cxm + R * math.cos(u), cym + R * math.sin(u)) for u in [2 * math.pi * i / 200 for i in range(201)]], 'fixe', lw=1.0)
mx, my = cxm - R * math.sin(t), cym - R * math.cos(t)
line(ax, [(cxm, cym), (cxm, oy)], 'fixe', lw=1.0)
line(ax, [(cxm, cym), (mx, my)], 'sujet', lw=1.0)
# arc de l'angle t entre CI (vers le bas) et CM (vers la gauche) : encre
arc = [(cxm + 5 * math.cos(-math.pi / 2 - u), cym + 5 * math.sin(-math.pi / 2 - u)) for u in [t * i / 30 for i in range(31)]]
line(ax, arc, 'encre', lw=1.0)
text(ax, cxm - 3.6, cym - 7.4, 't', 'encre', 's')
disc(ax, cxm, cym, 0.9, 'fixe')
disc(ax, cxm, oy, 0.9, 'fixe')
disc(ax, mx, my, 1.2, 'varie')
text(ax, cxm + 3, cym + 2.2, 'C', 'fixe', 's')
text(ax, cxm + 2.5, oy - 3, 'I', 'fixe', 's')
text(ax, mx - 3.5, my + 1, 'M', 'varie', 's')
for tt, lab in [(0, 't = 0'), (math.pi, 't = π'), (2 * math.pi, 't = 2π')]:
    disc(ax, X(tt), Y(tt), 1.1, 'sujet')
    text(ax, X(tt), Y(tt) + (4 if tt == math.pi else -4), lab, 'sujet', 's')
save(fig, '40-096')
