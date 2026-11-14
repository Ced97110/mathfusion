import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# proportion mal écrite : les gallons en bas à gauche et en haut à droite
for cx, top, bot, rt, rb in [(18, '30 miles', '2 gallons', 'sujet', 'varie'), (70, '5 gallons', '? miles', 'varie', 'sujet')]:
    box(ax, cx - 13, 52, 26, 9, rt, label=top)
    line(ax, [(cx - 13, 49), (cx + 13, 49)], 'encre', lw=1.0)
    box(ax, cx - 13, 37, 26, 9, rb, label=bot)
text(ax, 44, 49, '=', 'encre', 'l')
text(ax, 44, 66, 'unités mal placées', 'limite', 's')
arrow(ax, (44, 33), (44, 25), 'varie')
text(ax, 44, 29, 'produit en croix', 'varie', 's', ha='left') if False else None
text(ax, 62, 29, 'produit en croix', 'varie', 's')
box(ax, 4, 11, 32, 9, 'sujet', label='miles × miles')
box(ax, 52, 11, 32, 9, 'varie', label='gallons × gallons')
text(ax, 44, 15.5, '=', 'limite', 'l')
text(ax, 44, 4.5, 'pas les mêmes choses', 'limite', 's')
save(fig, '09-065')
