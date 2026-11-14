import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 58, 'valeur de la forme sur la flèche', 'fixe', 's')
text(ax, 54, 49, r'$e_1$', 'fixe', 'l'); text(ax, 74, 49, r'$e_2$', 'fixe', 'l')
text(ax, 30, 49, 'flèche', 'fixe', 's', ha='right')
vals = ((r'$e_1^*$', 1, 0, 30), (r'$e_2^*$', 0, 1, 12))
for lab, a, b, y in vals:
    text(ax, 24, y + 7, lab, 'sujet', 'l')
    for x, v in ((46, a), (66, b)):
        box(ax, x, y, 16, 14, 'resultat' if v else 'fixe', label=str(v), size='l')
save(fig, '71-039')
