import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'$S_3$ : 6 éléments, 2 classes de 3', 'encre', 'm')
rows = [(36, 'sujet', ['1', '(1 2 3)', '(1 3 2)'], r'$N$' + '\npaires'),
        (14, 'varie', ['(1 2)', '(1 3)', '(2 3)'], 'reste\nimpaires')]
for y, role, labs, name in rows:
    text(ax, 10, y + 5, name, role, 's')
    for i, l in enumerate(labs):
        box(ax, 21 + i * 18, y, 16, 10, role, label=l, size='s')
    box(ax, 19, y - 2, 56, 14, role, fill=False, dash=True, lw=0.7)
    text(ax, 81, y + 5, 'gauche\n= droite', 'resultat', 's')
save(fig, '47-161')
