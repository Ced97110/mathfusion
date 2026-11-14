import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
y = 36
f = numberline(ax, 6, 78, y, 0, 11, step=1, every=2, arrow_right=False)
brace(ax, f(0), f(4), y + 3, 'sujet', r'$h_2 = 4$', down=False)
brace(ax, f(4), f(10), y + 3, 'autre', r'$h_3 = 6$', down=False)
text(ax, f(10), y + 9, r'$g = 10$', 'resultat', 's')
disc(ax, f(4), y, 2.4, 'sujet'); disc(ax, f(6), y, 2.4, 'autre'); disc(ax, f(10), y, 2.4, 'resultat')
arrow(ax, (f(10), y - 9), (f(6), y - 9), 'varie', curve=-0.5)
text(ax, f(8), y - 18, r'$h_3 = g - h_2 = 10 - 4$', 'varie', 's')
text(ax, 44, 7, r'6 est pair, donc dans $H_1$ ; et dans $H_3$', 'resultat', 's')
save(fig, '79-159')
