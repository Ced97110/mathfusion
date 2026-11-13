import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$\sigma=(1\ 2)$ change chaque nombre', 'varie', 'm')
top = [1, 2, 3]; img = [2, 1, 3]
text(ax, 44, 51, r'$\tau=(1\ 2\ 3)$', 'sujet', 'm')
text(ax, 44, 15, r'$\sigma\tau\sigma^{-1}=(2\ 1\ 3)$', 'resultat', 'm')
for i in range(3):
    x = 24 + i * 20
    disc(ax, x, 40, 4.2, 'sujet', label=str(top[i]), size='m')
    disc(ax, x, 24, 4.2, 'resultat', label=str(img[i]), size='m')
    arrow(ax, (x, 35.6), (x, 28.6), 'varie')
text(ax, 80, 32, r'$\sigma$', 'varie', 'l')
text(ax, 44, 6, 'même longueur, mêmes places', 'fixe', 's')
save(fig, '47-168')
