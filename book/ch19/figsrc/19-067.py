import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for x0, role, t, pt, a, b in [(4, 'sujet', '1er point', '(2, 5)', r'$x_1 = 2$', r'$y_1 = 5$'),
                              (46, 'autre', '2e point', '(6, 13)', r'$x_2 = 6$', r'$y_2 = 13$')]:
    box(ax, x0, 18, 38, 46, role)
    text(ax, x0 + 19, 57, t, role, 'm', weight='bold')
    text(ax, x0 + 19, 46, pt, role, 'l')
    text(ax, x0 + 19, 34, a, role, 'l')
    text(ax, x0 + 19, 24, b, role, 'l')
box(ax, 14, 2, 60, 11, 'fixe', label='petit chiffre : le numéro', size='m')
save(fig, '19-067')
