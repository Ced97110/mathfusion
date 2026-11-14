import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xs = [18, 32, 44, 56, 70]
for x, t, r in zip(xs, ['(', r'$s$', ',', r'$t$', ')'], ['fixe', 'sujet', 'fixe', 'autre', 'fixe']):
    text(ax, x, 44, t, r, 'l', weight='bold')
brace(ax, 14, 74, 51, 'fixe', 'un seul couple', down=False)
box(ax, 20, 12, 24, 16, 'sujet', label='1re place :\ncolonne 2', size='s')
box(ax, 44, 12, 24, 16, 'autre', label='2e place :\nligne $b$', size='s')
arrow(ax, (32, 39), (32, 29), 'sujet'); arrow(ax, (56, 39), (56, 29), 'autre')
save(fig, '42-172')
