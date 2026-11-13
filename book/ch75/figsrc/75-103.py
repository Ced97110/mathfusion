import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
x0, y0, d = 26, 24, 14
for i in range(3):
    for j in range(3):
        disc(ax, x0 + i * d, y0 + j * d, 2.6, 'sujet')
    text(ax, x0 + i * d, y0 - 7, str(i), 'varie', 'm')
    text(ax, x0 - 9, y0 + i * d, str(i), 'varie', 'm')
text(ax, x0 + d, y0 - 14, '1re coordonnée : 3 choix', 'varie', 's')
text(ax, 9, y0 + 2 * d + 8, '2e : 3 choix', 'varie', 's', ha='left')
text(ax, 44, 72, r'$\mathbb{F}_3^{\,2}$ : $3\times 3=9$ vecteurs', 'resultat', 'm')
text(ax, 70, y0 + d, r'$q^n=3^2$', 'resultat', 'l')
save(fig, '75-103')
