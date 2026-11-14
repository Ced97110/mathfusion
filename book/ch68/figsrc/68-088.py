import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
y = 36
f = numberline(ax, 8, 72, y, 0, 5, 1, arrow_right=False)
disc(ax, f(0), y, 2.4, 'sujet'); disc(ax, f(2), y, 2.4, 'varie'); disc(ax, f(5), y, 2.4, 'autre')
text(ax, f(0), y + 6, r'$c$', 'sujet', 'm')
text(ax, f(2), y + 6, r'$r$', 'varie', 'm')
text(ax, f(5), y + 6, r"$c'$", 'autre', 'm')
brace(ax, f(0), f(5), y + 11, 'fixe', label=r"$d(c,c')\geq d=5$", down=False)
brace(ax, f(0), f(2), y - 10, 'varie', label=r'$\leq t=2$', down=True)
brace(ax, f(2), f(5), y - 10, 'autre', label=r'$\geq d-t=3$', down=True)
text(ax, 44, 8, r"3 > 2 : $c$ est le plus proche", 'resultat', 'm')
save(fig, '68-088')
