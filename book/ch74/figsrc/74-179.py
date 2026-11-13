import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
x0, y0, c = 8, 36, 11
roles = [['sujet','fixe','fixe'],['fixe','sujet','fixe'],['fixe','fixe','varie']]
for r in range(3):
    for k in range(3): box(ax, x0 + k*c, y0 + (2-r)*c, c, c, roles[r][k], lw=0.6)
text(ax, x0 + 0.5*c, y0 + 2.5*c, r'$\cos\theta$', 'sujet', 's'); text(ax, x0 + 1.5*c, y0 + 1.5*c, r'$\cos\theta$', 'sujet', 's')
text(ax, x0 + 2.5*c, y0 + 0.5*c, '1', 'varie', 'm')
text(ax, x0 + 1.0*c, y0 + 3*c + 3, 'plan tourné', 'sujet', 's'); text(ax, x0 + 4.4*c, y0 + 0.5*c, 'axe fixe', 'varie', 's', ha='left')
text(ax, 69, y0 + 2.2*c, r'trace', 'resultat', 's')
text(ax, 69, y0 + 1.6*c, r'$1+2\cos\theta$', 'resultat', 'm')
text(ax, 22, 28, 'quart de tour : 1 + 0 = 1', 'resultat', 's', ha='left')
text(ax, 22, 20, r'$\frac{1}{5}$ de tour : 1 + 0,618', 'limite', 's', ha='left')
text(ax, 22, 13, '≈ 1,618, pas entier', 'limite', 's', ha='left')
disc(ax, 14, 28, 3, 'resultat'); disc(ax, 14, 17, 3, 'limite')
save(fig, '74-179')
