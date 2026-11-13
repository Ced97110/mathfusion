import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
s=9; g=1.5; x0=30
rows=[(r'$\mathbb{R}$ : dim. 1',['1']),(r'$\mathbb{C}$ : dim. 2',['1','i']),(r'$\mathbb{H}$ : dim. 4',['1','i','j','k'])]
y=64
for lab,els in rows:
    text(ax,2,y+s/2,lab,'sujet','m',ha='left')
    for i,e in enumerate(els):
        box(ax,x0+i*(s+g),y,s,s,'sujet',label=r'$%s$'%e)
    y-=s+5
text(ax,2,y+s/2,'dim. 5 ?','limite','m',ha='left')
box(ax,x0,y,4*s+3*g,s,'sujet',label=r'$\mathbb{H}$')
box(ax,x0+4*(s+g),y,s,s,'limite',label=r'$l$',dash=True)
text(ax,44,y-6,r'$lk=-lk$ : impossible','limite','m')
text(ax,44,y-14,'aucune ligne après $\\mathbb{H}$','fixe','s')
save(fig,'78-113')
