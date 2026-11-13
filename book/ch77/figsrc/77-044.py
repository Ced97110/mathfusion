import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cols = [(40, 'somme'), (56, r'$\times$ nombre'), (72, 'produit')]
for x, t in cols: text(ax, x, 64, t, 'fixe', 's')
for y, lab in ((54, r'$\mathbb{C}$'), (44, r'$a+b\sqrt{2}$'), (34, r'matrices $2\times2$')):
    text(ax, 2, y, lab, 'encre', 's', ha='left')
    for x, _ in cols: line(ax, [(x - 1.5, y), (x - 0.5, y - 1.3), (x + 1.8, y + 1.8)], 'resultat', 1.2)
line(ax, [(2, 59), (82, 59)], 'fixe', 0.5)
arrow(ax, (44, 28), (44, 17), 'sujet')
box(ax, 22, 3, 44, 14, 'sujet', label=r'$A$ : l’algèbre', size='m')
save(fig, '77-044')
