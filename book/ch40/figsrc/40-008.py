import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# quatre actions = quatre colonnes ; deux cas chiffrés = deux lignes
xs = [3.0, 25.0, 47.0, 69.0]; w = 16.0
heads = ['1. choisir\n' + r'$\theta$', '2. calculer\n' + r'$\cos\theta$', '3. nombre\nsous la barre', '4. diviser\n149,6']
roles = ['varie', 'varie', 'sujet', 'resultat']
for x, h, r in zip(xs, heads, roles):
    box(ax, x, 48, w, 14, r, label=h, size='s')
for i in range(3):
    arrow(ax, (xs[i] + w + 0.5, 55), (xs[i + 1] - 0.5, 55), 'fixe')
cases = [(30, [r'$\pi/2$', '0', '1', '149,6']), (8, [r'$\pi/3$', '0,5', '1,0085', '148,3'])]
text(ax, 44, 42, r'$1+0{,}017\cos\theta$ puis $149{,}6$ divisé par ce nombre', 'encre', 's')
for y, vals in cases:
    for i, (x, v) in enumerate(zip(xs, vals)):
        box(ax, x, y, w, 9, roles[i], label=v, size='m')
    for i in range(3):
        arrow(ax, (xs[i] + w + 0.5, y + 4.5), (xs[i + 1] - 0.5, y + 4.5), 'fixe')
save(fig, '40-008')
