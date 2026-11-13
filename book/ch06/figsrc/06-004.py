import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'fractio : « casser »', 'varie', 'l')
box(ax, 14, 38, 60, 8, 'sujet', label='unité = 1')
arrow(ax, (44, 36), (44, 27), 'varie')
text(ax, 50, 31.5, 'casser', 'varie', ha='left')
for j in range(4):
    box(ax, 13.5 + j * 16, 14, 13, 8, 'sujet')
brace(ax, 13.5, 74.5, 14, 'fixe', '4 morceaux égaux')
save(fig, '06-004')
