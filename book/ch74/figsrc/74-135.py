import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
x0, x1 = 12, 72; u = (x1-x0)/5
f = numberline(ax, x0, x1, 14, 0, 5, arrow_right=False)
text(ax, 80, 14, 'cm', 'fixe', 's')
box(ax, f(0), 38, 5*u, 5, 'sujet')
text(ax, f(2.5), 46.5, r'$|v| = 5$ cm', 'sujet', 'm')
box(ax, f(0), 26, 3.09*u, 5, 'resultat')
text(ax, f(1.55), 34.5, r'$|OQ| \approx 3{,}1$ cm', 'resultat', 'm')
text(ax, 44, 4, r'$2\cos 72^\circ \times 5 \approx 3{,}1 < 5$', 'resultat', 's')
save(fig, '74-135')
