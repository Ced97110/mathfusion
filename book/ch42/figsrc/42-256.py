import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
for j,(inp,img,col,role) in enumerate((('(1, 0)','(3, 5)','35','sujet'),('(0, 1)','(1, 2)','12','autre'))):
    cx=24+j*40
    box(ax,cx-10,66,20,9,'fixe',label=inp,size='s')
    arrow(ax,(cx,65.4),(cx,56.6),'varie')
    box(ax,cx-10,47,20,9,role,label=img,size='s')
    arrow(ax,(cx,46.4),(cx,40.6),'varie')
    box(ax,cx-9,6,18,34,role)
    for i,v in enumerate(col): text(ax,cx,30-i*13,v,role,'l',weight='bold')
text(ax,46,61,r'$T_A$','varie','m')
save(fig,'42-256')
