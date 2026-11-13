import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
text(ax, 44, 96, r'$\frac{4}{x-1}=\frac{2}{x+6}$', 'encre', 'l')
steps = [('1 valeurs interdites', r'$x\neq 1$ et $x\neq -6$'),
         ('2 multiplier par PPCM', r'$4(x+6)=2(x-1)$'),
         ('3 résoudre', r'$x=-13$'),
         ('4 contrôler', r"$-13$ n'est pas interdit")]
for i, (a, b) in enumerate(steps):
    y = 66 - i * 22
    box(ax, 3, y, 38, 12, 'sujet', True, a, 's')
    box(ax, 46, y, 39, 12, 'resultat', True, b, 's')
    arrow(ax, (41, y + 6), (46, y + 6), 'varie')
    if i < 3: arrow(ax, (22, y - 0.5), (22, y - 9.5), 'varie')
save(fig, '21-087')
