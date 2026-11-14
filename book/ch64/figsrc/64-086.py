import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
dims = [(12, 10), (22, 18), (32, 26), (42, 34)]
roles = ['fixe', 'sujet', 'sujet', 'resultat']
for (w, h), r in reversed(list(zip(dims, roles))):
    box(ax, 2, 4, w, h, r)
text(ax, 8, 9, r'$F_1$', 'fixe', 's')
text(ax, 6, 4 + 18 - 3.5, r'$F_2$', 'sujet', 's', ha='left')
text(ax, 6, 4 + 26 - 3.5, r'$F_3$', 'sujet', 's', ha='left')
text(ax, 6, 4 + 34 - 3.5, r'$K=F_{r+1}$', 'resultat', 's', ha='left')
# un étage : F_i -> F_{i+1}
x0, w = 50, 36
box(ax, x0, 44, w, 10, 'sujet', label=r'$F_{i+1}=F_i(d_i)$', size='m')
arrow(ax, (x0 + w / 2, 44), (x0 + w / 2, 39.5), 'varie', lw=1.2)
box(ax, x0, 27, w, 12, 'varie', label=r'$d_i^{\,n_i}=a_i$', size='l')
text(ax, x0 + w / 2, 22.5, r'avec $a_i\in F_i$ (étage d’avant)', 'varie', 's')
box(ax, x0, 4, w, 12, 'resultat', label='$K$ contient les racines\nde $f$ : $r$ étapes', size='s')
save(fig, '64-086')
