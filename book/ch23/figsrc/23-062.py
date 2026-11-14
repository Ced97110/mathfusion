import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
S = [r'$a=1,\ b=-3,\ c=-1$', r'$b^2-4ac=9+4=13$', r'$\sqrt{13}$', r'$3+\sqrt{13}\ \mathrm{et}\ 3-\sqrt{13}$', r'$x=\frac{3\pm\sqrt{13}}{2}$']
roles = ['sujet', 'fixe', 'fixe', 'fixe', 'resultat']
labs = ['repérer', 'calculer', 'racine', 'numérateurs', 'diviser par 2a']
for i, t in enumerate(S):
    y = 88 - i*21
    disc(ax, 6, y+7, 3.4, 'varie', label=str(i+1), size='s')
    box(ax, 12, y, 74, 14, roles[i], label=t)
    text(ax, 14, y+17.5, labs[i], 'varie', 's', ha='left') if False else None
    if i: arrow(ax, (6, y+21-3.4+0.0), (6, y+14+3.4+0.0), 'varie') if False else None
for i in range(4):
    y = 88 - i*21
    arrow(ax, (49, y-0.3), (49, y-7+0.3), 'fixe')
save(fig, '23-062')
