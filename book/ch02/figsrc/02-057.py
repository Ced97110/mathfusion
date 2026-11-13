import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
for x,t,r in [(26,'a','sujet'),(32,'+','encre'),(38,'b','autre'),(44,'=','encre'),(50,'b','autre'),(56,'+','encre'),(62,'a','sujet')]:
    text(ax,x,48,t,r,'l')
arrow(ax,(26,45),(62,45),'varie',curve=0.3)
arrow(ax,(38,51),(50,51),'varie',curve=-0.4)
u=2.6
box(ax,6,22,8*u,5,'sujet',label='a = 8',size='s'); box(ax,6+8*u,22,5*u,5,'autre',label='b = 5',size='s')
box(ax,48,22,5*u,5,'autre',label='b = 5',size='s'); box(ax,48+5*u,22,8*u,5,'sujet',label='a = 8',size='s')
brace(ax,6,6+13*u,20,'resultat',label='13 euros',down=True)
brace(ax,48,48+13*u,20,'resultat',label='13 euros',down=True)
save(fig,'02-057')
