import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def R(ax,x,y,w,h,role): ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role],lw=0.8,zorder=2))
fig,ax=canvas(62)
u=3
for i,(a,b) in enumerate([(4,6),(3,8),(2,12)]):
    y=[43,26,12][i]
    R(ax,4,y-a*u/2,b*u,a*u,'sujet')
    text(ax,4+b*u/2,y,f'${a}\\times {b}$','sujet','m')
    text(ax,4+b*u+4,y,'= 24','resultat','m',ha='left')
text(ax,44,57,'aire 24','encre','l')
save(fig,'18-004')
