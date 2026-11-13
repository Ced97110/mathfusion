import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
for x,s,r in [(30,'a','sujet'),(37,'+','encre'),(44,'b','varie'),(51,'=','encre'),(58,'S','resultat')]:
    text(ax,x,62,s,r,'l')
brace(ax,27,47,58.5,'fixe','2 entrées')
brace(ax,55,61,58.5,'resultat','1 sortie')
def cas(y,u,a,b,ta,tb,ts):
    ax.plot([10,76],[y,y],color=COL['fixe'],lw=0.9,zorder=1.5)
    line(ax,[(10,y-1.5),(10,y+1.5)],'fixe')
    box(ax,10,y-1.5,a*u,3,'sujet'); box(ax,10+a*u,y-1.5,b*u,3,'varie')
    disc(ax,10+(a+b)*u,y,1.5,'resultat')
    text(ax,10+a*u/2,y+5,ta,'sujet','m'); text(ax,10+a*u+b*u/2,y+5,tb,'varie','m'); text(ax,10+(a+b)*u,y+5,ts,'resultat','m')
cas(40,9,4,3,'4','3','7')
cas(20,1.2,18,34,'18','34','52')
text(ax,44,8,'seules les valeurs changent','encre','s')
save(fig,'02-014')
