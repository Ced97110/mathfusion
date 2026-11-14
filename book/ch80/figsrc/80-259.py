import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
pos={1:(26,10),2:(12,28),3:(40,28),4:(12,46),6:(40,46),12:(26,64)}
for a,b in ((1,2),(1,3),(2,4),(2,6),(3,6),(4,12),(6,12)): line(ax,[pos[a],pos[b]],'fixe')
for n,(x,y) in pos.items(): disc(ax,x,y,4.6,{2:'sujet',3:'autre'}.get(n,'fixe'),label=str(n),size='s')
line(ax,[(16.8,28),(35.2,28)],'limite',dash=True)
text(ax,70,68,'diviseurs de 12','fixe','s')
text(ax,70,58,r'ni $2\leq3$ ni $3\leq2$','limite','s')
box(ax,54,36,32,11,'resultat',label=r'$\mu(2,3)=0$',size='s')
box(ax,54,20,32,11,'resultat',label=r'$\mu(3,2)=0$',size='s')
[l.set_zorder(1.5) for l in ax.lines]
save(fig,'80-259')
