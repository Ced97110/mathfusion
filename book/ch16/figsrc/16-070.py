import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for i in range(5):
    box(ax, 10 + i * 14, 40, 12, 9, 'sujet', label=r'$x$')
brace(ax, 10, 76, 50, 'fixe', label='35 g', down=False)
arrow(ax, (30, 38), (30, 20), 'varie')
text(ax, 22, 29, '÷ 5', 'varie', 'l')
arrow(ax, (58, 20), (58, 38), 'autre')
text(ax, 66, 29, '× 5', 'autre', 'l')
box(ax, 20, 8, 48, 10, 'resultat', label=r'$x=7$ g')
save(fig, '16-070')
