import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
text(ax,8,53,'scalaires','varie','s')
text(ax,72,53,'droite vectorielle','sujet','s')
box(ax,64,3,22,43,'sujet',fill=True)
text(ax,75,39,'{000, 110}','sujet','m')
text(ax,75,26,'000','encre','l'); text(ax,75,12,'110','encre','l')
for y,s,res in ((38,0,'000'),(16,1,'110')):
    disc(ax,8,y,4,'varie',label=str(s),size='l')
    box(ax,17,y-6,36,12,'fixe',label=r'$%d\times 110 = %s$'%(s,res))
    arrow(ax,(53,y),(68,26 if s==0 else 12),'resultat')
    arrow(ax,(12,y),(17,y),'varie')
save(fig,'80-049')
