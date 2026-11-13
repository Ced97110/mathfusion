import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
pw, y0 = 22, 14
xs = [5, 33, 61]
box(ax, xs[0] + 2.75, y0, 16.5, 16.5, 'sujet')
cs = 5.5
for i in range(4):
    for j in range(3):
        box(ax, xs[1] + i * cs, y0 + j * cs, cs, cs, 'varie', r=0.2)
for i in range(4):
    for j in range(3):
        box(ax, xs[2] + i * cs, y0 + j * cs, cs, cs, 'resultat' if (i < 3 and j < 2) else 'fixe', r=0.2)
for k, t in enumerate(['départ', 'étape clé', 'arrivée']):
    text(ax, xs[k] + 11, 42, t, ['sujet', 'varie', 'resultat'][k], 'm', weight='bold')
for k, t in enumerate(['carré de côté 1', '12 cases égales', '6 cases sur 12']):
    text(ax, xs[k] + 11, 7, t, 'encre', 's')
for k in range(2):
    arrow(ax, (xs[k] + pw + 0.5, y0 + 8.25), (xs[k + 1] - 0.8, y0 + 8.25), 'varie')
save(fig, '06-056')
