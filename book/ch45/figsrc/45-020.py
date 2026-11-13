import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = numberline(ax, 8, 70, 24, 0, 5, arrow_right=False, size='m')
arrow(ax, (f(0), 26), (f(3), 26), 'varie', curve=-0.35); text(ax, f(1.5), 38, '3 quarts', 'varie', 's')
arrow(ax, (f(3), 26), (f(5), 26), 'autre', curve=-0.4); text(ax, f(4), 35, '2 quarts', 'autre', 's')
arrow(ax, (f(5), 20), (f(1), 20), 'resultat', curve=-0.4)
text(ax, f(3), 7.5, r'5 quarts = 4 + 1 : retour sur 1', 'resultat', 's')
text(ax, 44, 55, r'$r_3\circ r_2=r_{3+2}=r_1$', 'encre', 'l')
save(fig, '45-020')
