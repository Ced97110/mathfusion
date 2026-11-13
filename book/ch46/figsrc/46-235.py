import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'$4! = 4\times 3\times 2\times 1 = 24$', 'sujet', 'l')
for c, (k, lab) in enumerate(zip([4, 3, 2, 1], ['1re carte', '2e carte', '3e carte', '4e carte'])):
    cx = 12 + c * 21
    for j in range(k): box(ax, cx - 6, 12 + j * 7.5, 12, 6.5, 'sujet' if c == 0 else 'varie', lw=0.6, r=0.4)
    text(ax, cx, 6, lab, 'encre', 's')
    if c < 3: text(ax, cx + 10.5, 27, r'$\times$', 'encre', 'l')
save(fig, '46-235')
