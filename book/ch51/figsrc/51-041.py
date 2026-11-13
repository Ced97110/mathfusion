import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
disc(ax, 5, 63, 1.7, 'sujet'); text(ax, 9, 63, '$b$ = 4', 'sujet', 's', ha='left')
disc(ax, 26, 63, 1.7, 'varie'); text(ax, 30, 63, '$c$ = 5', 'varie', 's', ha='left')
text(ax, 86, 63, '$a$ = 3 sachets', 'fixe', 's', ha='right')
for i in range(3):
    bx = 2 + i * 28.5
    box(ax, bx, 31, 26, 24, 'fixe')
    for n, y, role in ((4, 48, 'sujet'), (5, 39, 'varie')):
        for k in range(n):
            disc(ax, bx + 13 + (k - (n - 1) / 2) * 4.4, y, 1.7, role)
brace(ax, 2, 28, 29, 'fixe', label='4 + 5')
box(ax, 2, 3, 41, 15, 'sujet'); text(ax, 22.5, 14.5, 'par sachet', 'sujet', 's'); text(ax, 22.5, 8, r'$3\times(4+5)=27$', 'encre', 'm')
box(ax, 45, 3, 41, 15, 'varie'); text(ax, 65.5, 14.5, 'par couleur', 'varie', 's'); text(ax, 65.5, 8, r'$3\times4+3\times5=27$', 'encre', 'm')
save(fig, '51-041')
