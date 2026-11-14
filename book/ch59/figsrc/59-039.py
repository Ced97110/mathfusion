import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
rows = [((4, 6), r'$4x_1+6x_2=0$', 31), ((6, 4), r'$6x_1+4x_2=0$', 18)]
for vals, eq, y in rows:
    box(ax, 3, y, 32, 8, 'autre', label=eq)
    arrow(ax, (35.6, y + 4), (49.4, y + 4), 'varie')
    for j, v in enumerate(vals):
        box(ax, 50 + j * 9, y, 9, 8, 'sujet', label=str(v))
text(ax, 59, 44, r'$A$', 'sujet', 'l')
brace(ax, 50, 68, 17, 'sujet', label=r'$n=2$ colonnes')
text(ax, 79, 26, '$m=2$\nlignes', 'sujet', 's')
text(ax, 19, 44, 'deux relations', 'autre', 's')
save(fig, '59-039')
