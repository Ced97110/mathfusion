import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
def row(y, n, role, k=1):
    w = 84 / n
    for i in range(n): box(ax, 2 + i * w, y, w, 7, role, r=0.5)
row(62, 12, 'fixe'); row(44, 6, 'sujet'); row(26, 2, 'resultat'); row(8, 2, 'resultat')
text(ax, 2, 73, r'$G$ : 12 éléments', 'fixe', 's', ha='left')
text(ax, 2, 55, r'$G/K$ : $12\div 2=6$', 'sujet', 's', ha='left')
text(ax, 2, 37, r'$(G/K)/(H/K)$ : $6\div 3=2$', 'resultat', 's', ha='left')
text(ax, 2, 19, r'$G/H$ : $12\div 6=2$', 'resultat', 's', ha='left')
text(ax, 78, 22.5, r'$\cong$', 'resultat', 'xl')
save(fig, '48-105')
