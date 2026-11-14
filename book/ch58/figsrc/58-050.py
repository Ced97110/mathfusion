import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 56, r'$e_i$', 'sujet', 24)
text(ax, 66, 56, r'$i$ : le numéro', 'varie', 's', ha='left')
cw, ch = 11.0, 8.0
sacs = ['(1, 0, 0)', '(0, 1, 0)', '(0, 0, 1)']
for k in range(3):
    xc = 7 + k * 28
    box(ax, xc, 22, 22, 10, 'sujet', label=r'$e_%d$' % (k + 1), r=0.6)
    text(ax, xc + 11, 17, sacs[k], 'fixe', 's')
    arrow(ax, (44, 48), (xc + 11, 33), 'fixe', lw=0.8)
    if k < 2: arrow(ax, (xc + 23, 27), (xc + 27, 27), 'varie', lw=1.0)
text(ax, 44, 6, 'base standard : dans cet ordre', 'encre', 's')
save(fig, '58-050')
