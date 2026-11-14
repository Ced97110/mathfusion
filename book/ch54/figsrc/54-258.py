import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 66, r'$p=x^4-2x^3+x+1$ modulo 2', 'sujet', 's')
cells = [r'$x^4$', r'$-2x^3$', r'$x$', r'$1$']
for i, c in enumerate(cells):
    box(ax, 4 + i * 21, 44, 19, 10, 'sujet', label=c)
text(ax, 44, 38, 'modulo 2', 'varie', 's')
for i in range(4):
    arrow(ax, (13.5 + i * 21, 43), (13.5 + i * 21, 33), 'varie')
new = [('sujet', r'$x^4$'), ('varie', r'$0$'), ('sujet', r'$x$'), ('sujet', r'$1$')]
for i, (r, c) in enumerate(new):
    box(ax, 4 + i * 21, 22, 19, 10, r, label=c, dash=(i == 1))
text(ax, 44, 15, r'$-2$ = 0 modulo 2 : le terme disparaît', 'varie', 's')
box(ax, 4, 2, 80, 9, 'resultat', label=r'2 ne divise pas 1 : $x^4+x+1$')
save(fig, '54-258')
