import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, 'un cas : 2 et 3', 'fixe', 'm')
box(ax, 8, 38, 14, 12, 'fixe', label='2', size='l'); box(ax, 30, 38, 14, 12, 'fixe', label='3', size='l')
text(ax, 68, 44, '(2 × 3) $v$', 'fixe', 'm')
for x in (8, 30):
    arrow(ax, (x + 7, 38), (x + 7, 26), 'varie')
box(ax, 8, 14, 14, 12, 'varie', label=r'$\alpha$', size='l'); box(ax, 30, 14, 14, 12, 'varie', label=r'$\beta$', size='l')
text(ax, 68, 20, r'$(\alpha\beta)\,v$', 'varie', 'm')
text(ax, 68, 32, 'une infinité\nde cas', 'varie', 's')
text(ax, 44, 5, r'$\alpha$ et $\beta$ : égaux ou non', 'varie', 's')
save(fig, '58-089')
