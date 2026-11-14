import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
box(ax, 8, 92, 72, 9, 'fixe', label=r'hypothèse : $(3,1)$, $(1,2)$ indépendants', size='s')
text(ax, 44, 86, 'départ : deux écritures de (7, 4)', 'fixe', 's')
box(ax, 3, 74, 60, 9, 'sujet', label=r'$(7,4)=2\,(3,1)+1\,(1,2)$')
text(ax, 75, 78.5, r'$\alpha_1=2,\ \alpha_2=1$', 'sujet', 's')
box(ax, 3, 62, 60, 9, 'autre', label=r'$(7,4)=\beta_1\,(3,1)+\beta_2\,(1,2)$', size='s')
text(ax, 75, 66.5, r'$\beta_1,\ \beta_2$ : autres', 'autre', 's')
# soustraction
arrow(ax, (44, 61), (44, 53), 'varie', lw=1.5)
text(ax, 48, 57, 'on soustrait', 'varie', 's', ha='left')
box(ax, 8, 42, 72, 10, 'varie', label=r'$(2-\beta_1)(3,1)+(1-\beta_2)(1,2)=(0,0)$', size='s')
# étape qui porte le poids : indépendance
arrow(ax, (44, 41), (44, 33), 'varie', lw=1.5)
text(ax, 48, 37, 'hypothèse d’indépendance', 'varie', 's', ha='left', weight='bold')
box(ax, 8, 22, 72, 10, 'fixe', label='seule combinaison nulle : triviale', size='s')
arrow(ax, (44, 21), (44, 14), 'resultat', lw=1.5)
box(ax, 8, 3, 72, 10, 'resultat', label=r'$\alpha_i-\beta_i=0$, donc $\alpha_i=\beta_i$', weight='bold')
save(fig, '58-166')
