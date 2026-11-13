import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ys = [64, 45, 26, 7]
vals = [r'$(2\,;\,1)$', r'$(3\,;\,1)$', r'$(6\,;\,1)$', r'$(3{,}5\,;\,2{,}5)$']
roles = ['sujet', 'fixe', 'fixe', 'resultat']
side = ['entrée, nouvelle base', 'ancienne base', 'ancienne base', 'sortie, nouvelle base']
ops = [r'$\times\,P$ (à droite)', r'$A$ agit', r'$P^{-1}\times$ (à gauche)']
oc = ['varie', 'varie', 'varie']
for y, v, r, s in zip(ys, vals, roles, side):
    box(ax, 4, y, 30, 9, r, label=v)
    text(ax, 38, y + 4.5, s, r, 's', ha='left')
for i, (o, c) in enumerate(zip(ops, oc)):
    arrow(ax, (19, ys[i] - 0.5), (19, ys[i + 1] + 9.5), c)
    text(ax, 23, (ys[i] + ys[i + 1] + 9) / 2, o, c, 's', ha='left')
save(fig, '71-065')
