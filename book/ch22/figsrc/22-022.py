import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [('1,4', '1,9', '6'), ('1,41', '1,988', '1'), ('1,414', '1,99939', '6')]
xr = 76; cw = 6.5
text(ax, xr - cw / 2, 56, 'jamais 0', 'varie', 's')
for i, (a, b, c) in enumerate(rows):
    y = 41 - i * 12
    wb = 2.6 * len(b) + 3
    text(ax, 8, y + 4, a + ' au carré', 'sujet', 's', ha='left')
    box(ax, xr - cw - wb - 1, y, wb, 8, 'fixe', label=b, size='s', r=0.4)
    box(ax, xr - cw, y, cw, 8, 'varie', label=c, size='s', r=0.4)
y = 4
text(ax, 8, y + 4, 'et 2 s\'écrit', 'resultat', 's', ha='left')
box(ax, xr - 24, y, 24, 8, 'resultat', label='2,000…', size='s', r=0.4)
save(fig, '22-022')
