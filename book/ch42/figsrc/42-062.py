import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
x0=18;u=7.5
for i in range(8):
    box(ax,x0+u*i,30,u,u,'sujet' if i<3 else 'varie',r=0.3)
    box(ax,x0+u*i,12,u,u,'varie' if i<5 else 'sujet',r=0.3)
text(ax,15,33.75,'3 + 5','encre','s',ha='right'); text(ax,15,15.75,'5 + 3','encre','s',ha='right')
text(ax,48,24.75,'=','encre','xl')
brace(ax,x0,x0+8*u,39,'resultat',label='8',down=False)
brace(ax,x0,x0+8*u,10.5,'resultat',label='8',down=True)
box(ax,18,50,5,5,'sujet'); text(ax,25,52.5,'a = 3','sujet','s',ha='left')
box(ax,50,50,5,5,'varie'); text(ax,57,52.5,'b = 5','varie','s',ha='left')
save(fig,'42-062')
