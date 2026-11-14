import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
x0=22; d=9
for r in range(3):
    y=48-r*15
    box(ax,x0-2,y-5.5,4*d+2,11,'sujet' if r==0 else 'fixe',r=0.5)
    for c in range(4): disc(ax,x0+4+c*d,y,2.2,'sujet' if r==0 else 'fixe')
    text(ax,8,y,str(r+1),'varie','m')
brace(ax,x0-2,x0+4*d,63,'sujet',label=r'$|H|=4$',down=False)
line(ax,[(63,56),(63,26)],'varie',lw=0.8)
text(ax,66,40,r'$[G:H]=3$','varie','m',ha='left')
text(ax,44,10,r'$|G|=12$ éléments','fixe','m')
save(fig,'47-074')
