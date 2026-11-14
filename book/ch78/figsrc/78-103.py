import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
text(ax, 44, 76, r'$D$ commutatif et associatif', 'encre', 'm')
text(ax, 44, 69, r'si $A$ l’est et si $\bar{x}=x$', 'encre', 'm')
for y, A, cond, D, res, role in [(42, r'$A=\mathbb{R}$', r'$\bar{x}=x$ : vrai', r'$D=\mathbb{C}$', 'commutatif', 'resultat'),
                                 (14, r'$A=\mathbb{C}$', r'$\bar{i}=-i$ : $\bar{x}=x$ faux', r'$D=\mathbb{H}$', r'$ij=-ji$ : pas commutatif', 'limite')]:
    box(ax, 3, y, 24, 12, 'sujet', label=A)
    arrow(ax, (29, y + 6), (45, y + 6), 'varie', lw=1.4)
    text(ax, 37, y + 10, 'double', 'varie', 's')
    box(ax, 47, y, 38, 12, role, label=D)
    text(ax, 15, y - 4, cond, role, 's')
    text(ax, 66, y - 4, res, role, 's')
save(fig, '78-103')
