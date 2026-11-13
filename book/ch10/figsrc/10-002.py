import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
y = 26; x0, x1 = 6, 76
f = numberline(ax, x0, x1, y, 0, 200, 50)
disc(ax, f(84), y, 1.5, 'sujet'); disc(ax, f(84.63), y, 2.6, 'resultat', fill=False)
disc(ax, f(184.63), y, 1.5, 'limite')
text(ax, f(84) - 1, y + 10, 'attendu 84', 'sujet', 'm', ha='right')
line(ax, [(f(84), y + 2), (f(84), y + 8)], 'sujet')
arrow(ax, (f(84), y + 3), (f(184.63), y + 3), 'limite', curve=-0.3)
text(ax, (f(84) + f(184.63)) / 2 + 3, y + 12, 'écart 100,63', 'limite', 'm')
text(ax, f(84.63), y - 12, 'écran 84,63 : écart 0,63', 'resultat', 'm')
line(ax, [(f(84.63), y - 3), (f(84.63), y - 9.5)], 'resultat')
text(ax, f(184.63), y - 12, 'écran 184,63', 'limite', 'm', ha='right')
save(fig, '10-002')
