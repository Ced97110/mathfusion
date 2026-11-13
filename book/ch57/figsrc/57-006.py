import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
cw, ch, cy = 14, 12, 18
xs = [2, 21, 40]
for x in xs:
    box(ax, x, cy, cw, ch, 'sujet', label='(2, 1)', size='s')
for x in (17.5, 36.5):
    text(ax, x + 1, cy + ch / 2, '+', 'varie', 'l', weight='bold')
text(ax, 58, cy + ch / 2, '=', 'varie', 'l', weight='bold')
box(ax, 65, cy, 21, ch, 'resultat', label='(6, 3)')
text(ax, 21, 40, '3 × (2, 1)', 'sujet', 'm')
text(ax, 23, 10, '2 + 2 + 2 = 6', 'encre', 's')
text(ax, 70, 10, '1 + 1 + 1 = 3', 'encre', 's')
save(fig, '57-006')
