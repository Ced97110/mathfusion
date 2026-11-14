import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 60, r'on remplace $x$ par 3', 'sujet', 'm')
box(ax, 2, 42, 30, 10, 'fixe', label=r'$x^5-1=242$')
box(ax, 35, 42, 28, 10, 'varie', label=r'$\div\ (x-1)=2$')
box(ax, 66, 42, 20, 10, 'resultat', label=r'$=121$')
arrow(ax, (63, 47), (66, 47), 'varie')
terms = [(r'$x^4$', 81), (r'$x^3$', 27), (r'$x^2$', 9), (r'$x$', 3), ('1', 1)]
for i, (t, v) in enumerate(terms):
    x = 3 + i * 17
    box(ax, x, 14, 15, 14, 'resultat', label=t + '\n' + str(v), r=0.6)
brace(ax, 3, 3 + 4 * 17 + 15, 12, 'fixe', label='81 + 27 + 9 + 3 + 1 = 121')
arrow(ax, (76, 41), (76, 29.5), 'resultat')
save(fig, '66-047')
