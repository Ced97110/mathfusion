import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
rows = [(42, 'resultat', r'$3+(-5)$', r'$=-2$', 'bon : les deux gestes'),
        (23, 'limite', r'$-3+5$', r'$=2$', 'faux : signe de 3 changé'),
        (4, 'limite', r'$3-(-5)$', r'$=8$', 'faux : trait « moins » gardé')]
for y, r, e, v, note in rows:
    box(ax, 2, y, 20, 9, 'sujet', label=r'$3-5$')
    arrow(ax, (23, y + 4.5), (33, y + 4.5), 'varie')
    box(ax, 34, y, 28, 9, r, label=e)
    box(ax, 66, y, 20, 9, r, label=v)
    text(ax, 48, y + 12.2, note, r, 's')
save(fig, '13-067')
