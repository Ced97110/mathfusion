import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
sw = 76 / 28
for k in range(28):
    box(ax, 6 + k * sw, 24, sw, 8, 'sujet' if k == 0 else 'autre', r=0.2, lw=0.4)
box(ax, 6, 6, sw, 8, 'sujet', r=0.2, lw=0.4)
text(ax, 44, 38, r'$SL_{4}(\mathbb{F}_{2})$ : 20 160', 'autre', 's')
text(ax, 10 + sw, 10, r'$Sp_{4}(\mathbb{F}_{2})$ : 720', 'sujet', 's', ha='left')
text(ax, 62, 17.5, '28 fois plus grand', 'varie', 's')
save(fig, '75-128')
