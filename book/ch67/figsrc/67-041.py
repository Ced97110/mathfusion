import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 30, 46, 28, 9, 'fixe', label=r'$\mathbb{Z}$')
arrow(ax, (44, 46), (44, 39.5), 'varie')
text(ax, 50, 43, r'$\varphi$', 'varie', 'm')
for i in range(6):
    hot = i in (2, 3)
    box(ax, 4 + 14 * i, 28, 12, 10, 'varie' if hot else 'sujet', label=str(i))
brace(ax, 4, 86, 26, 'sujet', label=r'image : 6 éléments, $p=6$')
box(ax, 14, 5, 60, 10, 'limite', label=r'$2\times3=0$ : pas un corps')
save(fig, '67-041')
