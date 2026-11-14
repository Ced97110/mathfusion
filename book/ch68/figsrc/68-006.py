import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
for i, b in enumerate('0010'):
    box(ax, 30 + i * 13, 40, 10, 9, 'varie' if i == 1 else 'fixe', label=b, size='l')
for i, b in enumerate('0110'):
    box(ax, 30 + i * 13, 12, 10, 9, 'resultat', label=b, size='l')
text(ax, 2, 44.5, 'reçu', 'encre', 'm', ha='left')
text(ax, 2, 16.5, 'corrigé', 'resultat', 'm', ha='left')
text(ax, 48, 53, 'bit 2 faux', 'varie', 's')
arrow(ax, (48, 39.5), (48, 21.8), 'varie', lw=1.3)
text(ax, 51, 30.5, 'remettre à 1', 'varie', 's', ha='left')
text(ax, 54.5, 6, '0110 : seul mot permis à 1 bit près', 'resultat', 's')
save(fig, '68-006')
