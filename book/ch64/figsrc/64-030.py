import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 2, 6, 50, 54, 'fixe')
box(ax, 6, 34, 42, 18, 'sujet')
box(ax, 8.5, 36.5, 13, 13, 'resultat')
xs = [15, 27, 39]
for x in xs:
    disc(ax, x, 43, 2.6, 'resultat' if x == 15 else 'sujet')
    disc(ax, x, 20, 2.6, 'fixe')
text(ax, 58, 52, r'$S_3$ : 6 éléments', 'fixe', 's', ha='left')
text(ax, 58, 44, r'$A_3$ : 3 éléments', 'sujet', 's', ha='left')
text(ax, 58, 36, r'$\{e\}$ : 1 élément', 'resultat', 's', ha='left')
text(ax, 58, 24, r'$S_3/A_3$ ≅ ℤ/2', 'varie', 's', ha='left')
text(ax, 58, 16, r'$A_3$ ≅ ℤ/3', 'varie', 's', ha='left')
save(fig, '64-030')
