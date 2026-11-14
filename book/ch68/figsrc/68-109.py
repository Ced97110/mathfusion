import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
X = [16 + 10 * c for c in range(4)]
text(ax, 6, 48, '$H$', 'sujet', 'm')
text(ax, 6, 34, '$x$', 'autre', 'm')
for c, x in enumerate(X):
    box(ax, x, 44, 9, 8, 'sujet', label='1')
    box(ax, x, 30, 9, 8, 'autre', label='0111'[c])
    arrow(ax, (x + 4.5, 43.5), (x + 4.5, 38.5), 'varie')
brace(ax, 16, 55, 30, 'varie', label='0 + 1 + 1 + 1')
arrow(ax, (35.5, 17), (35.5, 11), 'varie')
text(ax, 35.5, 6, r'$Hx=1$ car $1+1=0$', 'resultat', 'm')
save(fig, '68-109')
