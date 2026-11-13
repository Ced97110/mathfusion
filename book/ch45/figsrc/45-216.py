import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
P = {'e': (22, 52), 'a': (62, 52), 'b': (22, 22), 'c': (62, 22)}
cols = {'a': 'sujet', 'b': 'varie', 'c': 'autre'}
for k in 'abc': line(ax, [P['e'], P[k]], cols[k], lw=1.6)
lab = {'e': r'$(0,0)=e$', 'a': r'$(1,0)$', 'b': r'$(0,1)$', 'c': r'$(1,1)$'}
for k, (x, y) in P.items():
    disc(ax, x, y, 2.2, cols.get(k, 'fixe'))
text(ax, 22, 57, lab['e'], 'fixe', 's'); text(ax, 62, 57, lab['a'], 'sujet', 's')
text(ax, 22, 17, lab['b'], 'varie', 's'); text(ax, 62, 17, lab['c'], 'autre', 's')
text(ax, 42, 55, r'$H_1$', 'sujet', 's'); text(ax, 17, 37, r'$H_2$', 'varie', 's'); text(ax, 46, 41, r'$H_3$', 'autre', 's')
text(ax, 44, 78, r'sous-groupes $H_1,H_2,H_3$ : deux à deux, seulement en $e$', 'resultat', 's')
text(ax, 44, 70, r'attendu : $2\times2\times2=8$ éléments', 'limite', 's')
text(ax, 78, 37, 'mais le groupe', 'limite', 's'); text(ax, 78, 32, 'n’en a que 4', 'limite', 's')
text(ax, 44, 7, r'$(1,1)=(1,0)+(0,1)$ : $H_3$ est dans $H_1+H_2$', 'limite', 's')
save(fig, '45-216')
