import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 6, 78, 24, -12, 36, step=12, arrow_right=False)
for v in (-11, 13, 25):
    disc(ax, f(v), 24, 1.7, 'varie'); text(ax, f(v), 31, str(v).replace('-', '−'), 'varie', 's')
disc(ax, f(1), 24, 2.1, 'resultat'); text(ax, f(1), 31, '1', 'resultat', 'm', weight='bold')
brace(ax, f(0), f(11), 40, 'resultat', down=False, depth=1.6)
text(ax, f(5.5), 47, 'noms : 0, 1, …, 11', 'resultat', 's')
text(ax, 42, 11, 'même classe : −11, 1, 13, 25, …', 'varie', 's')
text(ax, 42, 4, 'on la nomme 1 : le plus petit positif', 'resultat', 's')
save(fig, '44-142')
