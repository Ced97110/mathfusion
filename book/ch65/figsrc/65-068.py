import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 72, r'$d = 81 = 9^2$ : un carré', 'resultat', 'm')
text(ax, 44, 65, r'irréductible : ordre 3 ou 6', 'fixe', 's')
labs = ['1', '(123)', '(132)', '(12)', '(13)', '(23)']
for i, s in enumerate(labs):
    box(ax, 3 + i * 14, 38, 12, 9, 'resultat' if i < 3 else 'fixe', label=s, size='s')
brace(ax, 3, 43, 48, 'resultat', r'$A_3$ : 3 éléments', down=False)
brace(ax, 3, 85, 37, 'fixe', r'$S_3$ : 6 éléments', down=True)
text(ax, 44, 52.5, '', 'fixe', 's')
box(ax, 24, 4, 40, 12, 'resultat', label=r'$G_f = A_3$', size='l')
arrow(ax, (44, 26), (44, 17), 'varie')
text(ax, 62, 21.5, 'dans A₃', 'varie', 's')
save(fig, '65-068')
