import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,61,r'$\varepsilon^2=0$','sujet','l')
x0,y0,cw,ch=30,22,16,12
text(ax,24,50,r'$\times$','fixe')
heads=[r'$1$',r'$\varepsilon$']; cells=[[r'$1$',r'$\varepsilon$'],[r'$\varepsilon$',r'$0$']]
for j in range(2): text(ax,x0+j*cw+cw/2,y0+2*ch+4,heads[j],'sujet')
for i in range(2):
    text(ax,x0-6,y0+(1-i)*ch+ch/2,heads[i],'sujet')
    for j in range(2):
        r='varie' if (i==1 and j==1) else 'fixe'
        box(ax,x0+j*cw,y0+(1-i)*ch,cw,ch,r,label=cells[i][j])
text(ax,44,12,r'$2\varepsilon\times3\varepsilon=0$','varie')
text(ax,44,5,'deux éléments non nuls','fixe','s')
save(fig,'77-100')
