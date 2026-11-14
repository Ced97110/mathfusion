import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
items = ['ordonné', r'racines des positifs', 'impair : une racine']
for k, t in enumerate(items):
    y = 46 - 12 * k
    box(ax, 2, y, 30, 9, 'fixe', label=t, size='s')
    arrow(ax, (33, y + 4.5), (38, 36), 'varie', lw=0.8)
box(ax, 38, 26, 12, 20, 'sujet', label=r'$R$', size='l')
box(ax, 58, 40, 28, 14, 'resultat', label='exemple :\n' + r'$\mathbb{R}$', size='s')
box(ax, 58, 18, 28, 14, 'resultat', label='exemple :\nréels algébriques', size='s')
arrow(ax, (51, 40), (57, 46), 'sujet', lw=0.8)
arrow(ax, (51, 32), (57, 26), 'sujet', lw=0.8)
text(ax, 44, 8, 'R : n’importe quel corps\nréel clos, pas seulement ℝ', 'encre', 's')
save(fig, '69-053')
