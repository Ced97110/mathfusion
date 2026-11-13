import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 4, 20, 26, 16, 'autre', label='')
text(ax, 17, 31, 'sinus', 'autre')
text(ax, 17, 25, '0,5', 'autre', 'l')
for i, a in enumerate(['30°', '150°', '390°']):
    y = 38 - i * 14 - 4
    box(ax, 58, y + 4 - 4 + 0, 24, 10, 'sujet', label=a)
    arrow(ax, (31, 28), (57, y + 5), 'varie')
text(ax, 44, 52, 'quel angle ?', 'varie', 'l')
text(ax, 44, 4, '3 angles, même sinus', 'resultat', 's')
save(fig, '33-010')
