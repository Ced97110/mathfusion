import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
X = [14 + k * 14 for k in range(4)]
y = 44
for k in range(4): disc(ax, X[k], y, 3.2, 'sujet', label=str(k + 1), size='s')
disc(ax, 72, y, 3.2, 'fixe', fill=False, label='5', size='s')
for a, b in ((0, 1), (2, 3)):
    arrow(ax, (X[a] + 1, y + 4.2), (X[b] - 1, y + 4.2), 'varie', curve=-0.6, both=True)
brace(ax, X[0] - 3, X[3] + 3, y - 5, 'resultat', label=r'$\gamma=(1\,2)(3\,4)$ : paire', size='s')
text(ax, 72, y - 8, 'pas utilisé', 'fixe', 's')
text(ax, 44, 57, 'deux échanges, quatre objets', 'encre', 's')
box(ax, 3, 4, 40, 11, 'resultat', label=r'lemme $B$ : dès $n\geq3$', size='s')
box(ax, 46, 4, 39, 11, 'fixe', dash=True, label=r'$n\geq5$ : lemme suivant', size='s')
save(fig, '64-126')
