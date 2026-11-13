import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
for x, t in [(2, 'factoriser'), (31, 'garder le max'), (60, 'multiplier')]:
    text(ax, x + 13, 46, t, 'varie', 's')
arrow(ax, (28, 28), (32, 28), 'varie', lw=0.8); arrow(ax, (57, 28), (61, 28), 'varie', lw=0.8)
text(ax, 4, 35, r'$6$', 'sujet'); text(ax, 4, 20, r'$4$', 'autre')
box(ax, 8, 31.5, 7, 7, 'sujet', label='2', r=0.5); box(ax, 16, 31.5, 7, 7, 'fixe', label='3', r=0.5)
box(ax, 8, 16.5, 7, 7, 'autre', label='2', r=0.5); box(ax, 16, 16.5, 7, 7, 'autre', label='2', r=0.5)
for i, (s, r) in enumerate([('2', 'autre'), ('2', 'autre'), ('3', 'fixe')]):
    box(ax, 34 + 8 * i, 24, 7, 7, r, label=s, r=0.5)
box(ax, 61, 22, 25, 11, 'resultat', label=r'$2\times2\times3=12$', size='s')
save(fig, '21-067')
