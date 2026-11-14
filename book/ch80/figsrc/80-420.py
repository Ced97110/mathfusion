import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(58)
f = numberline(ax, 8, 74, 22, 0, 6, arrow_right=False)
box(ax, 4, 34, 40, 9, 'resultat', label=r"axiomes : $a\vee a=a$", size='s')
arrow(ax, (f(3), 34), (f(3), 25.5), 'resultat')
box(ax, 48, 46, 38, 9, 'limite', label=r"$\vee$ comme $+$ : $3\vee3=6$", size='s')
arrow(ax, (f(6), 46), (f(6), 25.5), 'limite')
disc(ax, f(3), 22, 1.6, 'resultat'); disc(ax, f(6), 22, 1.6, 'limite')
save(fig, '80-420')
