import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 11, 48, 'totaux', 'sujet', 's')
for i, g in enumerate([12, 19, 27]):
    box(ax, 22 + 22 * i, 43, 18, 10, 'sujet', label=str(g))
text(ax, 11, 14, 'points', 'resultat', 's')
box(ax, 44, 9, 18, 10, 'resultat', label='7')
box(ax, 66, 9, 18, 10, 'resultat', label='8')
arrow(ax, (53, 43), (53, 20), 'varie'); arrow(ax, (75, 43), (75, 20), 'varie')
text(ax, 44, 31, '19 − 12', 'varie', 's', ha='right')
text(ax, 66, 31, '27 − 19', 'varie', 's', ha='right')
text(ax, 50, 3, 'entiers, sans division', 'resultat', 's')
save(fig, '80-272')
