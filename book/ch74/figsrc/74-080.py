import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
xs = [26, 38, 50, 62]
text(ax, 2, 46, 'frise', 'sujet', 's', ha='left'); text(ax, 2, 18, 'retournée', 'limite', 's', ha='left')
for i, x in enumerate(xs):
    text(ax, x, 46, 'bp'[i % 2], 'sujet', 'l'); text(ax, x, 18, 'pb'[i % 2], 'limite', 'l')
    arrow(ax, (x, 41), (x, 24), 'varie')
text(ax, 79, 35, 'réflexion', 'varie', 's'); text(ax, 79, 30.5, 'horizontale', 'varie', 's')
text(ax, 44, 7, 'pas une symétrie de la frise', 'limite', 'm')
save(fig, '74-080')
