import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
for y, lab, r1, r2, l1, l2 in [(40, 'couple', 'sujet', 'autre', r'$g$', r'$h$'), (22, 'neutre', 'fixe', 'fixe', r'$e_G$', r'$e_H$'), (4, 'résultat', 'resultat', 'resultat', r'$g$', r'$h$')]:
    text(ax, 3, y + 5, lab, 'encre', 'm', ha='left')
    box(ax, 28, y, 18, 10, r1, label=l1); box(ax, 48, y, 18, 10, r2, label=l2)
text(ax, 47, 36, r'$\times$', 'varie', 'l')
for x in (37, 57): arrow(ax, (x, 22), (x, 14.5), 'varie')
text(ax, 69, 9, 'inchangé', 'resultat', 's', ha='left')
save(fig, '45-162')
