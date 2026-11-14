import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'$\mathrm{deg}\ m$ = plus haute puissance de $x$', 'sujet', 'l')
rows = [(48, r'$x^2$', r'$-\ 2$', 'deg = 2'), (22, r'$x^4$', r'$-\ 4$', 'deg = 4')]
for y, hi, lo, res in rows:
    box(ax, 6, y - 6, 20, 12, 'sujet', label=hi, size='l')
    box(ax, 28, y - 6, 16, 12, 'fixe', label=lo, size='l')
    arrow(ax, (44, y), (56, y), 'varie')
    box(ax, 56, y - 6, 26, 12, 'resultat', label=res, size='l')
text(ax, 16, 36.5, 'plus haute puissance', 'sujet', 's')
text(ax, 16, 10.5, 'plus haute puissance', 'sujet', 's')
text(ax, 69, 56.5, 'le degré', 'resultat', 's')
save(fig, '61-063')
