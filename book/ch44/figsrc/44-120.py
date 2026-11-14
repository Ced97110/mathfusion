import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, r'$|S_3|$ : on choisit les images une par une', 'sujet', 's')
xs = [4, 34, 64]
for i, (x, k) in enumerate(zip(xs, (3, 2, 1))):
    box(ax, x, 20, 22, 24, 'sujet')
    text(ax, x + 11, 49 - 2, '', 'encre', 's')
    text(ax, x + 11, 38.5, f"image de {i + 1}", 'sujet', 's')
    for j in range(k):
        disc(ax, x + 11 + (j - (k - 1) / 2) * 6.4, 28, 2.5, 'varie')
    text(ax, x + 11, 14, f'{k} choix', 'varie', 's')
text(ax, 29, 32, r'$\times$', 'encre', 'l'); text(ax, 59, 32, r'$\times$', 'encre', 'l')
text(ax, 44, 5, r'$3\times2\times1=6$ ; pour 4 : 24', 'resultat', 'm')
save(fig, '44-120')
