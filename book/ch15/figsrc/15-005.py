import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for i in range(5):
    box(ax, 8 + 14 * i, 38, 12, 12, 'sujet' if i < 3 else 'varie', label=r'$x$', weight='bold')
brace(ax, 8, 48, 37, 'sujet', r'$3x$'); brace(ax, 50, 76, 37, 'varie', r'$2x$')
brace(ax, 8, 76, 26, 'resultat', r'$5x$', size='m')
for cx, p, t in ((15, 2, 10), (44, 3, 15), (73, 5, 25)):
    text(ax, cx, 9, f'x = {p} : {t} €', 'resultat', 's')
save(fig, '15-005')
