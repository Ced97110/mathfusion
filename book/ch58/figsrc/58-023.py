import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# (5, 4) comme somme : avec M1 et M2 une seule façon ; avec M1 et M deux façons
text(ax, 44, 61, r'$(5,\ 4) = \ldots + \ldots$', 'encre', 'm', weight='bold')
text(ax, 21, 52, r'$M_1 \oplus M_2$', 'sujet', 'm', weight='bold')
text(ax, 66, 52, r'$M_1 + M$', 'fixe', 'm', weight='bold')
line(ax, [(44, 8), (44, 56)], 'fixe', lw=0.5, dash=True)
def row(x, y, a, b, ra, rb):
    box(ax, x, y, 15, 9, ra, label=a, size='s')
    text(ax, x + 17.2, y + 4.5, '+', 'encre', 'm')
    box(ax, x + 19.5, y, 15, 9, rb, label=b, size='s')
row(4, 34, '(5, 0)', '(0, 4)', 'sujet', 'autre')
box(ax, 6, 14, 32, 9, 'resultat', label='une seule façon', size='s', weight='bold')
row(49, 38, '(5, 0)', '(0, 4)', 'sujet', 'fixe')
row(49, 26, '(0, 0)', '(5, 4)', 'sujet', 'fixe')
box(ax, 51, 8, 32, 9, 'limite', label='deux façons', size='s', weight='bold')
save(fig, '58-023')
