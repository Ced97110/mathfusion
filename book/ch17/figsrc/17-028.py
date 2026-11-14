import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
heads = [('une seule', 'lettre'), ('jamais', 'au carré'), ('jamais au', 'dénominateur')]
forms = [r'$2y - 1 \leq 16$', r'$x^2 < 4$', r'$x \leq 5y + 3$', r'$x$ au dénominateur']
ok = [[1, 1, 1], [1, 0, 1], [0, 1, 1], [1, 1, 0]]
for c, (a, b) in enumerate(heads):
    x = 34 + 17 * c
    text(ax, x + 8, 70, a, 'encre', 's'); text(ax, x + 8, 66, b, 'encre', 's')
for r in range(4):
    y = 44 - 12 * r
    text(ax, 17, y + 5, forms[r], 'sujet' if r == 0 else 'fixe', 'm', weight='bold' if r == 0 else 'normal')
    for c in range(3):
        box(ax, 34 + 17 * c, y, 16, 10, 'resultat' if ok[r][c] else 'limite')
box(ax, 1, 43, 86, 12, 'sujet', fill=False, lw=1.4)
save(fig, '17-028')
