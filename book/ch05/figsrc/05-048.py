import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
for x,role,lab,cap in [(6,'sujet',r'$d$','un diviseur'),(30,'varie',r'$\mid$','divise'),(54,'autre',r'$n=12$','nombre étudié')]:
    box(ax,x,44,18,14,role,label=lab,size='l'); text(ax,x+9,39,cap,role,'s')
text(ax,4,29,'on remplace d par :','encre','s',ha='left')
for i,v in enumerate([2,3,4,5,6]):
    box(ax,6+14*i,16,12,9,'limite' if v==5 else 'resultat',label=str(v),size='m')
text(ax,4,10,'12 = 3 × 4 : d = 3 convient','resultat','s',ha='left')
text(ax,4,4,'5 ne divise pas 12','limite','s',ha='left')
save(fig,'05-048')
