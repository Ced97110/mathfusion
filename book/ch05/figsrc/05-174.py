import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,60,'PGCD(12, 18) = 6 : un groupe','varie','s')
u=4; x0=12
for r,(n,y,role) in enumerate([(12,50,'sujet'),(18,38,'autre')]):
    text(ax,2,y,str(n),role,'m',ha='left',weight='bold')
    for i in range(n): box(ax,x0+i*u,y-2.5,u,5,role,r=0.2,lw=0.4)
    for g in range(n//6): box(ax,x0+g*6*u,y-2.5,6*u,5,'varie',fill=False,lw=1.5,r=0.2)
text(ax,63,50,'2 groupes de 6','sujet','s',ha='left')
text(ax,x0+36,31,'3 groupes de 6','autre','s')
text(ax,44,15,r'$\dfrac{12}{18}=\dfrac{2}{3}$','resultat','xl')
save(fig,'05-174')
