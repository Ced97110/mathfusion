import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [('0, 4, 8', '0', True), ('1, 5, 9', '1', False), ('2, 6, 10', '2', True), ('3, 7, 11', '3', False)]
text(ax, 14, 56, r'$H$ : pairs', 'sujet', 'm')
for k, (a, p, hit) in enumerate(rows):
    y = 43 - k * 11
    if hit:
        box(ax, 5, y - 4.5, 30, 9, 'sujet', fill=True, dash=False)
        text(ax, 20, y, a, 'sujet', 'm')
        arrow(ax, (30, y), (60, y), 'varie', lw=1.0)
        disc(ax, 68, y, 4.5, 'resultat', label=p, size='m')
    else:
        text(ax, 20, y, a, 'fixe', 's')
        disc(ax, 68, y, 4.5, 'fixe', fill=False, label=p, size='m')
text(ax, 45, 49, r'$f$', 'varie', 'm')
box(ax, 59, 6, 18, 44, 'resultat', fill=False, dash=True)
text(ax, 68, 56, r'$f(H)$', 'resultat', 'm')
save(fig, '48-037')
