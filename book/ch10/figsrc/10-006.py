import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
y = 34; x0, x1 = 4, 80
f = lambda v: x0 + v / 1000 * (x1 - x0)
numberline(ax, x0, x1, y, 0, 1000, 100, labels=False, arrow_right=False)
disc(ax, f(90), y, 1.6, 'limite'); disc(ax, f(900), y, 1.6, 'resultat'); disc(ax, f(1000), y, 1.6, 'sujet')
text(ax, 3, y + 8, 'collègue : 90', 'limite', 'm', ha='left')
text(ax, f(900) - 1, y + 8, 'exact : 900', 'resultat', 'm', ha='right')
text(ax, f(1000) + 3, y - 14, r'attendu : 40 $\times$ 25 = 1 000', 'sujet', 'm', ha='right')
arrow(ax, (f(90), y - 4), (f(900), y - 4), 'limite')
text(ax, (f(90) + f(900)) / 2, y - 8, 'très éloigné de 1 000', 'limite', 's')
arrow(ax, (f(900) + 1, y + 4), (f(1000) - 1, y + 4), 'resultat')
text(ax, f(1000), y + 8, 'proche', 'resultat', 's', ha='right')
save(fig, '10-006')
