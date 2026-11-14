import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
for y, lab, res, r in [(46, 'double', '(2, 4)', 'fixe'), (28, 'somme', '(3, 2)', 'fixe'), (10, r'$I$ : ne bouge pas', '(1, 2)', 'resultat')]:
    box(ax, 4, y, 18, 10, 'sujet', label='(1, 2)', size='s'); box(ax, 66, y, 18, 10, r, label=res, size='s')
    arrow(ax, (23, y + 5), (65, y + 5), 'resultat' if r == 'resultat' else 'varie'); text(ax, 44, y + 9, lab, 'resultat' if r == 'resultat' else 'varie', 's')
save(fig, '43-042')
