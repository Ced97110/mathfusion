import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
for y, a, b, c, r1, r2, lab, side in ((40, '3', r'$-3$', '0', 'sujet', 'varie', r'opposé de 3 : $-3$', 'nombres'),
                                      (14, r'$A$', r'$A$', r'$\varnothing$', 'sujet', 'varie', r'opposé de $A$ : $A$', 'parties')):
    box(ax, 4, y, 16, 12, r1, label=a, size='l'); text(ax, 25, y + 6, '+', 'encre', 'xl')
    box(ax, 30, y, 16, 12, r2, label=b, size='l'); text(ax, 51, y + 6, '=', 'encre', 'xl')
    box(ax, 56, y, 16, 12, 'resultat', label=c, size='l')
    text(ax, 38, y - 4.5, lab, r2, 's'); text(ax, 80, y + 6, side, 'fixe', 's')
save(fig, '80-322')
