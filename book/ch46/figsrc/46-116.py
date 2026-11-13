import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
y = 58
text(ax, 11, y, r'$s$ℤ  =', 'sujet', 'xl')
text(ax, 25, y, '{', 'encre', 'xl')
text(ax, 34, y, r'$sk$', 'varie', 'xl')
text(ax, 42, y, '|', 'encre', 'xl')
text(ax, 58, y, r'$k$ ∈ ℤ', 'autre', 'xl')
text(ax, 72, y, '}', 'encre', 'xl')
brace(ax, 30, 38, y - 5, 'varie', label=None)
text(ax, 22, y - 14, r'$s$ fois $k$', 'varie', 's')
brace(ax, 50, 67, y - 5, 'autre', label=None)
text(ax, 66, y - 14, r'$k$ parcourt ℤ', 'autre', 's')
text(ax, 44, 38, r'une lettre $s$ à la place de 2, 3, 6', 'sujet', 's')
for i, (n, lab) in enumerate([(2, '2ℤ'), (3, '3ℤ'), (6, '6ℤ')]):
    x = 8 + i * 28
    arrow(ax, (x + 10, 29), (x + 10, 21), 'varie')
    box(ax, x, 9, 20, 10, 'sujet', label=lab, size='l')
    text(ax, x + 10, 32.5, rf'$s$ = {n}', 'varie', 's')
save(fig, '46-116')
