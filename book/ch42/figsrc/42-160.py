import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
text(ax,20,66,'comparer','encre','s'); text(ax,66,66,r'cas $(2,5)$ et $(5,2)$','encre','s')
for c,(a,b,a2,b2),role,sg,sr in ((4,(r'$s$',r'$t$',r"$s^\prime$",r"$t^\prime$"),'sujet',r'$=$','resultat'),(52,('2','5','5','2'),'sujet',r'$\neq$','limite')):
    box(ax,c,46,14,12,role,label=a); box(ax,c+16,46,14,12,role,label=b)
    box(ax,c,16,14,12,'autre',label=a2); box(ax,c+16,16,14,12,'autre',label=b2)
    for x in (c+7,c+23):
        arrow(ax,(x,45),(x,29),sr,both=True); text(ax,x+4,37,sg,sr,'m')
text(ax,44,8,r'égaux : $s=s^\prime$ ET $t=t^\prime$','resultat','m',weight='bold')
save(fig,'42-160')
