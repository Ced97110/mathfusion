import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 22, 60, 'trace de A', 'sujet', 'm', weight='bold')
text(ax, 22, 51, '−1 + 0 + 4', 'sujet', 'm')
box(ax, 14, 28, 16, 14, 'sujet', label='3', size='l')
arrow(ax, (22, 48), (22, 43), 'sujet')
text(ax, 66, 60, 'racines de f = (λ − 1)³', 'autre', 'm', weight='bold')
for x in (52, 66, 80):
    disc(ax, x, 48, 5, 'autre', label='1', size='m')
arrow(ax, (66, 42), (66, 38), 'autre')
text(ax, 66, 34, '1 + 1 + 1 = 3', 'autre', 'm')
text(ax, 44, 34, '=', 'resultat', 'xl', weight='bold')
text(ax, 44, 16, 'comptée une fois : 1 ≠ 3', 'limite', 's')
save(fig, '60-209')
