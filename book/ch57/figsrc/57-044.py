import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 9, 54, 'départ', 'sujet', 's')
text(ax, 41, 54, r"$\zeta$ d'abord : tripler", 'varie', 's')
text(ax, 75, 54, r'$\eta$ ensuite : doubler', 'varie', 's')
for y, x, a, b in [(32, 4, 12, 24), (14, 5, 15, 30)]:
    box(ax, 2, y, 14, 10, 'sujet', label=str(x))
    box(ax, 32, y, 18, 10, 'varie', label=str(a))
    box(ax, 64, y, 22, 10, 'resultat', label=str(b))
    arrow(ax, (16.5, y + 5), (31.5, y + 5), 'varie')
    arrow(ax, (50.5, y + 5), (63.5, y + 5), 'varie')
text(ax, 44, 5, 'chaque fois : 6 fois le départ', 'resultat', 's')
save(fig, '57-044')
