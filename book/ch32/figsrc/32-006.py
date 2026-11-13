import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
X0, X1 = 20, 76
Y = lambda h: 8 + 10 * h
fx = lambda t: X0 + (X1 - X0) * t / 3
hh = lambda t: 2 + 2 * math.sin(math.radians(30 * t))
line(ax, [(X0, 8), (X0, 52)], 'fixe')
line(ax, [(X0, 8), (X1 + 4, 8)], 'fixe')
for h in (2, 3, 4):
    line(ax, [(X0 - 1, Y(h)), (X0 + 1, Y(h))], 'fixe')
    text(ax, X0 - 2.5, Y(h), f'{h} m', 'fixe', 'm', ha='right')
line(ax, [(X0, Y(3)), (X1 + 4, Y(3))], 'varie', dash=True)
ts = [3 * i / 60 for i in range(61)]
line(ax, [(fx(t), Y(hh(t))) for t in ts], 'sujet', lw=1.4)
disc(ax, fx(0), Y(2), 1.7, 'fixe')
disc(ax, fx(3), Y(4), 1.7, 'resultat')
text(ax, fx(0) + 2, 8 - 3.5, 'minuit', 'fixe', 's', ha='left')
text(ax, fx(3), 8 - 3.5, '3 h', 'fixe', 's')
text(ax, fx(0) + 3, Y(2) - 4, 'trop peu', 'fixe', 'm', ha='left')
text(ax, fx(3) - 3, Y(4) + 4, 'assez', 'resultat', 'm', ha='right')
text(ax, 66, Y(3) - 4.5, 'quelle heure ?', 'varie', 'm')
save(fig, '32-006')
