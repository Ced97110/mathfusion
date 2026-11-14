import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
top = ['(5, 4)', '(2, 1)', '(7, 5)']
bot = ['« 1, 3 »', '« 1, 0 »', '« 2, 3 »']
xs = [2, 33, 64]
text(ax, 2, 57, 'stocks (éléments du module)', 'sujet', 's', ha='left')
text(ax, 2, 6, 'nouveaux noms (listes)', 'autre', 's', ha='left')
for x, a, b in zip(xs, top, bot):
    box(ax, x, 40, 22, 10, 'sujet', label=a)
    box(ax, x, 12, 22, 10, 'autre', label=b)
    arrow(ax, (x + 11, 40), (x + 11, 22), 'varie')
for x in (27, 58):
    pass
text(ax, 27.5, 45, '+', 'encre', 'l'); text(ax, 58.5, 45, '=', 'encre', 'l')
text(ax, 27.5, 17, '+', 'encre', 'l'); text(ax, 58.5, 17, '=', 'encre', 'l')
text(ax, 18, 31, 'renommer', 'varie', 's', ha='left')
save(fig, '58-062')
