import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
pts = ['(0, 0)', '(4, 6)', '(6, 4)', '(10, 10)']
w, g, x0 = 16.0, 2.0, 4.0
for i, p in enumerate(pts):
    box(ax, x0 + i * (w + g), 34, w, 9, 'sujet', label=p, size='s')
text(ax, x0 + 4 * (w + g) + 3, 38.5, '…', 'fixe', 'l')
text(ax, 44, 52, 'points atteints : la liste ne finit pas', 'fixe', 's')
x1 = x0 + 4 * (w + g) + 8
brace(ax, x0, x1, 32, 'sujet', depth=2.4)
text(ax, 44, 19, r'$K$', 'sujet', 'xl', weight='bold')
text(ax, 44, 9, r'tous les $af_1+bf_2$, $a$ et $b$ entiers', 'sujet', 's')
save(fig, '59-005')
