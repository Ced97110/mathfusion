import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = numberline(ax, 8, 76, 12, -5, 5, labels=False, arrow_right=True)
box(ax, 28, 40, 32, 16, 'sujet'); text(ax, 44, 49, 't   0\n0   1', 'sujet', 'l'); 
pts = [(-3, 'varie', '−3'), (1, 'resultat', '1'), (5, 'varie', '5')]
for v, r, lab in pts:
    disc(ax, f(v), 12, 1.6, r); text(ax, f(v), 5, lab, r, 'm')
    arrow(ax, (44 + (f(v) - 44) * 0.3, 40), (f(v), 15), r)
disc(ax, f(0), 12, 1.6, 'limite', fill=False); text(ax, f(0), 5, '0', 'limite', 'm')
text(ax, 44, 59.5, 'det de cette matrice = t', 'varie', 's')
text(ax, 44, 30, 'tout t ≠ 0 est atteint', 'varie', 's')
text(ax, f(1) + 14, 20, 'noyau', 'resultat', 's') if False else None
save(fig, '48-136')
