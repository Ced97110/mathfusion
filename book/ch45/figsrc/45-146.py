import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
xs = [6, 26, 46]
for x in xs: box(ax, x, 20, 12, 12, 'sujet', label='2', size='l')
for x in (18.5, 38.5): text(ax, x + 0.5, 26, '+', 'encre', 'l')
text(ax, 61.5, 26, '=', 'encre', 'l')
box(ax, 68, 20, 14, 12, 'resultat', label='2', size='l')
brace(ax, 6, 58, 18, 'varie', label=r'$3a$ : 3 fois $a$', size='m')
text(ax, 75, 12, '6, reste 2', 'resultat', 's')
text(ax, 12, 37, r'$a=2$', 'sujet', 's'); text(ax, 52, 37, r'$a=2$', 'sujet', 's')
text(ax, 32, 37, r'$a=2$', 'sujet', 's')
save(fig, '45-146')
