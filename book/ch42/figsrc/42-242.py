import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
def panel(x0,rl,rr,fwd,role,title,trole):
    for y,a,b in ((40,rl[0],rr[0]),(24,rl[1],rr[1])):
        disc(ax,x0+3.5,y,3,'sujet',label=a,size='s'); disc(ax,x0+18.5,y,3,'autre',label=b,size='s')
        if fwd: arrow(ax,(x0+7,y),(x0+15,y),role)
        else: arrow(ax,(x0+15,y),(x0+7,y),role)
    text(ax,x0+11,10,title,trole,'s')
panel(2,['1','2'],['a','b'],True,'fixe',r'$\alpha$','fixe')
panel(33,['1','2'],['a','b'],False,'sujet',r'$\alpha^{-1}$','sujet')
panel(64,['1','2'],['a','b'],True,'resultat',r'$=\alpha$','resultat')
arrow(ax,(26,32),(32,32),'varie'); arrow(ax,(57,32),(63,32),'varie')
text(ax,29,36.5,'inverse','varie','s'); text(ax,60,36.5,'inverse','varie','s')
text(ax,44,54,r'$(\alpha^{-1})^{-1}=\alpha$','resultat','m')
save(fig,'42-242')
