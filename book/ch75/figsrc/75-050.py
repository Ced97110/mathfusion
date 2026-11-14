import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
for k, n in enumerate([1, 2, 3]):
    y = 33 - k * 14
    text(ax, 9, y + 4, rf'$n={n}$', 'encre', 'm')
    for p in range(n):
        x = 22 + p * 15
        box(ax, x, y, 13, 8, 'sujet')
        for c in range(2):
            box(ax, x + 1.8 + c * 5.2, y + 1.8, 4, 4.4, 'varie', r=0.3)
    text(ax, 78, y + 4, rf'$2n={2*n}$', 'resultat', 'm')
text(ax, 44, 46, 'une paire = deux flèches', 'sujet', 's')
save(fig, '75-050')
