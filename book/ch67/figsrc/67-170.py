import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
rows = [r'$\alpha^0=1$', r'$\alpha^1=\alpha$', r'$\alpha^2$', r'$\alpha^3$',
        r'$\alpha^4=\alpha+1$', r'$\alpha^5=\alpha+\alpha^2$']
roles = ['sujet', 'sujet', 'sujet', 'sujet', 'varie', 'resultat']
ys = [72 - 13 * i for i in range(6)]
for y, s, role in zip(ys, rows, roles):
    box(ax, 8, y, 44, 8, role, label=s)
for y in ys[:-1]:
    arrow(ax, (30, y), (30, y - 4.8), 'varie')
    text(ax, 33, y - 2.5, r'$\times\alpha$', 'varie', 's', ha='left')
text(ax, 55, ys[4] + 6, 'exposant 4 atteint :', 'varie', 's', ha='left')
text(ax, 55, ys[4] + 1.5, 'on applique la règle', 'varie', 's', ha='left')
box(ax, 8, 87, 72, 9, 'varie', label=r'règle du corps : $\alpha^4=\alpha+1$')
save(fig, '67-170')
