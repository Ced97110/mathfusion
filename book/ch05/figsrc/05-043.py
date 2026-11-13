import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
y=28
f=numberline(ax,6,76,y,-30,-15,step=1,labels=False,arrow_right=False)
for v in (-30,-25,-20,-15): text(ax,f(v),y-4,f'−{abs(v)}',  'fixe','s')
disc(ax,f(-25),y,1.9,'resultat'); disc(ax,f(-20),y,1.9,'limite'); disc(ax,f(-23),y,1.5,'sujet')
text(ax,f(-23),y+4.2,'−23','sujet','s')
arrow(ax,(f(-25),y+8),(f(-23),y+8),'resultat'); arrow(ax,(f(-23),y+8),(f(-20),y+8),'limite')
text(ax,f(-24)-3,y+12,'r = 2','resultat','s'); text(ax,f(-22)+2,y+12,'r = −3 : refusé','limite','s',ha='left')
text(ax,f(-25)+2,y-9,'−25 : multiple à gauche','resultat','s')
text(ax,44,5,r'$-23=5\times(-5)+2$','sujet','l')
save(fig,'05-043')
