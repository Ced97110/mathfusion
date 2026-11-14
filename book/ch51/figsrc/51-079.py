import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
def panel(ox,neutral,name,eq):
    oy=14; L=32; H=30
    arrow(ax,(ox,oy),(ox+L+4,oy),'fixe',lw=0.8); arrow(ax,(ox,oy),(ox,oy+H+8),'fixe',lw=0.8)
    f=lambda x:0.3+0.4*x
    pts=[(ox+x*L,oy+f(x)*25) for x in [i/20 for i in range(21)]]
    line(ax,pts,'sujet',lw=1.3)
    line(ax,[(ox,oy+neutral*25),(ox+L,oy+neutral*25)],'autre',lw=1.3)
    text(ax,ox+L-2,oy+f(1)*25+3.2,r'$h$','sujet','m')
    text(ax,ox+L/2,oy+neutral*25+(3.5 if neutral else 3.5),name,'autre','s')
    text(ax,ox+L/2,6,eq,'resultat','m')
panel(6,0,'fonction 0 : 0 partout',r'$h+0=h$')
panel(49,1,'fonction 1 : 1 partout',r'$h\times1=h$')
save(fig,'51-079')
