import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
y=22
f=numberline(ax,6,76,y,0,25,step=1,labels=False,arrow_right=False)
for v in [0,5,10,15,20,25]: text(ax,f(v),y-4,str(v),'fixe','s')
for v in [3,8,13,18,23]:
    disc(ax,f(v),y,1.5,'sujet')
disc(ax,f(8),y,2.2,'limite'); disc(ax,f(3),y,2.2,'resultat')
arrow(ax,(f(8),y+3),(f(3),y+3),'varie',curve=0.5)
text(ax,(f(8)+f(3))/2,y+13,'on retire b = 5','varie','s')
text(ax,f(8)+3,y+9,'r = 8 supposé, r ≥ b','limite','s',ha='left')
text(ax,f(3)+8,y-10,'3 < 8 : contradiction','resultat','s')
text(ax,44,y-16,r'points : $23-5\times x\geq 0$','sujet','s')
save(fig,'05-036')
