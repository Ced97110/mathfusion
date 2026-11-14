import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, '« Le nombre −2 existe-t-il ? »', 'limite', 'm')
f = numberline(ax, 8, 70, 22, -3, 4)
for v in (0, 1, 2, 3, 4):
    disc(ax, f(v), 22, 1.6, 'sujet')
disc(ax, f(-2), 22, 1.8, 'varie', fill=False)
brace(ax, f(0), f(4), 14, 'sujet', label='entiers naturels')
box(ax, 4, 42, 44, 10, 'sujet', label='couples d’entiers naturels', size='s')
arrow(ax, (26, 41), (f(-2), 26), 'varie')
text(ax, f(-2) + 14, 32, 'on le fabrique', 'varie', 's')
save(fig, '13-085')
