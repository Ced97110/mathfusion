import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 23, 74, r'$S_4$ : résoluble', 'autre', 'm', weight='bold')
labs = [r'$S_4$ : 24', r'$A_4$ : 12', r'$V$ : 4', r'$\{e\}$ : 1']
for i, lab in enumerate(labs):
    y = 56 - i * 15
    box(ax, 8, y, 30, 9, 'autre', label=lab, size='s')
    if i < 3: arrow(ax, (23, y - 0.5), (23, y - 5.5), 'autre')
text(ax, 67, 74, r'$S_5$ : pas résoluble', 'sujet', 'm', weight='bold')
box(ax, 50, 56, 34, 9, 'sujet', label=r'$S_5$ : 120', size='s')
arrow(ax, (67, 55.5), (67, 50.5), 'sujet')
box(ax, 50, 41, 34, 9, 'sujet', label=r'$A_5$ : 60  (simple)', size='s')
arrow(ax, (67, 40.5), (67, 35.5), 'limite')
box(ax, 50, 26, 34, 9, 'limite', label=r'$\{e\}$ : 1, inatteignable', size='s', dash=True)
text(ax, 67, 20, r'$A_5$ non abélien : bloqué', 'limite', 's')
save(fig, '64-013')
