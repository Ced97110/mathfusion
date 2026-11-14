import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, 'deux règles, selon le nombre', 'encre', 's')
text(ax, 9, 26, r'$|a|=$', 'sujet', 'l')
line(ax, [(20, 12), (18.5, 12), (18.5, 24), (17.5, 26), (18.5, 28), (18.5, 40), (20, 40)], 'sujet')
for y, expr, cond, ex in [(32, r'$a$', r'si $a\geq 0$', r'$|8|=8$'), (8, r'$-a$', r'si $a<0$', r'$|-3|=3$')]:
    box(ax, 23, y, 16, 12, 'sujet', label=expr, size='l')
    box(ax, 42, y, 23, 12, 'fixe', label=cond, size='m')
    text(ax, 76, y + 6, ex, 'resultat', 'm')
save(fig, '13-044')
