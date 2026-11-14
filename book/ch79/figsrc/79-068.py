import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
text(ax, 22, 82, 'diviseurs de 60', 'resultat', 's'); text(ax, 66, 82, 'entiers positifs', 'limite', 's')
for i, s in enumerate(['4', '6', '10']):
    box(ax, 4 + 12 * i, 56, 10, 9, 'sujet', label=s)
for i in range(3): arrow(ax, (9 + 12 * i, 56), (17 + 5 * i, 36), 'fixe')
box(ax, 14, 24, 16, 11, 'resultat', label='60')
text(ax, 22, 14, 'un sup existe', 'resultat', 's')
xs = [50, 58, 66, 74]
for x, s in zip(xs, ['2', '4', '8', '16']):
    box(ax, x - 4, 56, 8, 9, 'sujet', label=s)
text(ax, 82, 60.5, '…', 'sujet', 'l')
for i, x in enumerate(xs): arrow(ax, (x, 56), (63 + 3.5 * i, 36), 'fixe')
box(ax, 60, 24, 16, 11, 'limite', label='?')
text(ax, 68, 14, 'aucun sup', 'limite', 's')
line(ax, [(44, 8), (44, 76)], 'fixe', dash=True)
save(fig, '79-068')
