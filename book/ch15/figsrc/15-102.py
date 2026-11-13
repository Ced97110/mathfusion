import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
f=numberline(ax,6,78,14,0,30,5)
for v,top in [(25,52),(5,40),(9,28)]: line(ax,[(f(v),14),(f(v),top)],'fixe',dash=True)
arrow(ax,(f(0),52),(f(25),52),'sujet'); text(ax,f(12.5),55.5,r'$a^2=25$','sujet','m')
arrow(ax,(f(25),40),(f(5),40),'varie'); text(ax,f(15),43.5,r'$-2ab=-20$','varie','m')
arrow(ax,(f(5),28),(f(9),28),'autre'); text(ax,f(7),31.5,r'$+b^2=+4$','autre','m')
text(ax,f(9)+3,27.5,r'$=9=(5-2)^2$','resultat','m',ha='left')
save(fig,'15-102')
