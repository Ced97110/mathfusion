import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 15, 62, 'applications', 'sujet', 'm', weight='bold')
text(ax, 73, 62, 'tableaux 2 × 2', 'autre', 'm', weight='bold')
L = [r'$\eta$', r'$\eta+\eta^{\prime}$', r'$\rho\circ\eta$']
R = [r'$A$', r'$A+A^{\prime}$', r'$CA$']
T = ['correspond à', 'somme ↔ somme', 'composée ↔ produit']
for k in range(3):
    y = 44 - 18 * k
    box(ax, 3, y, 24, 11, 'sujet', label=L[k])
    box(ax, 61, y, 24, 11, 'autre', label=R[k])
    arrow(ax, (27.5, y + 5.5), (60.5, y + 5.5), 'resultat', both=True)
    text(ax, 44, y + 9, T[k], 'resultat', 's')
text(ax, 44, 3, 'isomorphisme d’anneaux', 'resultat', 'm', weight='bold')
save(fig, '58-222')
