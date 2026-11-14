import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
o=(26,18); u=20
for name,v,r in [('i',(1,0,0),'sujet'),('j',(0,1,0),'autre'),('k',(0,0,1),'resultat')]:
    p=iso(*v,origin=o,u=u); arrow(ax,o,p,r,lw=1.4)
    d=(p[0]-o[0],p[1]-o[1]); n=math.hypot(*d)
    text(ax,p[0]+d[0]/n*4,p[1]+d[1]/n*4,name,r,'l')
for r,s,y in [('sujet',r'$i^2=-1$',70),('autre',r'$j^2=-1$',56),('resultat',r'$k^2=-1$',42)]:
    box(ax,56,y,28,10,r,label=s)
text(ax,70,34,r'$k=ij$','resultat','m')
box(ax,44,6,40,12,'varie',label=r'$ij=-ji$')
text(ax,70,22,'étape clé','varie','s')
text(ax,24,76,'trois directions orthogonales','encre','s')
save(fig,'78-152')
