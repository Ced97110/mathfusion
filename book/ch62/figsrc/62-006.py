import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, '$x^3+x+1$ dans le corps {0 ; 1}', 'sujet', 'm')
text(ax, 44, 55, 'ici 1 + 1 = 0', 'fixe', 's')
for x, v, calc, res in [(4, '0', '0 + 0 + 1', '1'), (47, '1', '1 + 1 + 1 = 3', '3 vaut 1')]:
    box(ax, x, 40, 37, 9, 'sujet', label=f'on essaie {v}')
    arrow(ax, (x + 18.5, 39.5), (x + 18.5, 33.5), 'varie')
    box(ax, x, 23, 37, 10, 'fixe', label=calc)
    arrow(ax, (x + 18.5, 22.5), (x + 18.5, 16.5), 'varie')
    box(ax, x, 6, 37, 10, 'limite', label=(f'{res} ≠ 0' if res == '1' else '3 vaut 1 : ≠ 0'))
save(fig, '62-006')
