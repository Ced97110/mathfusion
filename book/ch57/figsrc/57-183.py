import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 60, 'même classe  ⇒  même nombre x − 2y', 'encre', 'm')
rows = [(40, '(3 ; 0)', '(5 ; 1)', '3 − 0 = 3', '5 − 2 = 3'),
        (14, '(5 ; 2)', '(7 ; 3)', '5 − 4 = 1', '7 − 6 = 1')]
for y, a, b, ca, cb in rows:
    box(ax, 4, y, 20, 9, 'sujet', label=a)
    box(ax, 64, y, 20, 9, 'sujet', label=b)
    arrow(ax, (25, y + 4.5), (63, y + 4.5), 'varie', lw=1.2)
    text(ax, 44, y + 8.2, 'on ajoute (2 ; 1)', 'varie', 's')
    text(ax, 14, y - 4, ca, 'resultat', 's')
    text(ax, 74, y - 4, cb, 'resultat', 's')
    text(ax, 44, y - 4, '=', 'resultat', 'l', weight='bold')
save(fig, '57-183')
