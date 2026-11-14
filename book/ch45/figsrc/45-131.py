import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
s=12; x0=26; y0=6
text(ax,x0+2*s,62,r'$y$','encre','m')
text(ax,x0-12,y0+2*s,r'$x$','encre','m')
hl={(1,3):0,(3,1):0,(2,3):1,(3,2):1}
for r in range(4):
    text(ax,x0+r*s+s/2,y0+4*s+4,str(r),'fixe','s')
    text(ax,x0-4,y0+(3-r)*s+s/2,str(r),'fixe','s')
    for c in range(4):
        role='resultat' if (r,c) in hl else 'fixe'
        box(ax,x0+c*s,y0+(3-r)*s,s,s,role,r=0.3,lw=0.6)
        if (r,c) in hl: text(ax,x0+c*s+s/2,y0+(3-r)*s+s/2,str(hl[(r,c)]),'resultat','m',weight='bold')
line(ax,[(x0,y0+4*s),(x0+4*s,y0)],'varie',dash=True,lw=1.0)
save(fig,'45-131')
