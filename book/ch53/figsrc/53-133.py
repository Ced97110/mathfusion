import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(84)
labs = [r'$17^{1}\equiv17$', r'$17^{2}\equiv14$', r'$17^{4}\equiv31$', r'$17^{8}\equiv26$', r'$17^{16}\equiv16$']
calc = ['17² = 289 = 5 × 55 + 14', '14² = 196 = 3 × 55 + 31',
        '31² = 961 = 17 × 55 + 26', '26² = 676 = 12 × 55 + 16']
text(ax, 36, 72, 'chaque ligne = carré de la précédente', 'fixe', 's', ha='left')
for i, lab in enumerate(labs):
    y = 68 - 16 * i
    box(ax, 2, y, 30, 10, 'sujet', label=lab)
    if i < 4:
        arrow(ax, (17, y - 0.5), (17, y - 5.5), 'varie')
        text(ax, 36, y - 3, calc[i], 'varie', 's', ha='left')
save(fig, '53-133')
