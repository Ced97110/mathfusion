import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
text(ax,44,70,r'$x^{2} = 16$','sujet','l')
# partie « longueur » : carré d'aire 16, côté inconnu x, quadrillé de 5 mm
poly(ax,[(8,32),(28,32),(28,52),(8,52)],'sujet')
for i in (1,2,3):
    line(ax,[(8+5*i,32),(8+5*i,52)],'fixe',lw=0.3)
    line(ax,[(8,32+5*i),(28,32+5*i)],'fixe',lw=0.3)
text(ax,4.5,42,r'$x$','sujet','s')
# essai 3 : carré de 9 carreaux, trop petit
line(ax,[(8,32),(23,32),(23,47),(8,47),(8,32)],'limite',dash=True)
text(ax,15.5,39.5,'9','limite','s')
text(ax,62,62,'3 × 3 = 9 : trop petit','limite','s')
arrow(ax,(29.5,46),(46,54),'varie')
text(ax,63,54,r'$x$ = √16 = 4','resultat','m')
text(ax,63,47,'côté : longueur, donc 4','resultat','s')
# partie « équation » : droite graduée de −5 à 5 : f(v) = 42 + 6,4 v
f=numberline(ax,10,74,10,-5,5,labels=False)
for v in (-4,0,4):
    text(ax,f(v),6.6,('−%d' % -v if v<0 else str(v)),'fixe','s')
ax.add_patch(Circle((f(4),10),1.3,color=COL['resultat'],zorder=6))
text(ax,f(4),15.5,'4 × 4 = 16','resultat','s')
ax.add_patch(Circle((f(-4),10),1.3,color=COL['autre'],zorder=6))
text(ax,17,15.5,'(−4) × (−4) = 16','autre','s')
text(ax,17,19.2,'pas un côté','limite','s')
line(ax,[(4,27),(84,27)],'fixe',lw=0.5,dash=True)
text(ax,44,23,r'équation $x^{2} = 16$ : deux solutions','fixe','s')
save(fig,'04-088')
