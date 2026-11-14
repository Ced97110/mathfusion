import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
def row(y, lab, vals):
    text(ax, 17, y + 5, lab, 'encre', 's')
    for i, (v, r, ok) in enumerate(vals):
        box(ax, 36 + i * 24, y, 20, 10, 'resultat' if ok else 'limite', label=f'{v}\nreste {r}', size='s')
row(70, '$n_3$ divise 5\n(reste modulo 3)', [(1, 1, True), (5, 2, False)])
row(54, '$n_5$ divise 3\n(reste modulo 5)', [(1, 1, True), (3, 3, False)])
text(ax, 44, 41, r'$n_3 = 1$ et $n_5 = 1$', 'resultat', 'l')
cx, cy, R = 22, 19, 13
disc(ax, cx, cy, R, 'fixe', fill=False)
for k in range(15):
    a = math.pi / 2 - 2 * math.pi * k / 15
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 1.0, 'sujet')
text(ax, 64, 25, '15 éléments', 'sujet', 'm')
text(ax, 64, 15, 'groupe cyclique', 'resultat', 'm')
save(fig, '50-177')
