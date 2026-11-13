import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 52, r'$PSL_2(F)$ : nombre d’éléments', 'sujet', 's')
rows = [('F à 2 éléments : pas simple', 6, 'limite'), ('F à 3 éléments : pas simple', 12, 'limite'), ('F à 5 éléments : simple', 60, 'resultat')]
for k, (lab, n, r) in enumerate(rows):
    y = 34 - 15*k
    text(ax, 3, y+9, lab, r, 's', ha='left')
    box(ax, 3, y, 1.1*n+1.5, 5, r, r=0.5)
    text(ax, 3 + 1.1*n + 4, y+2.5, str(n), r, 'm', ha='left')
save(fig, '73-060')
