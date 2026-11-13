import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# r = cos 3θ, θ = 60° : r = cos 180° = -1 -> on recule de 1 : le point est sur la demi-droite de 240°
fig, ax = canvas(86)
o = (40, 46); u = 26
def pt(r, deg): return (o[0] + u * r * math.cos(math.radians(deg)), o[1] + u * r * math.sin(math.radians(deg)))
def arc(rad, a0, a1, role):
    line(ax, [(o[0] + rad * math.cos(math.radians(a)), o[1] + rad * math.sin(math.radians(a))) for a in range(a0, a1 + 1, 3)], role, lw=1.2)
line(ax, [(o[0] - 30, o[1]), (o[0] + 34, o[1])], 'fixe')
line(ax, [o, pt(1.25, 60)], 'fixe', dash=True)
line(ax, [o, pt(1.25, 240)], 'fixe', dash=True)
arc(8, 0, 60, 'varie')
arc(12, 0, 240, 'sujet')
q = pt(1, 240)
arrow(ax, (o[0] - 0.4, o[1] - 0.7), (q[0] + 0.5, q[1] + 0.9), 'varie', lw=1.6)
disc(ax, q[0], q[1], 1.5, 'sujet')
disc(ax, o[0], o[1], 0.9, 'encre')
text(ax, o[0] + 17, o[1] + 6, r'$\theta$ = 60°', 'varie', 's')
text(ax, o[0] + 22, o[1] - 12, r'$\theta + \pi$ = 240°', 'sujet', 's')
text(ax, o[0] + 16, o[1] - 27, 'on recule de 1', 'varie', 's')
text(ax, o[0] + 3, o[1] - 3.5, 'O', 'encre', 's')
text(ax, 44, 12, r'$r = \cos 3\theta = \cos 180° = -1$', 'sujet', 'm')
text(ax, 44, 5, r'$|r|$ = 1 : distance, sur la demi-droite de 240°', 'sujet', 's')
text(ax, 44, 83, 'avancer de 1 devient reculer de 1', 'encre', 'm')
save(fig, '40-032')
