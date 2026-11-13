import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cell(ax,x,y,w,h,role,fill=True,lw=0.6): ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=lw,zorder=2))
fig,ax=canvas(72)
x0=8
for i in range(15): cell(ax,x0+i*4.8,52,4.8,8,'sujet')
for k in range(6):
    for j in range(5): cell(ax,x0+k*12+j*2.4,30,2.4,8,'resultat',lw=0.2)
    cell(ax,x0+k*12,30,12,8,'resultat',fill=False,lw=1.0)
line(ax,[(8,26),(8,64)],'fixe',dash=True); line(ax,[(80,26),(80,64)],'fixe',dash=True)
text(ax,44,66,r'planche : $15/4$ m','sujet','m')
text(ax,44,45,'=','encre','l')
text(ax,44,24,r'$6\times 5/8 = 30/8$ m','resultat','m')
text(ax,44,10,r'$30/8 = 15/4$ : on s’arrête','resultat','m')
save(fig,'06-075')
