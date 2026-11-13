import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cell(ax,x,y,w,h,role,fill=True,lw=0.6): ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=lw,zorder=2))
fig,ax=canvas(82)
for i in range(4):
    for j in range(3):
        role='fixe' if i==3 else ('resultat' if j<2 else 'sujet')
        cell(ax,22+i*12,32+j*10,12,10,role)
text(ax,46,77,'terrain : 12 ha','encre','m')
brace(ax,22,58,63,'sujet',label=r'$3/4$ planté : 9 ha',down=False)
text(ax,15,52,r'$2/3$ : blé, 6 ha','resultat','s',rot=90)
text(ax,46,22,r'$6/12 = 1/2$ du terrain','resultat','m')
save(fig,'06-071')
