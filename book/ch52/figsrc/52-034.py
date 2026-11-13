import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,56,r'$17\equiv 5\equiv 29$ (modulo 12)','sujet','m')
y=30; f=numberline(ax,8,76,y,0,36,step=12,arrow_right=False)
for v,r in ((5,'sujet'),(17,'sujet'),(29,'sujet')):
    disc(ax,f(v),y,1.8,r); text(ax,f(v),y+4.4,str(v),r,'s')
arrow(ax,(f(5),y+6),(f(17),y+6),'varie',curve=-0.3); text(ax,(f(5)+f(17))/2,y+13,'+ 12','varie','s')
arrow(ax,(f(17),y+6),(f(29),y+6),'varie',curve=-0.3); text(ax,(f(17)+f(29))/2,y+13,'+ 12','varie','s')
box(ax,14,3,60,10,'resultat',label=r'$17-5=12\in I$ donc $17\equiv 5$',size='s')
save(fig,'52-034')
