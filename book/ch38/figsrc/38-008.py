import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
# voie 1 : formule apprise
box(ax, 4, 46, 36, 10, 'fixe', label='formule à retenir', size='s')
text(ax, 22, 41, 'apprise par cœur', 'fixe', 's')
text(ax, 62, 51, 'ou bien', 'encre', 'm')
# voie 2 : triangle redessiné puis calcul
A, B, P = (6, 12), (28, 12), (22, 32)
poly(ax, [A, B, P], 'sujet')
text(ax, A[0] - 1, 7, '$A$', 'sujet', 's')
text(ax, B[0] + 1, 7, '$B$', 'sujet', 's')
text(ax, P[0], 36.5, '$P$', 'sujet', 's')
text(ax, 17, 1.8, 'triangle redessiné', 'sujet', 's')
arrow(ax, (34, 22), (46, 22), 'varie')
box(ax, 47, 14, 38, 16, 'resultat', label='calcul refait', size='s')
text(ax, 66, 8, 'loi des sinus / cosinus', 'resultat', 's')
save(fig, '38-008')
