import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
def row(y,n,divs,label,lrole):
    f=numberline(ax,8,80,y,0,12,step=1,labels=False,arrow_right=False)
    text(ax,8,y+7,label,lrole,'m',ha='left')
    for d in divs:
        role='resultat' if d in (1,n) else 'limite'
        disc(ax,f(d),y,1.7,role); text(ax,f(d),y-4.5,str(d),role,'s')
row(40,7,[1,7],'7 : premier','resultat')
row(18,12,[1,2,3,4,6,12],'12 : pas premier','limite')
text(ax,4,4,'vert : 1 et lui-même','resultat','s',ha='left')
text(ax,84,4,'rouge : autres diviseurs','limite','s',ha='right')
save(fig,'05-044')
