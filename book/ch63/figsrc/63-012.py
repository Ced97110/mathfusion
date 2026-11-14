import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
rows = [(r'$a+b\sqrt{2}$', r'$a-b\sqrt{2}$'), (r'$5+3\sqrt{2}$', r'$5-3\sqrt{2}$'), (r'$4+0\sqrt{2}$', r'$4-0\sqrt{2}=4$')]
for i, (l, r) in enumerate(rows):
    y = 46 - 20 * i
    box(ax, 2, y, 34, 14, 'sujet', label=l)
    arrow(ax, (37, y + 7), (51, y + 7), 'varie')
    text(ax, 44, y + 11, r'$\sigma$', 'varie', 'm')
    box(ax, 52, y, 34, 14, 'resultat', label=r)
save(fig, '63-012')
