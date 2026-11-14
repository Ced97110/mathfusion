import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
words = ['Un nombre', 'plus 4', 'est strictement\nplus grand que', '6']
syms = [r'$x$', r'$+\,4$', r'$>$', r'$6$']
ws = [19, 13, 26, 9]; gap = 4
x = (W - sum(ws) - gap * 3) / 2
for wd, sy, wi in zip(words, syms, ws):
    box(ax, x, 36, wi, 14, 'fixe', label=wd, size='s')
    box(ax, x, 8, wi, 14, 'sujet', label=sy, size='xl')
    arrow(ax, (x + wi / 2, 36), (x + wi / 2, 23), 'varie')
    x += wi + gap
text(ax, 44, 57, 'phrase', 'fixe', 'm')
text(ax, 44, 3, 'symboles', 'sujet', 'm')
save(fig, '12-113')
