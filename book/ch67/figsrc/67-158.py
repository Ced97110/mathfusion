import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 16, 65, r'racines de $f$', 'sujet')
text(ax, 71, 65, r'racines de $f_3$', 'resultat')
for y, a, b in [(46, r'$i$', r'$\psi(i)$'), (28, r'$-i$', r'$\psi(-i)$')]:
    box(ax, 4, y, 24, 10, 'sujet', label=a)
    box(ax, 58, y, 26, 10, 'resultat', label=b)
    arrow(ax, (28, y + 5), (58, y + 5), 'varie')
    text(ax, 43, y + 8.5, r'$\psi$', 'varie')
text(ax, 44, 20, 'deux images différentes', 'resultat')
text(ax, 44, 11, r'$f=\prod(x-r_i)$', 'fixe')
text(ax, 44, 4, r'$f_3=\prod(x-\psi(r_i))$', 'fixe')
save(fig, '67-158')
