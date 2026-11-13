import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def rect(ax,x,y,w,h,role,dash=False,fill=True):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=0.8,ls='--' if dash else '-',zorder=2))

fig,ax=canvas(66)
text(ax,44,61,r'$4 = 2\times 2$  et  $6 = 2\times 3$','encre','m')
X=[4,14,24]
def chips(y,spec):
    for i,s in enumerate(spec):
        if s is None: box(ax,X[i],y,9,9,'limite',fill=False,dash=True)
        else: box(ax,X[i],y,9,9,'sujet' if s=='2' else 'autre',label=s)
rows=[(40,['2','2','3'],'12','resultat','tous les premiers,\nplus grand exposant'),
      (22,['2','2',None],'4','limite','oublie le 3'),
      (4,['2',None,'3'],'6','limite','prend l\'exposant 1\nau lieu de 2')]
for y,spec,res,r,lab in rows:
    chips(y,spec)
    arrow(ax,(34.5,y+4.5),(39.5,y+4.5),r)
    box(ax,40,y,12,9,r,label=res,size='l')
    text(ax,56,y+4.5,lab,r,'s',ha='left')
save(fig,'05-131')
