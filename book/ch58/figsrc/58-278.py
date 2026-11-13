import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
labs = [(r'$M_1$', 'sujet'), (r'$M_2$', 'varie'), (r'$M_3$', 'autre')]
for i, (lab, r) in enumerate(labs):
    box(ax, 6 + i * 28, 48, 24, 11, r, label=lab)
brace(ax, 6, 58, 59, 'sujet', label=r'paquet $N_1$', down=False)
brace(ax, 62, 86, 59, 'autre', label=r'paquet $N_2$', down=False)
text(ax, 44, 41, 'un élément x = (a, b, c) :', 'fixe', 's')
box(ax, 4, 26, 38, 10, 'sujet', label='(a, b, 0) dans N₁', size='s')
box(ax, 46, 26, 38, 10, 'autre', label='(0, 0, c) dans N₂', size='s')
text(ax, 44, 31, '+', 'encre', 'l')
arrow(ax, (23, 25), (14, 15.5), 'varie', lw=1.0)
arrow(ax, (23, 25), (36, 15.5), 'varie', lw=1.0)
box(ax, 2, 5, 24, 10, 'sujet', label='(a, 0, 0)', size='s')
box(ax, 30, 5, 24, 10, 'varie', label='(0, b, 0)', size='s')
text(ax, 70, 10, 'écriture unique', 'resultat', 's')
save(fig, '58-278')
