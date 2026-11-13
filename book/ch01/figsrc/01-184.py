import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
for x,h in zip((20,32,44,56),'8421'):
    text(ax,x+6,79,h,'fixe','m')
box(ax,20,64,12,10,'fixe',fill=False,dash=True)
for x in (32,44,56):
    box(ax,x,64,12,10,'sujet'); text(ax,x+6,69,'1','sujet','l')
for a,b in [(62,50),(50,38),(38,26)]: arrow(ax,(a,82),(b,82),'varie',curve=0.5)
text(ax,72,84,r'$\times$ 2','varie','m')
text(ax,44,57,r'4 + 2 + 1 = 7 $\rightarrow$ 111','resultat','m')
pat=[1,0,0,0,0,1,1,1,0,1,0,0,1]
for i,b in enumerate(pat): box(ax,8+5.5*i,34,5.5,6,'sujet',fill=bool(b),r=0.4,lw=0.6)
text(ax,44,45,'1000011101001 : 13 signes','sujet','s')
for i in range(4): box(ax,8+5.5*i,14,5.5,6,'autre',r=0.4,lw=0.6)
text(ax,44,25,'4 329 : 4 signes (base dix)','autre','s')
save(fig,'01-184')
