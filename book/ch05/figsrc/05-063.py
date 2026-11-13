import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 60, r'on suppose que $a$ existe', 'encre', 'm')
yb, hb = 24, 10
box(ax, 4, yb, 46, hb, 'resultat', label='plus petits : factorisés', size='s')
box(ax, 50, yb, 14, hb, 'limite', label=r'$a$', size='l')
box(ax, 64, yb, 20, hb, 'fixe', label='plus grands', size='s')
text(ax, 57, yb - 4, 'le plus petit sans', 'limite', 's')
disc(ax, 14, 46, 4.3, 'resultat', label=r'$a_1$'); disc(ax, 34, 46, 4.3, 'resultat', label=r'$a_2$')
arrow(ax, (54.5, yb + hb), (17.5, 49), 'varie', curve=-0.35)
arrow(ax, (57, yb + hb), (37.5, 49), 'varie', curve=-0.2)
text(ax, 73, 42, r'$a = a_1 \times a_2$', 'varie', 's')
text(ax, 44, 8, r'donc $a$ est factorisé : contradiction', 'limite', 's')
save(fig, '05-063')
