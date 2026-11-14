import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
for cx in (14, 44):
    disc(ax, cx, 32, 10, 'sujet', fill=False, lw=1.1)
    text(ax, cx, 45, r'$A$', 'sujet', 'l')
    for dx, l in ((-5, 'a'), (5, 'b')): disc(ax, cx + dx, 32, 3, 'fixe', label='$' + l + '$')
text(ax, 29, 32, '+', 'varie', 'xl'); text(ax, 59, 32, '=', 'encre', 'xl')
disc(ax, 74, 32, 10, 'resultat', fill=False, lw=1.1)
text(ax, 74, 32, r'$\varnothing$', 'resultat', 'xl')
text(ax, 29, 14, r'$a$ et $b$ : dans les deux', 'fixe', 's')
text(ax, 74, 14, 'aucun élément', 'resultat', 's')
save(fig, '80-315')
