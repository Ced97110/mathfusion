import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
y, h, cw = 22, 9, 8.0
box(ax, 4, y, 10, h, 'sujet', label='z', weight='bold')
arrow(ax, (15, y + h / 2), (24, y + h / 2), 'varie', lw=1.2)
text(ax, 19.5, y + h + 3.5, '× b', 'varie', 's')
labels = ['0', 'z', '2z', '3z', '4z']
x0 = 26
for i, s in enumerate(labels):
    box(ax, x0 + i * cw, y, cw, h, 'sujet' if i else 'fixe', r=0.3, label=s, size='s')
text(ax, x0 + 5 * cw + 3, y + h / 2, '…', 'sujet', 'l')
brace(ax, x0, x0 + 5 * cw, y - 1.5, 'sujet', label='Dz : tous les b·z', down=True, depth=2.2)
text(ax, 44, 46, 'b est pris dans D', 'fixe', 's')
save(fig, '59-100')
