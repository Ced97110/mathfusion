import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# θ en radians : θ = π/3 (60°) donne r = 1,5 ; θ = 60 (radians) donne r = 1 + cos 60 ≈ 0,05
fig, ax = canvas(70)
u = 14
text(ax, 44, 66, r'$r = 1 + \cos\theta$', 'encre', 'm')
def panel(o, theta, r, role, lab, res):
    line(ax, [(o[0] - 4, o[1]), (o[0] + 30, o[1])], 'fixe')
    d = 18 if abs(theta) > 10 else 28
    line(ax, [o, (o[0] + d * math.cos(theta), o[1] + d * math.sin(theta))], 'fixe', dash=True)
    q = (o[0] + u * r * math.cos(theta), o[1] + u * r * math.sin(theta))
    line(ax, [o, q], role, lw=1.6)
    disc(ax, q[0], q[1], 1.2, role)
    text(ax, o[0] + 13, o[1] + 44, lab, role, 'm')
    text(ax, o[0] + 13, o[1] + 38, res, role, 's')
    return q
oL = (6, 20)
panel(oL, math.radians(60), 1.5, 'resultat', r'$\theta = \pi/3$', r'$r$ = 1,5')
text(ax, oL[0] + 22, oL[1] + 8, '60°', 'varie', 's')
# 60 radians = 9,55 tours : angle effectif 60 - 18π rad
th = 60.0
r2 = 1 + math.cos(th)
oR = (50, 20)
q = panel(oR, th, r2, 'limite', r'$\theta$ = 60', r'$r \approx$ 0,05')
text(ax, oR[0] + 13, oR[1] + 30, '60 radians', 'limite', 's')
text(ax, oR[0] + 13, oR[1] + 25, '≈ 9,5 tours', 'limite', 's')
text(ax, oR[0] + 20, oR[1] + 6, 'point collé à O', 'limite', 's')
disc(ax, oR[0], oR[1], 0.7, 'encre')
disc(ax, oL[0], oL[1], 0.7, 'encre')
text(ax, oL[0] - 1, oL[1] - 3, 'O', 'encre', 's')
text(ax, oR[0] - 1, oR[1] - 3, 'O', 'encre', 's')
save(fig, '40-029')
