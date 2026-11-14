import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# Klein group: 4 elements, all with x^2 = 1 ; in a field x^2 - 1 has at most 2 roots, so 2 of them do not fit
text(ax, 44, 65, r'Klein : 4 éléments, $x^2 = 1$', 'sujet', 'm')
text(ax, 22, 54, 'au plus 2 solutions', 'fixe', 's')
text(ax, 71, 54, 'en trop', 'limite', 's')
for k, x in enumerate([5, 25, 52, 70]):
    ok = k < 2
    box(ax, x, 30, 16, 18, 'fixe' if ok else 'limite', fill=False, dash=ok, lw=1.0)
    disc(ax, x + 8, 39, 3.6, 'sujet' if ok else 'limite')
brace(ax, 5, 87, 28, 'limite', label=r'4 solutions $> 2$ : impossible', size='s')
save(fig, '67-085')
