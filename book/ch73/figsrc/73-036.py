import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 2, 4, 84, 56, 'fixe')
text(ax, 44, 55, r'$GL_n(F)$ : $\det \neq 0$', 'fixe', 'm', weight='bold')
box(ax, 5, 6, 50, 43, 'sujet')
text(ax, 30, 44, r'$SL_n(F)$ : $\det = 1$', 'sujet', 'm', weight='bold')
for y, s in [(32, 'cisaillement : det 1'), (20, 'rotation de 30° : det 1')]:
    disc(ax, 10, y, 2, 'resultat'); text(ax, 14, y, s, 'resultat', 's', ha='left')
disc(ax, 60, 32, 2, 'limite'); text(ax, 71, 24, 'dilatation\n×2 : det 2', 'limite', 's')
save(fig, '73-036')
