import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
labs = ['$e$', r'$(1\ 2)(3\ 4)$', r'$(1\ 3)(2\ 4)$', r'$(1\ 4)(2\ 3)$']
for i, lab in enumerate(labs):
    box(ax, 4 + i * 20.2, 46, 19, 9, 'resultat', label=lab, size='s')
brace(ax, 4, 4 + 3 * 20.2 + 19, 45, 'resultat', label=r'sous-groupe de $4 = 2^2$ éléments', down=True, size='s')
f = numberline(ax, 12, 76, 14, 1, 5, step=1, labels=True, arrow_right=False, size='s')
text(ax, 44, 4, 'taille du sous-groupe', 'fixe', 's')
for v in (2, 3, 5):
    disc(ax, f(v), 22, 2.0, 'sujet')
disc(ax, f(4), 22, 2.0, 'resultat')
text(ax, 26, 32, 'Cauchy : 2, 3, 5', 'sujet', 's')
text(ax, 66, 32, 'Sylow I ajoute : 4', 'resultat', 's')
save(fig, '50-058')
