import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ch, cw = 9, 21
xs = [18, 41, 64]
roles = ['sujet', 'autre', 'resultat']
heads = [r'$f(x)=2x$', r'$g(x)=x+1$', r'$(f+g)(x)$']
for x, r, hd in zip(xs, roles, heads):
    box(ax, x, 46, cw, ch, r, label=hd, size='s')
rows = [(32, '2', ('4', '3', '4 + 3 = 7')), (20, '5', ('10', '6', '10 + 6 = 16'))]
for y, xv, vals in rows:
    text(ax, 3, y + 4.5, r'$x=$' + xv, 'encre', 's', ha='left')
    for x, r, v in zip(xs, roles, vals):
        box(ax, x, y, cw, ch, r, label=v, size='s')
box(ax, 4, 3, 80, 9, 'varie', label=r'$\alpha f$ : chaque valeur $\times\,\alpha$', size='s')
save(fig, '58-103')
