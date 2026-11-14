import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
U = 0.26    # 1 zéro = 0,26 mm ; les longueurs comptent les zéros
X = 4.0
# la puissance de la machine : 9 + 9 = 18 zéros
text(ax, X, 62, 'puissance par seconde :', 'sujet', 's', ha='left')
box(ax, X, 50, 9 * U, 8, 'sujet', r=0.3)
box(ax, X + 9 * U, 50, 9 * U, 8, 'autre', r=0.3)
text(ax, X + 18 * U + 3, 54, r'$10^{9} \times 10^{9} = 10^{18}$', 'sujet', 's', ha='left')
# le travail : 300 zéros
text(ax, X, 36, 'nombre d’essais : 300 chiffres', 'varie', 's', ha='left')
box(ax, X, 24, 18 * U, 8, 'sujet', r=0.3)
box(ax, X + 18 * U, 24, 282 * U, 8, 'varie', r=0.3)
brace(ax, X + 18 * U, X + 300 * U, 24, 'varie', label='il reste 282 zéros')
text(ax, 60, 14, 'la machine n’en gagne que 18', 'sujet', 's')
save(fig, '53-166')
