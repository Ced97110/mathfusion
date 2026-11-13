import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 53, r'$D^*$ = D sans 0', 'encre', 'm')
text(ax, 3, 34.5, 'D = ℤ', 'sujet', 'm', ha='left')
text(ax, 3, 14.5, r'$D^*$', 'sujet', 'm', ha='left')
labs = ['−2', '−1', '0', '1', '2']
for i, s in enumerate(labs):
    box(ax, 24 + i * 12, 30, 10, 9, 'fixe' if s == '0' else 'sujet', label=s)
    if s == '0':
        box(ax, 24 + i * 12, 10, 10, 9, 'fixe', fill=False, dash=True)
    else:
        box(ax, 24 + i * 12, 10, 10, 9, 'sujet', label=s)
arrow(ax, (53, 29), (53, 20.5), 'varie')
text(ax, 57, 24.5, 'on retire 0', 'varie', 's', ha='left')
save(fig, '56-021')
