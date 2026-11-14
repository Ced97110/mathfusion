import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 42, 52, 'z', 'sujet', 'xl'); text(ax, 46.5, 56.5, 'n', 'varie', 'xl', weight='bold')
text(ax, 62, 52, '= z × … × z', 'sujet', 'm', ha='left')
arrow(ax, (46.5, 52), (46.5, 41), 'varie', lw=0.9)
text(ax, 8, 47, 'n compte les facteurs', 'varie', 's', ha='left')
# three factors for n = 3
x0, w, g = 10, 16, 8
for i in range(3):
    box(ax, x0 + i * (w + g), 22, w, 12, 'sujet', label='z', size='l')
    if i < 2: text(ax, x0 + i * (w + g) + w + g / 2, 28, '×', 'encre', 'l')
brace(ax, x0, x0 + 3 * w + 2 * g, 20, 'varie', label='n = 3 facteurs égaux à z', down=True, size='s')
text(ax, 44, 6, 'n est un entier : 1, 2, 3…', 'encre', 's')
save(fig, '39-076')
