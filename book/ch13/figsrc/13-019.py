import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
y = 28
f = numberline(ax, 10, 66, y, -3, 3, every=3, arrow_right=False)
disc(ax, f(3), y, 1.6, 'sujet'); disc(ax, f(-3), y, 1.6, 'autre'); disc(ax, f(0), y, 1.3, 'fixe')
brace(ax, f(0), f(3), y + 3, 'resultat', '3 pas', down=False)
brace(ax, f(-3), f(0), y + 3, 'resultat', '3 pas', down=False)
text(ax, f(0), 50, 'même distance', 'resultat', 'm', weight='bold')
arrow(ax, (f(0) - 1, y - 9), (f(-3) + 1, y - 9), 'varie')
arrow(ax, (f(0) + 1, y - 9), (f(3) - 1, y - 9), 'varie')
text(ax, f(0), 10, 'côtés contraires', 'varie', 'm', weight='bold')
save(fig, '13-019')
