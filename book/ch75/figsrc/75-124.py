import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 34, 50, r'$q^{3}(q^{4}-1)$', 'sujet', 'm'); text(ax, 61, 50, r'$q(q^{2}-1)$', 'autre', 'm'); text(ax, 80, 50, 'produit', 'resultat', 's')
for y, lab, a, c, d in [(34, r'$q=2$', '8 × 15', '2 × 3', '720'), (14, r'$q=3$', '27 × 80', '3 × 8', '51 840')]:
    text(ax, 2, y, lab, 'encre', 's', ha='left')
    box(ax, 12, y - 6, 28, 12, 'sujet', label=a, size='s'); box(ax, 46, y - 6, 22, 12, 'autre', label=c, size='s')
    box(ax, 72, y - 6, 15, 12, 'resultat', label=d, size='s')
    text(ax, 43, y, '×', 'varie', 'm'); text(ax, 70, y, '', 'varie', 's')
save(fig, '75-124')
