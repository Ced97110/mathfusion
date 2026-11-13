import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
k, x = 0.65, 6
text(ax, 6, 48, 'estimée', 'sujet', 's', ha='left'); text(ax, 82, 48, '100', 'sujet', 'm', ha='right', weight='bold')
for d in (10, 20, 30, 40):
    box(ax, x, 34, d * k, 9, 'sujet', label=str(d), size='s', r=0.3); x += d * k
x = 6
text(ax, 6, 24, 'vraie', 'sujet', 's', ha='left'); text(ax, 82, 24, '116', 'sujet', 'm', ha='right', weight='bold')
for d in (10, 20, 30, 40):
    box(ax, x, 10, d * k, 9, 'sujet', r=0.3); x += d * k
    box(ax, x, 10, 4 * k, 9, 'varie', label='4', size='s', r=0.3); x += 4 * k
text(ax, 44, 3.5, r'restes perdus : $E=-16$', 'varie', 's')
save(fig, '10-083')
