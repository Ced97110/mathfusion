import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
ms=[60,30,15,5,1]; lab=['départ',r'$\div 2$',r'$\div 2$',r'$\div 3$',r'$\div 5$']
xc=[11,28,45,62,79]; base=16; k=0.7
line(ax,[(2,base+0.7),(86,base+0.7)],'limite',dash=True)
tops=[]
for x,m,l in zip(xc,ms,lab):
    role='resultat' if m==1 else 'sujet'
    ax.add_patch(Rectangle((x-5,base),10,m*k,ec=COL[role],fc=FILL[role],lw=0.8,zorder=2))
    text(ax,x,base+m*k+3.5,str(m),role,'m',weight='bold')
    text(ax,x,base-5,l,'varie','m')
    tops.append(base+m*k)
for i in range(4):
    arrow(ax,(xc[i]+5.3,tops[i]),(xc[i+1]-5.3,tops[i+1]+0.3),'varie')
text(ax,44,69,r'$m$ diminue à chaque étape','encre','m')
text(ax,66,33,r'$m$ ne descend pas sous 1','limite','s')
save(fig,'05-124')
