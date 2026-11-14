import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 23, 57, r'$q$', 'sujet', 'l')
text(ax, 61, 57, r'$p^m$', 'autre', 'l')
rows = [(4, r'$2^2$'), (8, r'$2^3$'), (9, r'$3^2$'), (256, r'$2^8$')]
for i, (q, s) in enumerate(rows):
    y = 41 - 12 * i
    box(ax, 14, y, 18, 9, 'sujet', label=str(q))
    text(ax, 42, y + 4.5, '=', 'encre', 'l')
    box(ax, 52, y, 18, 9, 'autre', label=s)
save(fig, '67-048')
