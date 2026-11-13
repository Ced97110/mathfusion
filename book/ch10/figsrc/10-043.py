import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
rows=[(52,53.5,53.82,54,'53,82','54','+0,18','1er nombre'),(34,41.5,41.6,42,'41,6','42','+0,4','2e nombre'),(16,95.4,95.42,96,'95,42','96','+0,58','somme')]
for y,v0,a,b,la,lb,d,lab in rows:
    f=numberline(ax,20,80,y,v0,v0+1,0.5,labels=False,arrow_right=False)
    disc(ax,f(a),y,1.5,'sujet'); disc(ax,f(b),y,1.5,'varie')
    arrow(ax,(f(a)+1.8,y+3.2),(f(b)-0.2,y+3.2),'varie',lw=1.4); text(ax,(f(a)+f(b))/2,y+6.5,d,'varie','s')
    text(ax,f(a),y-4.5,la,'sujet','s'); text(ax,f(b)+2,y-4.5,lb,'varie','s'); text(ax,2,y,lab,'encre','s',ha='left')
save(fig,'10-043')
