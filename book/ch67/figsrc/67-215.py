import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
xs = [34 + 9 * i for i in range(6)]
# modulo 3 : cycle de longueur 5 + un point fixe
y1 = 64
text(ax, 2, y1, 'modulo 3', 'encre', 's', ha='left')
for i, x in enumerate(xs):
    disc(ax, x, y1, 3.0, 'sujet' if i < 5 else 'fixe')
for i in range(4):
    arrow(ax, (xs[i] + 3.4, y1), (xs[i + 1] - 3.4, y1), 'varie')
arrow(ax, (xs[4] - 1, y1 + 3.2), (xs[0] + 1, y1 + 3.2), 'varie', curve=0.35)
brace(ax, xs[0] - 3, xs[4] + 3, y1 - 4, 'varie', label='5-cycle')
# modulo 5 : un échange + quatre points fixes
y2 = 40
text(ax, 2, y2, 'modulo 5', 'encre', 's', ha='left')
for i, x in enumerate(xs):
    disc(ax, x, y2, 3.0, 'fixe' if i < 4 else 'sujet')
arrow(ax, (xs[4] + 0.5, y2 + 3.4), (xs[5] - 0.5, y2 + 3.4), 'varie', both=True, curve=-0.6)
brace(ax, xs[4] - 3, xs[5] + 3, y2 - 4, 'varie', label='échange')
box(ax, 6, 14, 76, 11, 'resultat', label=r'$G_f=S_6$ : 720 éléments')
text(ax, 44, 7, 'non résoluble : pas de radicaux', 'limite', 's')
save(fig, '67-215')
