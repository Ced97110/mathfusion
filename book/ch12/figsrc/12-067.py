import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
cw = 9; x0 = 26
text(ax, 2, 38.5, 'naturels', 'sujet', 'm', ha='left')
text(ax, 2, 22.5, 'entiers', 'sujet', 'm', ha='left')
box(ax, x0, 34, cw - 1, 9, 'fixe', fill=False, dash=True)
box(ax, x0, 18, cw - 1, 9, 'varie', label='0')
for c in range(1, 5):
    box(ax, x0 + c * cw, 34, cw - 1, 9, 'sujet', label=str(c))
    box(ax, x0 + c * cw, 18, cw - 1, 9, 'sujet', label=str(c))
text(ax, x0 + 5 * cw + 3, 38.5, '…', 'sujet', 'l')
text(ax, x0 + 5 * cw + 3, 22.5, '…', 'sujet', 'l')
text(ax, x0, 6, 'seule différence : 0', 'varie', 's', ha='left')
arrow(ax, (x0 + 4, 8.5), (x0 + 4, 17.3), 'varie')
save(fig, '12-067')
