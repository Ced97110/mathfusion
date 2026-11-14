import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
box(ax,2,8,32,52,'sujet'); box(ax,54,8,32,52,'autre')
text(ax,18,65,r'$G$','sujet','l',weight='bold'); text(ax,70,65,r'$\mathrm{Sym}\,S$','autre','l',weight='bold')
L=[r'$g_1$',r'$g_2$',r'$g_1g_2$']; R=[r'$T(g_1)$',r'$T(g_2)$',r'$T(g_1g_2)$']
for y,l,r in zip([48,34,20],L,R):
    text(ax,18,y,l,'sujet','m'); text(ax,70,y,r,'autre','m')
    arrow(ax,(27,y),(61,y),'varie')
text(ax,44,52,r'$T$','varie','m')
text(ax,44,3,r'$T(g_1g_2)=T(g_1)\circ T(g_2)$','resultat','s')
save(fig,'49-106')
