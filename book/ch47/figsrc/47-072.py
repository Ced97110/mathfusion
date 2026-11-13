import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
x0=24; cw=11; ch=8; gap=1.2
names=[r'$g_1H$',r'$g_2H$',r'$g_3H$']
for r in range(3):
    y=46-r*(ch+gap+1.5)
    text(ax,12,y+ch/2,names[r],'sujet','m')
    for c in range(4):
        box(ax,x0+c*(cw+gap),y,cw,ch,'sujet',r=0.5)
brace(ax,x0,x0+4*cw+3*gap,60,'fixe',label=r'$|H|=4$ par ligne',down=False)
text(ax,44,14,r'$|G|=3\times4=12$','resultat','l')
text(ax,44,6,'avec {0, 1} : 24, trop','limite','s')
save(fig,'47-072')
