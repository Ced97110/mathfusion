import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(100)
box(ax,16,86,56,11,'sujet'); text(ax,44,91.5,r'$\varphi(\alpha)\,\varphi(\beta)$','sujet','l')
for x in (23,65):
    arrow(ax,(44+(x-44)*0.5,86),(x,73),'varie')
text(ax,44,80,r'développer ($i\times i=-1$)','varie','s')
for x,t,fm in [(23,'partie réelle',r'$\cos\alpha\cos\beta-\sin\alpha\sin\beta$'),(65,'partie imaginaire',r'$\sin\alpha\cos\beta+\cos\alpha\sin\beta$')]:
    box(ax,x-21,52,42,21,'fixe'); text(ax,x,67,t,'fixe','s'); text(ax,x,59,fm,'encre','s')
    arrow(ax,(x,52),(x,41),'varie',lw=1.8)
text(ax,44,46.5,"formules d'addition",'varie','s',weight='bold')
for x,fm in [(23,r'$\cos(\alpha+\beta)$'),(65,r'$\sin(\alpha+\beta)$')]:
    box(ax,x-17,28,34,13,'resultat'); text(ax,x,34.5,fm,'resultat','m')
    arrow(ax,(x,28),(44+(x-44)*0.4,19),'resultat')
box(ax,26,6,36,13,'resultat'); text(ax,44,12.5,r'$=\varphi(\alpha+\beta)$','resultat','l')
save(fig,'48-149')
