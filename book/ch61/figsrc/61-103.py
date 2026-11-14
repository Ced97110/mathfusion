import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 2, 44, r'$K$ sur $F$', 'sujet', 's', ha='left')
text(ax, 2, 20, r'$E$ sur $K$', 'autre', 's', ha='left')
for x, s in zip([24, 40], [r'$v_1=1$', r'$v_2=\sqrt{2}$']):
    box(ax, x, 38, 14, 12, 'sujet', label=s, size='s')
for i, (x, s) in enumerate(zip([24, 40, 56, 72], [r'$w_1=1$', r'$w_2=\sqrt{3}$', '…', r'$w_m$'])):
    box(ax, x, 14, 14, 12, 'autre', label=s, size='s', dash=(i >= 2))
brace(ax, 24, 86, 12, 'autre', label=r'$m$ briques de $E$ sur $K$')
save(fig, '61-103')
