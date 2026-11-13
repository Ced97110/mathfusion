import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'$x^2 = 1$ et $y^2 = 1$ : les mots', 'sujet', 's')
words = [['1'], ['x', 'y'], ['xy', 'yx'], ['xyx', 'yxy'], ['xyxy', 'yxyx']]
cw = 15.5
for c, col in enumerate(words):
    cx = 6 + c * cw
    for r, w in enumerate(col):
        box(ax, cx, 56 - r * 11, 14, 8, 'sujet', label=w, size='s')
for c in range(4):
    arrow(ax, (6 + c * cw + 14.2, 60), (6 + (c + 1) * cw - 0.2, 60), 'fixe') if False else None
text(ax, 83, 56, '…', 'fixe', 'l')
text(ax, 44, 30, 'tous différents ? sans fin ?', 'limite', 'm', weight='bold')
box(ax, 8, 4, 72, 17, 'varie')
text(ax, 44, 15, 'la liste donne une idée', 'varie', 's')
text(ax, 44, 9, 'la preuve : une action', 'varie', 's')
save(fig, '49-304')
