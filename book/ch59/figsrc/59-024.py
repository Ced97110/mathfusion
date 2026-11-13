import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
vals = [2, 0, 5]
w, g, x0 = 22.0, 4.0, 5.0
for i, v in enumerate(vals):
    x = x0 + i * (w + g)
    box(ax, x, 22, w, 26, 'sujet')
    text(ax, x + w / 2, 52, f'case {i + 1}', 'sujet', 's')
    for k in range(v):
        disc(ax, x + 4 + (k % 3) * 6.5, 42 - (k // 3) * 7, 2.2, 'varie')
    text(ax, x + w / 2, 17, str(v), 'varie', 'l')
text(ax, 44, 60, r'$D^{(n)}$ : listes de $n$ éléments de $D$', 'encre', 's')
text(ax, 44, 8, r'ici $D=\mathbb{Z}$, $n=3$ : la liste $(2,\,0,\,5)$', 'sujet', 's')
save(fig, '59-024')
