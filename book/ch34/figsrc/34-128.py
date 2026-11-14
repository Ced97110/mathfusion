import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
rows = [(r'$\sin 2A$', r'2 $\times$ 3/5 $\times$ 4/5', '24/25'),
        (r'$\cos 2A$', r'16/25 − 9/25', '7/25'),
        (r'$\tan 2A$', r'(24/25) / (7/25)', '24/7')]
for i, (n, c, r) in enumerate(rows):
    y = 62 - i * 26
    box(ax, 2, y, 20, 14, 'sujet', label=n, size='m')
    box(ax, 28, y, 36, 14, 'varie', label=c, size='s')
    box(ax, 70, y, 16, 14, 'resultat', label=r, size='m')
    arrow(ax, (22, y + 7), (28, y + 7), 'fixe'); arrow(ax, (64, y + 7), (70, y + 7), 'varie')
text(ax, 44, 4, r'$\sin A=3/5,\ \cos A=4/5$', 'encre', 's')
save(fig, '34-128')
