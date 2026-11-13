import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
Y = [60, 48, 36, 24]
for xc, role, head, words in ((22, 'sujet', 'Français', ['zéro', 'un', 'deux', 'trois']),
                              (66, 'autre', 'Anglais', ['zero', 'one', 'two', 'three'])):
    text(ax, xc, 72, head, role, 'm', weight='bold')
    for y, w in zip(Y, words): box(ax, xc - 11, y - 3.5, 22, 7, role, label=w)
    for y in Y[:-1]: arrow(ax, (xc, y - 3.5), (xc, y - 8.5), 'fixe')
for y in Y: arrow(ax, (34, y), (54, y), 'varie', both=True)
text(ax, 44, 66, 'départ avec départ', 'varie', 's')
text(ax, 44, 30, 'suivant avec suivant', 'varie', 's')
text(ax, 44, 15, 'aucun oubli, aucun doublon', 'resultat', 's')
text(ax, 44, 7, 'mêmes, aux noms près', 'resultat', 'm', weight='bold')
save(fig, '01-041')
