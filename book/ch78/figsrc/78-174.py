import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,4,61,'groupe : composer','sujet','s',ha='left')
text(ax,4,4,'algèbre : additionner','autre','s',ha='left')
bw=22;xs=[4,33,62]
tops=[r'$R_{0{,}01}$',r'$R_{0{,}02}$',r'$R_{0{,}03}$']
bots=[r'$0{,}01\,J$',r'$0{,}02\,J$',r'$0{,}03\,J$']
for i,x in enumerate(xs):
    box(ax,x,44,bw,11,'resultat' if i==2 else 'sujet',label=tops[i])
    box(ax,x,10,bw,11,'resultat' if i==2 else 'autre',label=bots[i])
    arrow(ax,(x+bw/2,43),(x+bw/2,22),'varie')
text(ax,28.5,49.5,r'$\times$','encre','l')
text(ax,57.5,49.5,'=','encre','l')
text(ax,28.5,15.5,'+','encre','l')
text(ax,57.5,15.5,'=','encre','l')
text(ax,22,33,'Lie','varie','s')
save(fig,'78-174')
