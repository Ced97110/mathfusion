import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,60,'« un nombre augmenté de 9 vaut 30 »','encre','m')
ws=[(5,'un nombre'),(32,'augmenté de'),(63,'vaut')]
ss=[(5,'$x$'),(32,'$+\\,9$'),(63,'$=\\,30$')]
wd=[22,28,20]
for (x,t),(x2,s),d in zip(ws,ss,wd):
    box(ax,x,36,d,10,'sujet',label=t,size='s'); box(ax,x,10,d,10,'resultat',label=s,size='l')
    arrow(ax,(x+d/2,35.5),(x+d/2,20.5),'varie')

save(fig,'16-088')
