import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
items = [(2, r'$5+3\sqrt{2}$', 'sujet'), (33, r'$5-3\sqrt{2}$', 'varie'), (64, r'$5+3\sqrt{2}$', 'sujet')]
for x, lab, role in items:
    box(ax, x, 28, 22, 14, role, label=lab)
for x in (25, 56):
    arrow(ax, (x, 35), (x + 7, 35), 'varie')
    text(ax, x + 3.5, 40, r'$\sigma$', 'varie', 'm')
arrow(ax, (75, 27), (13, 27), 'resultat', curve=-0.4)
text(ax, 44, 8, r'$\sigma\circ\sigma=1$', 'resultat', 'l')
save(fig, '63-015')
