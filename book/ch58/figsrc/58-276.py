import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'listes à trois cases $(a,\ b,\ c)$', 'fixe', 's')
# ligne 1 : trois morceaux
for i, (lab, r) in enumerate([(r'$M_1$', 'sujet'), (r'$M_2$', 'varie'), (r'$M_3$', 'autre')]):
    box(ax, 6 + i * 28, 42, 24, 12, r, label=lab)
# ligne 2 : deux morceaux, les deux premiers regroupés
box(ax, 4, 6, 56, 16, 'sujet', fill=False, dash=True)
box(ax, 6, 8, 24, 12, 'sujet', label=r'$M_1$')
box(ax, 34, 8, 24, 12, 'varie', label=r'$M_2$')
box(ax, 62, 6, 24, 16, 'autre', label=r'$M_3$')
text(ax, 32, 25, r'$N=M_1\oplus M_2$', 'sujet', 's')
arrow(ax, (30, 39), (30, 29.5), 'resultat', lw=1.1)
arrow(ax, (50, 29.5), (50, 39), 'resultat', lw=1.1)
text(ax, 27, 34, 'regrouper', 'resultat', 's', ha='right')
text(ax, 53, 34, 'redécouper', 'resultat', 's', ha='left')
save(fig, '58-276')
