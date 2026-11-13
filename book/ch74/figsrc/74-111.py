import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(94)
c = (44, 62); u = 8
P = lambda a, b: (c[0]+a*u, c[1]+b*u)
r = math.sqrt(10)*u
line(ax, [(c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a))) for a in range(0, 361, 4)], 'fixe', dash=True)
for q, role in [((3, 1), 'sujet'), ((1, -3), 'resultat')]:
    line(ax, [c, P(*q)], role, lw=1.4); disc(ax, *P(*q), 1.6, role)
disc(ax, c[0], c[1], 1.0, 'encre')
text(ax, P(3,1)[0]+3, P(3,1)[1]+4, r'$(3,1)$', 'sujet', 's')
text(ax, P(1,-3)[0]+3, P(1,-3)[1]-4, r'$(1,-3)$', 'resultat', 's')
text(ax, P(1.9,0.7)[0]+2, P(1.9,0.7)[1]-4, r'$\sqrt{10}$', 'sujet', 'm')
text(ax, P(0.4,-2)[0]-5, P(0.4,-2)[1], r'$\sqrt{10}$', 'resultat', 'm')
box(ax, 2, 2, 84, 26, 'fixe')
text(ax, 44, 23, r'$\det s_1=-1$ et $\det s_2=-1$', 'varie', 's')
text(ax, 44, 16, r'$(-1)\times(-1)=1$', 'resultat', 'l')
text(ax, 44, 8, 'déterminant 1 : pas une réflexion', 'resultat', 's')
save(fig, '74-111')
