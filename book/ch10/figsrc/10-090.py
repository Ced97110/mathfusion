import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = lambda v: 14 + (v - 21.0) / 0.1 * 60
y = 28
line(ax, [(8, y), (80, y)], 'fixe')
for v in (21.0, 21.1): line(ax, [(f(v), y - 3), (f(v), y + 3)], 'fixe', lw=1.0)
disc(ax, f(21.0), y, 1.5, 'resultat')
disc(ax, f(21.04), y, 1.5, 'sujet')
text(ax, f(21.0), y - 6, '21,0 (lu)', 'resultat', 's'); text(ax, f(21.1), y - 6, '21,1', 'fixe', 's')
text(ax, f(21.04), y - 15, 'vraie : 21,04', 'sujet', 's')
arrow(ax, (f(21.04), y - 12.5), (f(21.04), y - 2.6), 'sujet', lw=0.7)
brace(ax, f(21.0) + 1, f(21.04) - 1, y + 5, 'varie', '0,04', down=False)
brace(ax, f(21.04) + 1, f(21.1) - 1, y + 5, 'fixe', '0,06', down=False)
text(ax, 44, 46, 'on lit le trait le plus proche', 'encre', 's')
save(fig, '10-090')
