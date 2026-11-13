import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
x0=24; cw=11; ch=8; gap=1.2
for r in range(3):
    y=30-r*(ch+gap)
    for c in range(4):
        box(ax,x0+c*(cw+gap),y,cw,ch,'sujet' if r==0 else 'resultat',r=0.5)
brace(ax,x0,x0+4*cw+3*gap,50,'sujet',label=r'$|H|=4$ par ligne',down=False)
line(ax,[(20,30+ch),(20,30-2*(ch+gap))],'varie',lw=0.9)
text(ax,4,30,r'$[G:H]$','varie','s',ha='left'); text(ax,4,23,'= 3 lignes','varie','s',ha='left')
text(ax,44,8,r'$|G|=12$ cases','resultat','m')
save(fig,'47-079')
