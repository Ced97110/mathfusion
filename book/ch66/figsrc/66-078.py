import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
text(ax, 44, 50, r'$5!=1\times 2\times 3\times 4\times 5$', 'sujet', 'l')
top = ['1', r'$\times 2$', r'$\times 3$', r'$\times 4$', r'$\times 5$']
run = ['1', '2', '6', '24', '120']
w, g = 14, 3.5
for i in range(5):
    x = 2.5 + i * (w + g)
    box(ax, x, 28, w, 10, 'varie', label=top[i], size='m')
    arrow(ax, (x + w / 2, 28), (x + w / 2, 19), 'fixe')
    box(ax, x, 8, w, 10, 'resultat' if i == 4 else 'sujet', label=run[i], size='m')
text(ax, 44, 43, 'on multiplie, un entier de plus à chaque fois', 'varie', 's')
save(fig, '66-078')
