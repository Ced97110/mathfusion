import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
text(ax, 44, 43, r'$Sp_{2n}(F)$', 'encre', 'xl')
items = [('Sp', 'sujet', 'groupe symplectique'), (r'$2n$', 'varie', 'dimension'), (r'$F$', 'autre', 'corps')]
xs = [16, 44, 72]
for x, (s, r, lab) in zip(xs, items):
    box(ax, x - 9, 18, 18, 10, r, label=s, size='l')
    arrow(ax, (44 + (x - 44) * 0.3, 37), (x, 29.5), r)
text(ax, 16, 12, 'groupe', 'sujet', 's'); text(ax, 16, 7, 'symplectique', 'sujet', 's')
text(ax, 44, 12, 'dimension', 'varie', 's')
text(ax, 72, 12, 'corps', 'autre', 's')
save(fig, '75-055')
