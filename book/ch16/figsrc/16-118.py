import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'$l = (P - 2w)\,/\,2$', 'sujet', 'l', weight='bold')
text(ax, 50, 58, r'moins 2$w$', 'varie', 's')
text(ax, 75, 58, 'divisé par 2', 'varie', 's')
rows = [(r'$P$=20, $w$=3', '20 − 6 = 14', '7'), (r'$P$=30, $w$=5', '30 − 10 = 20', '10'), (r'$P$=16, $w$=2', '16 − 4 = 12', '6')]
for i, (a, b, c) in enumerate(rows):
    y = 41 - i * 17
    box(ax, 2, y, 28, 11, 'fixe', label=a, size='s')
    arrow(ax, (30, y + 5.5), (35, y + 5.5), 'varie')
    box(ax, 35, y, 30, 11, 'varie', label=b, size='s')
    arrow(ax, (65, y + 5.5), (69, y + 5.5), 'varie')
    box(ax, 69, y, 17, 11, 'resultat', label=c, size='l')
save(fig, '16-118')
