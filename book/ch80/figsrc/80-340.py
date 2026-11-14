import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(68)
text(ax, 18, 62, 'diviseur de 30', 'sujet', 'm')
text(ax, 67, 62, 'facteurs premiers', 'autre', 'm')
rows = [('1', r'$\emptyset$'), ('6', r'$\{2,3\}$'), ('10', r'$\{2,5\}$'), ('30', r'$\{2,3,5\}$')]
for i, (d, s) in enumerate(rows):
    y = 44 - 14 * i
    box(ax, 6, y, 24, 9, 'sujet', label=d)
    box(ax, 52, y, 30, 9, 'autre', label=s)
    arrow(ax, (31, y + 4.5), (51, y + 4.5), 'varie', both=True)
save(fig, '80-340')
