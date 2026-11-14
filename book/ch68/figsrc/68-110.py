import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
labs = ['00', '01', '10', '11']
X = [44 + 11 * c for c in range(4)]
Y = [64 - 11 * r for r in range(4)]
text(ax, 44, 86, r'$C$ = mots $x$ avec $Hx = 0$', 'encre', 'm', weight='bold')
text(ax, 44, 79, 'mot de 4 bits : lignes puis colonnes', 'fixe', 's')
for c in range(4): text(ax, X[c], 72.5, labs[c], 'fixe', 's')
for r in range(4): text(ax, 26, Y[r], labs[r], 'fixe', 's')
for r in range(4):
    for c in range(4):
        a, b = labs[r], labs[c]
        h1 = (sum(map(int, a + b)) % 2 == 0)
        h2 = (a[0] == a[1])
        disc(ax, X[c], Y[r], 2.6, 'sujet' if h1 else 'fixe', fill=h1)
        if h2: disc(ax, X[c], Y[r], 4.2, 'autre', fill=False)
assert sum(map(int, '0110')) % 2 == 0
text(ax, 44, 16, r'plein : $Hx = 0$ pour $H$ = 1 1 1 1', 'sujet', 's')
text(ax, 44, 10, r'cercle : $Hx = 0$ pour $H$ = 1 1 0 0', 'autre', 's')
text(ax, 44, 4, r'ex. 0110 : 0+1+1+0 = 0, plein', 'sujet', 's')
save(fig, '68-110')
