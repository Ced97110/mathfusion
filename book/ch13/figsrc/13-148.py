import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
xs = [4 + i * 13 for i in range(5)]
sq = [1, 1, 0, 4, 4]
for x, n, q in zip(xs, ['1', '−1', '0', '2', '−2'], sq):
    box(ax, x, 50, 11, 9, 'sujet', label=n)
    arrow(ax, (x + 5.5, 49), (x + 5.5, 41), 'varie')
    box(ax, x, 31, 11, 9, 'resultat', label=str(q))
box(ax, 71, 50, 13, 9, 'fixe', dash=True, label='?')
box(ax, 71, 31, 13, 9, 'fixe', dash=True, label='?')
arrow(ax, (77.5, 49), (77.5, 41), 'fixe')
text(ax, 35, 63, 'cinq exemples testés', 'sujet', 's')
text(ax, 77.5, 63, 'et les autres ?', 'fixe', 's')
text(ax, 35, 26, 'carrés obtenus', 'resultat', 's')
box(ax, 22, 6, 44, 12, 'limite', dash=True, label=r'carré $= -1$ ?', size='m')
text(ax, 44, 21.5, 'pas obtenu avec ces cinq', 'fixe', 's')
save(fig, '13-148')
