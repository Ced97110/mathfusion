import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ax_, bx_, cw = 30, 59, 27
cA, cB = ax_ + cw / 2, bx_ + cw / 2
# en-têtes : les deux choix de rho
box(ax, ax_, 66, cw, 10, 'resultat', label=r'$\rho$ : tripler', size='s')
box(ax, bx_, 66, cw, 10, 'limite', label=r'$\rho$ : ajouter 1', size='s')
text(ax, cA, 59, r'$\eta$ : doubler' + '\n' + r'$\zeta$ : ne rien changer', 'fixe', 's')
text(ax, cB, 59, r'$\eta,\ \zeta$ :' + '\n' + 'ne rien changer', 'fixe', 's')
# ligne 1 : on additionne d'abord, puis rho
text(ax, 2, 47, r'$\rho(\eta+\zeta)(4)$', 'sujet', 's', ha='left', weight='bold')
text(ax, 2, 42.5, 'somme d’abord', 'fixe', 's', ha='left')
box(ax, ax_, 40, cw, 10, 'sujet', label='3 × 12 = 36', size='s')
box(ax, bx_, 40, cw, 10, 'sujet', label='8 + 1 = 9', size='s')
# ligne 2 : rho séparément
text(ax, 2, 31, r'$\rho\eta(4)+\rho\zeta(4)$', 'autre', 's', ha='left', weight='bold')
text(ax, 2, 26.5, 'chaque règle à part', 'fixe', 's', ha='left')
box(ax, ax_, 24, cw, 10, 'autre', label='24 + 12 = 36', size='s')
box(ax, bx_, 24, cw, 10, 'autre', label='5 + 5 = 10', size='s')
# résultat
text(ax, cA, 10, '36 = 36', 'resultat', 'l', weight='bold')
text(ax, cB, 10, '9 ≠ 10', 'limite', 'l', weight='bold')
save(fig, '57-051')
