import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def row(y, roots, tag):
    text(ax, 5, y + 5.5, tag, 'fixe', 's', ha='left')
    xs = (3, 22, 41)
    for x, a in zip(xs, roots):
        box(ax, x, y, 18, 10, 'sujet', label=rf'$x-{a}$')
    box(ax, 66, y, 18, 10, 'fixe', label=r'$k=1/4$')
    text(ax, 62.5, y + 5, r'$\times$', 'encre', 'm')
text(ax, 44, 76, r'$f=(x-a_1)\cdots(x-a_r)\,k$', 'sujet', 's')
text(ax, 30, 66, 'racines 1, 2, 3', 'varie', 's')
row(50, (1, 2, 3), '')
text(ax, 30, 40, 'racines 5, 6, 7', 'varie', 's')
row(24, (5, 6, 7), '')
box(ax, 8, 4, 72, 11, 'resultat', label=r'la forme reste : $n = r + \deg k$')
save(fig, '54-239')
