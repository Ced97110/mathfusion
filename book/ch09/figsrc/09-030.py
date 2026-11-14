import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 22, 56, 'première quantité', 'sujet', 's'); text(ax, 62, 56, 'seconde', 'fixe', 's')
for i, (a, b) in enumerate([('36', '4'), ('28', '7'), ('15', '3')]):
    y = 38 - i * 14
    box(ax, 6, y, 32, 10, 'sujet', label=r'$a$ = ' + a, size='m')
    text(ax, 46, y + 5, '÷', 'encre', 'l')
    box(ax, 54, y, 16, 10, 'fixe', label=b, size='m')
text(ax, 44, 4, 'seuls les nombres changent', 'encre', 's')
save(fig, '09-030')
