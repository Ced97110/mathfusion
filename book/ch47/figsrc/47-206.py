import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
for x, v, r in [(2, '3', 'sujet'), (38, '7', 'varie'), (74, '3', 'resultat')]:
    box(ax, x, 26, 12, 11, r, label=v, size='l')
arrow(ax, (14.5, 31.5), (37.5, 31.5), 'encre'); arrow(ax, (50.5, 31.5), (73.5, 31.5), 'encre')
text(ax, 26, 43, 'coder', 'varie', 's', weight='bold'); text(ax, 62, 43, 'décoder', 'varie', 's', weight='bold')
text(ax, 26, 22, r'puissance 3 : 27', 'encre', 's'); text(ax, 26, 17, 'reste 7', 'encre', 's')
text(ax, 62, 22, r'puissance 3 : 343', 'encre', 's'); text(ax, 62, 17, 'reste 3', 'encre', 's')
text(ax, 44, 7, r'$3\times3=9=1+2\times4$ : Euler', 'resultat', 's')
save(fig, '47-206')
