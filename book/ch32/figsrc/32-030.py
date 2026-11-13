import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 42, 44, 28, 14, 'fixe', label=r'$\sin^{-1}\,0{,}5$', size='m')
box(ax, 2, 44, 20, 14, 'sujet', label='30°', size='l'); arrow(ax, (41.5, 51), (22.5, 51), 'varie')
text(ax, 12, 63, 'angle principal', 'sujet', 's')
f = numberline(ax, 8, 74, 16, 0, 540, step=180)
for v, r in ((30, 'sujet'), (150, 'fixe'), (390, 'fixe'), (510, 'fixe')):
    disc(ax, f(v), 16, 2.0 if r == 'sujet' else 1.6, r); text(ax, f(v), 21, f'{v}°', r, 's')
arrow(ax, (12, 43.5), (f(30), 24.5), 'sujet')
text(ax, 52, 32, 'autres solutions', 'fixe', 's')
save(fig, '32-030')
