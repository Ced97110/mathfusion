import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [('0, 4, 8', '0', True), ('1, 5, 9', '1', False), ('2, 6, 10', '2', True), ('3, 7, 11', '3', False)]
text(ax, 20, 56, r'$f^{-1}(H^{\prime})$', 'resultat', 'm')
for k, (a, p, hit) in enumerate(rows):
    y = 43 - k * 11
    if hit:
        box(ax, 5, y - 4.5, 30, 9, 'resultat', fill=False, dash=True)
        text(ax, 20, y, a, 'resultat', 'm')
        arrow(ax, (60, y), (30, y), 'varie', lw=1.0)
        disc(ax, 68, y, 4.5, 'sujet', label=p, size='m')
    else:
        text(ax, 20, y, a, 'fixe', 's')
        disc(ax, 68, y, 4.5, 'fixe', fill=False, label=p, size='m')
text(ax, 45, 49, 'retour', 'varie', 's')
box(ax, 59, 6, 18, 44, 'sujet', fill=False, dash=True)
text(ax, 68, 56, r'$H^{\prime}$', 'sujet', 'm')
save(fig, '48-038')
