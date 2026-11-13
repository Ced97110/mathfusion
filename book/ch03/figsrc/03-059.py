import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax,x,y,r,role): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],lw=0.5,zorder=4))
fig,ax=canvas(61)
def rangee(d,yb,ylab,ytxt,thick):
    text(ax,2,ylab,f'd = {d}','encre','m',ha='left')
    for k in range(d+1):
        x=20+12.5*k; role='limite' if k==d else 'resultat'
        box(ax,x,yb,11,10,role,fill=False,lw=1.6 if k in thick else 0.8)
        for j in range(k): dot(ax,x+5.5+(j-(k-1)/2)*2.4,yb+5,1.0,role)
rangee(4,42,47,None,{2}); rangee(3,15,20,None,{1})
text(ax,75.5,57,'r = 4 interdit','limite','s')
brace(ax,20,67.5,53.5,'resultat','de 0 à d − 1 = 3',down=False)
text(ax,63,30,'r = 3 interdit','limite','s')
brace(ax,20,55,26.5,'resultat','de 0 à d − 1 = 2',down=False)
text(ax,50.5,38.5,'14 ÷ 4 ; 1 706 ÷ 4','encre','s')
text(ax,38,11,'85 ÷ 3','encre','s')
save(fig,'03-059')
