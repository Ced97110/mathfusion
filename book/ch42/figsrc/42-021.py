import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
rows = [(42, ['gourde', 'carte', 'lampe']), (28, ['livre 1', 'livre 2', 'livre 3']), (14, ['1', '2', '3'])]
for yc, labs in rows:
    for x, t in zip([3, 19, 35], labs):
        box(ax, x, yc - 4.5, 14, 9, 'sujet', label=t, size='s')
    arrow(ax, (51, yc), (62, 28 + (yc - 28) * 0.45), 'varie')
box(ax, 62, 17, 22, 22, 'resultat', label='8 sacs', size='m')
text(ax, 73, 11, 'toujours', 'resultat', 's')
save(fig, '42-021')
