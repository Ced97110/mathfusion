import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
X = [14 + k * 14 for k in range(5)]
def swaps(y):
    for a, b in ((0, 1), (2, 3)):
        arrow(ax, (X[a] + 1, y + 4.2), (X[b] - 1, y + 4.2), 'varie', curve=-0.6, both=True)
# n = 4
text(ax, 44, 79, r'$n=4$ : $A_4$ non simple', 'limite', 's')
yt = 62
for k in range(4): disc(ax, X[k], yt, 3.2, 'sujet', label=str(k + 1), size='s')
disc(ax, X[4], yt, 3.2, 'limite', fill=False, label='5', size='s')
swaps(yt)
text(ax, 44, 54, r'$(1\,2)(3\,4)$ touche 1, 2, 3, 4 ; pas de 5', 'encre', 's')
# n = 5
text(ax, 44, 45, r'$n=5$ : $\beta=(3\,4\,5)$ existe', 'resultat', 's')
yb = 26
for k in range(5): disc(ax, X[k], yb, 3.2, 'sujet' if k < 4 else 'resultat', label=str(k + 1), size='s')
swaps(yb + 6)
y0 = yb - 3.4
arrow(ax, (X[2] + 1, y0), (X[3] - 1, y0), 'resultat', curve=0.5)
arrow(ax, (X[3] + 1, y0), (X[4] - 1, y0), 'resultat', curve=0.5)
arrow(ax, (X[4] - 1.5, y0), (X[2] + 1.5, y0), 'resultat', curve=-0.9)
save(fig, '64-111')
