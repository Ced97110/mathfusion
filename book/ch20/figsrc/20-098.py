import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
s, y0 = 25, 12
xs = [2 + i * 29.5 for i in range(3)]
poly(ax, [(xs[0], y0), (xs[0] + s, y0), (xs[0] + s, y0 + s), (xs[0], y0 + s)], 'fixe', fill=False)
poly(ax, [(xs[0], y0), (xs[0] + s, y0), (xs[0] + s, y0 + s)], 'sujet')
line(ax, [(xs[0], y0), (xs[0] + s, y0 + s)], 'sujet', lw=1.3)
poly(ax, [(xs[1], y0), (xs[1] + s, y0), (xs[1] + s, y0 + s), (xs[1], y0 + s)], 'resultat')
box(ax, xs[2], y0, s, s, 'limite', fill=False, dash=True)
text(ax, xs[0] + s / 2, y0 + s + 5, 'avec x et y', 'sujet', 's')
text(ax, (xs[1] + xs[2] + s) / 2, y0 + s + 5, 'sans x ni y', 'fixe', 's')
line(ax, [(xs[1], y0 + s + 2), (xs[2] + s, y0 + s + 2)], 'fixe')
text(ax, xs[0] + s / 2, y0 - 5, 'un demi-plan', 'sujet', 's')
text(ax, xs[1] + s / 2, y0 - 5, r'$0<5$ : tout', 'resultat', 's')
text(ax, xs[2] + s / 2, y0 - 5, r'$0<-3$ : rien', 'limite', 's')
save(fig, '20-098')
