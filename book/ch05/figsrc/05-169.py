import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(104)
text(ax,2,98,'1. Départ : la liste est finie','varie','s',ha='left')
for i,l in enumerate([r'$p_1$',r'$p_2$','⋯',r'$p_n$']):
    if l=='⋯': text(ax,6+i*13+4,89,l,'sujet','m')
    else: disc(ax,10+i*13+(0 if i<3 else 0),89,3.6,'sujet',label=l,size='s')
line(ax,[(54,83),(54,95)],'varie',lw=1.6)
text(ax,2,76,'2. L’étape qui porte le poids','limite','s',ha='left')
u=14
for b in range(3):
    box(ax,10+b*u,58,u,7,'sujet',r=0.3,lw=0.6); box(ax,10+b*u,47,u,7,'sujet',r=0.3,lw=0.6)
box(ax,10+3*u,47,2,7,'varie',r=0.2,lw=0.6)
line(ax,[(52,45),(52,66)],'fixe',dash=True)
brace(ax,10,24,65,'sujet',r'$p_i$',down=False)
text(ax,55,61.5,r'$p_1\times\cdots\times p_n$','sujet','s',ha='left')
text(ax,57,50.5,r'$P$','varie','m',ha='left')
brace(ax,52,54,47,'varie','différence : 1')
text(ax,44,34,r'aucun $p_i$ ne divise 1','limite','s')
text(ax,2,24,'3. Arrivée : contradiction','resultat','s',ha='left')
box(ax,6,6,76,12,'resultat',label='P a un facteur hors liste',size='s')
arrow(ax,(44,31),(44,19),'resultat')
save(fig,'05-169')
