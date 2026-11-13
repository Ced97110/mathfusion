import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

u, v = (2, 0), (1, 2)
nu, nv = 2.0, 5 ** 0.5
c = (u[0] * v[0] + u[1] * v[1]) / (nu * nv)
sn = (1 - c * c) ** 0.5
assert abs(nu * nv * sn - 4) < 1e-9
fr = lambda x: f'{x:.3f}'.replace('.', ',')
o = (8, 10); L = 30
fig, ax = canvas(56)
arrow(ax, o, (o[0] + 34, o[1]), 'fixe', lw=0.8)
tip = (o[0] + L * c, o[1] + L * sn)
line(ax, [o, (o[0] + L * c, o[1])], 'sujet', lw=2.0)
line(ax, [(o[0] + L * c, o[1]), tip], 'resultat', lw=2.0)
arrow(ax, o, tip, 'autre', lw=1.0)
text(ax, o[0] + L * c / 2, o[1] - 3.5, r'$\cos\theta$', 'sujet', 's')
text(ax, tip[0] + 6, o[1] + L * sn / 2, r'$\sin\theta$', 'resultat', 's')
text(ax, o[0] + 5, o[1] + 7.5, r'$\theta$', 'encre', 's')
text(ax, o[0] - 1, tip[1] + 3, r'$v$ de longueur 1', 'autre', 's', ha='left')
box(ax, 44, 34, 42, 16, 'sujet', label=f'cosinus {fr(c)}\nproduit scalaire = 2\nun nombre', size='s')
box(ax, 44, 10, 42, 20, 'resultat', label=f'sinus {fr(sn)}\nproduit vectoriel\n$\\|u\\times v\\|$ = 4\nun vecteur', size='s')
save(fig, '41-103')
