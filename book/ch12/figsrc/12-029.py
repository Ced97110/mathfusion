import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for x, s, r in ((30, '3', 'encre'), (42, r'$\times$', 'encre'), (54, '$x$', 'encre')):
    text(ax, x, 50, s, r, 'l')
disc(ax, 42, 50, 5, 'varie', fill=False)
disc(ax, 54, 50, 5, 'sujet', fill=False)
text(ax, 42, 40, 'signe', 'varie', 's')
text(ax, 54, 40, 'lettre', 'sujet', 's') if False else None
text(ax, 54, 40, 'lettre', 'sujet', 's')
text(ax, 44, 61, 'deux croix presque pareilles', 'limite', 's')
arrow(ax, (44, 36), (44, 24), 'varie')
text(ax, 36, 14, '3', 'encre', 'l')
text(ax, 46, 14, '$x$', 'encre', 'l')
disc(ax, 46, 14, 5, 'sujet', fill=False)
text(ax, 70, 14, 'une seule croix', 'resultat', 's')
save(fig, '12-029')
