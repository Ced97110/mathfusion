import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for y, a, b, c, ex, tx in [(32, '2', '3', '2', r'$\times2$', r'$12=6\times2$'), (10, '2', '2', '3', r'$\times3$', r'$12=4\times3$')]:
    r1 = 'sujet' if y == 32 else 'autre'
    box(ax, 4, y, 10, 8, r1, label=a); box(ax, 16, y, 10, 8, r1, label=b); box(ax, 28, y, 10, 8, 'varie', label=c)
    brace(ax, 4, 26, y, r1, r'$6$' if y == 32 else r'$4$'); brace(ax, 28, 38, y, 'varie', ex)
    text(ax, 64, y + 4, tx, 'resultat', 'm')
save(fig, '21-068')
