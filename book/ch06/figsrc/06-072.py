import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cell(ax,x,y,w,h,role,fill=True,lw=0.6): ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=lw,zorder=2))
fig,ax=canvas(72)
for i in range(3):
    cell(ax,14+i*20,50,20,8,'sujet')
    arrow(ax,(24+i*20,49),(24+i*20,39),'varie')
    box(ax,16+i*20,28,16,10,'resultat',label=f'{i+1}')
text(ax,44,64,r'carafe : $3/4$ de litre','sujet','m')
text(ax,44,19,r'verre : $1/4$ de litre','varie','m')
text(ax,44,8,'réponse : 3 verres','resultat','m',weight='bold')
save(fig,'06-072')
