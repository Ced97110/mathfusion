import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
x0,y0,cw,ch=14,14,20,14
vals=[['0','0'],['1','0']]
for i in range(2):
    for j in range(2):
        box(ax,x0+j*cw,y0+(1-i)*ch,cw,ch,'sujet' if j==0 else 'autre',label=vals[i][j])
text(ax,x0+10,y0+2*ch+5,r'$\varepsilon\times1$','sujet'); text(ax,x0+30,y0+2*ch+5,r'$\varepsilon\times\varepsilon$','autre')
text(ax,x0+10,y0-5,r'$=\varepsilon$','sujet'); text(ax,x0+30,y0-5,r'$=0$','autre')
text(ax,72,36,r'$\varepsilon\neq0$','limite'); text(ax,72,24,r'$N(\varepsilon)=0$','limite')
arrow(ax,(55,28),(61,28),'varie')
save(fig,'77-101')
