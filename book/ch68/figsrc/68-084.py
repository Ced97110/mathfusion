import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
y = 34
f = numberline(ax, 8, 68, y, 0, 3, 1, arrow_right=True)
poly(ax, [(f(1), y + 1.5), (f(2), y + 1.5), (f(2), y + 5.5), (f(1), y + 5.5)], 'varie')
disc(ax, f(0), y, 2.4, 'sujet')
disc(ax, f(3), y, 2.4, 'autre')
text(ax, f(0), y + 9, r'$c=000$', 'sujet', 's')
text(ax, f(3), y + 9, '111', 'autre', 's')
text(ax, (f(1) + f(2)) / 2, y + 9, r'$r$ : 100 ou 110', 'varie', 's')
brace(ax, f(0), f(3), 25, 'fixe', label=r'aucun autre mot du code à moins de $d=3$', down=True)
text(ax, 44, 9, r'$r\notin C$ : ni $c$ ni 111', 'resultat', 'm')
save(fig, '68-084')
