import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, oy, k = 14, 8, 7.5
P = lambda a, b: (ox + a * k, oy + b * k)
arrow(ax, P(-0.8, 0), P(4, 0), 'fixe', lw=0.6)
arrow(ax, P(0, -0.5), P(0, 7.4), 'fixe', lw=0.6)
line(ax, [P(-0.35, -0.7), P(3.3, 6.6)], 'sujet', lw=1.6)
arrow(ax, P(0, 0), P(1, 2), 'varie', lw=1.6)
for (a, b) in [(2, 4), (3, 6)]:
    disc(ax, *P(a, b), 1.2, 'sujet')
disc(ax, *P(0, 0), 1.2, 'sujet')
text(ax, P(1, 2)[0] + 2, P(1, 2)[1] - 2.5, '(1, 2)', 'varie', 's', ha='left')
text(ax, P(2, 4)[0] + 2, P(2, 4)[1] - 2.5, '(2, 4)', 'sujet', 's', ha='left')
text(ax, P(3, 6)[0] + 2, P(3, 6)[1] - 2.5, '(3, 6)', 'sujet', 's', ha='left')
text(ax, P(0, 0)[0] + 2.5, P(0, 0)[1] - 3, '(0, 0)', 'sujet', 's', ha='left')
box(ax, 54, 44, 32, 14, 'varie', label=r'un vecteur $v$', size='s')
box(ax, 54, 16, 32, 20, 'sujet', label=r'$\langle v\rangle$ : la droite' + '\n' + 'de ses multiples', size='s')
arrow(ax, (70, 44), (70, 36), 'varie', lw=1.2)
save(fig, '58-092')
