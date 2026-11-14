import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 16, 48, 'point de départ', 'resultat', 's')
box(ax, 4, 24, 24, 20, 'resultat'); text(ax, 16, 38, 'plan', 'resultat', 'm', weight='bold'); text(ax, 16, 30, 'valeurs 2 et 5', 'resultat', 's')
for k, d in enumerate(['3', '4']):
    x = 38 + 28 * k
    arrow(ax, (x - 9, 34), (x - 1, 34), 'varie')
    text(ax, x - 5, 38.5, 'lien', 'varie', 's')
    box(ax, x, 24, 18, 20, 'fixe', dash=True)
    text(ax, x + 9, 38, f'dim. {d}', 'fixe', 'm'); text(ax, x + 9, 30, '?', 'fixe', 'l')
text(ax, 44, 12, 'lemme de Jacobson : le lien', 'varie', 's')
text(ax, 44, 5, 'sans lien : arrêt au plan', 'limite', 's')
save(fig, '75-135')
