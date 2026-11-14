import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 53, r'$\div$ 100 est écrit %', 'varie', 'm')
for y, n in [(36, 35), (22, 12), (8, 80)]:
    box(ax, 6, y, 28, 11, 'fixe', label=rf'$\frac{{{n}}}{{100}}$')
    arrow(ax, (36, y + 5.5), (52, y + 5.5), 'varie')
    box(ax, 54, y, 28, 11, 'sujet', label=f'{n} %', size='l')
save(fig, '09-069')
