import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 23, 66, r'$N$ = 3 rotations', 'encre', 's')
text(ax, 65, 66, r'$N=\{e\}$', 'encre', 's')
# left
cx = 23
box(ax, cx - 16, 44.5, 32, 11, 'resultat')
for dx in (-11, 0, 11):
    disc(ax, cx + dx, 50, 3.3, 'sujet')
    disc(ax, cx + dx, 36, 3.3, 'fixe')
text(ax, cx, 59.5, r"$N=G'$", 'resultat', 's')
text(ax, cx, 24, 'G/N : 2 éléments\nabélien', 'resultat', 's')
text(ax, cx, 12, r"$G'\subseteq N$", 'resultat', 'm')
# right
cx = 65
box(ax, cx - 16, 43.5, 32, 13, 'sujet', fill=False, dash=True)
box(ax, cx - 15.5, 45.5, 9, 9, 'limite')
for dx in (-11, 0, 11):
    disc(ax, cx + dx, 50, 3.3, 'sujet')
    disc(ax, cx + dx, 36, 3.3, 'fixe')
text(ax, cx - 11, 50, '$e$', 'encre', 's')
text(ax, cx + 12, 59.5, r"$G'$", 'sujet', 's')
text(ax, cx, 24, 'G/N : 6 éléments\nnon abélien', 'limite', 's')
text(ax, cx, 12, "$G'$ ⊄ $N$", 'limite', 'm')
save(fig, '50-213')
