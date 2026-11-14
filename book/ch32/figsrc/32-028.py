import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
xs = [2, 31.5, 61]
for x, r, lb, cap in zip(xs, ['fixe', 'varie', 'sujet'], [r'$\sin\,\theta=0{,}5$', r'$\theta$', '30°'],
                         ['équation\n(une phrase)', 'inconnue\n(une lettre)', 'solution\n(un angle)']):
    box(ax, x, 64, 25, 14, r, label=lb, size='m'); text(ax, x + 12.5, 57, cap, r, 's')
text(ax, 44, 46, 'tester un angle', 'fixe', 's')
box(ax, 2, 28, 20, 10, 'sujet', label='30°'); arrow(ax, (22.5, 33), (29.5, 33), 'fixe')
box(ax, 30, 28, 36, 10, 'resultat', label='sin 30° = 0,5'); text(ax, 77, 33, 'vrai', 'resultat', 'm')
box(ax, 2, 10, 20, 10, 'autre', label='40°'); arrow(ax, (22.5, 15), (29.5, 15), 'fixe')
box(ax, 30, 10, 36, 10, 'limite', label='sin 40° ≈ 0,64'); text(ax, 77, 15, 'faux', 'limite', 'm')
save(fig, '32-028')
