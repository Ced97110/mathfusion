import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
def mat(x,role,s,lab):
    box(ax,x,62,20,14,role,label=s,size='s'); text(ax,x+10,55,lab,role,'s')
mat(4,'sujet','0   -1\n1    0','rotation 90°\ndéterminant 1')
text(ax,28,69,r'$\times$','encre','l')
mat(32,'varie','1    0\n0   -1','miroir horizontal\ndéterminant -1')
text(ax,56,69,'=','encre','l')
mat(62,'resultat','0    1\n1    0','miroir\ndéterminant -1')
o=(44,22); u=14
P=lambda x,y:(o[0]+x*u,o[1]+y*u)
line(ax,[P(-0.5,-0.5),P(1.4,1.4)],'resultat',lw=0.9,dash=True)
arrow(ax,P(1,0),P(0,1),'resultat',lw=1.4,both=True,curve=0.0)
disc(ax,*P(1,0),1.1,'sujet'); disc(ax,*P(0,1),1.1,'sujet')
text(ax,P(1,0)[0]+2.5,P(1,0)[1]-3,r'$(1,0)$','sujet','s',ha='left')
text(ax,P(0,1)[0]-2.5,P(0,1)[1]+3,r'$(0,1)$','sujet','s',ha='right')
text(ax,P(1.4,1.4)[0]+2,P(1.4,1.4)[1],'axe 45°','resultat','s',ha='left')
save(fig,'73-235')
