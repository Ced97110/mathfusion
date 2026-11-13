import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xs = [5.5 + i * 20 for i in range(4)]
for i, (x, n) in enumerate(zip(xs, ['28', '31', '29', '32'])):
    text(ax, x + 8.5, 57, str(i + 1), 'varie', 's')
    box(ax, x, 40, 17, 10, 'fixe', label=n)
    arrow(ax, (x + 8.5, 40), (x + 8.5, 31), 'varie')
    box(ax, x, 20, 17, 10, 'sujet', label='30')
brace(ax, xs[0], xs[-1] + 17, 18, 'sujet', r'$n \times c$ : $c$ = 30', depth=2.0)
text(ax, 44, 6, r'$n = 4$ termes répétés', 'sujet', 'm')
save(fig, '10-025')
