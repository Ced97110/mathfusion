import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 24, 56, 40, 12, 'sujet', label=r'$2\cos 72° \approx 0{,}618$', size='m')
arrow(ax, (34, 56), (22, 44), 'resultat'); arrow(ax, (54, 56), (66, 44), 'limite')
c = (22, 26); R = 11
poly(ax, [(c[0] + R*math.cos(math.radians(90 + 72*k)), c[1] + R*math.sin(math.radians(90 + 72*k))) for k in range(5)], 'resultat')
text(ax, 22, 8, 'chap. 66 : constructible', 'resultat', 's')
text(ax, 22, 4, 'règle et compas', 'resultat', 's')
f = numberline(ax, 52, 76, 28, 0, 1, arrow_right=False, role='fixe', size='s')
disc(ax, f(0.618), 28, 1.6, 'limite')
text(ax, f(0.618), 35, '0,618', 'limite', 's')
text(ax, 66, 14, 'chap. 74 : pas entier', 'limite', 's')
text(ax, 66, 8, 'impossible pour un réseau', 'limite', 's')
save(fig, '74-185')
