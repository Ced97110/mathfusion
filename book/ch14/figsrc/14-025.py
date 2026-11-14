import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
def case(y,k,b,nv,mv):
    for i in range(k): box(ax,8+11*i,y,9,9,'varie',label=b)
    x2=8+11*k+6
    for i in range(mv): box(ax,x2+11*i,y,9,9,'fixe',label=b)
    brace(ax,8,8+11*k-2,y+9,'varie',label=f'$n$ = {nv}',down=False)
    brace(ax,x2,x2+11*mv-2,y,'fixe',label=f'$m$ = {mv}')
case(44,3,'2',3,2)
case(14,4,'5',4,1)
save(fig,'14-025')
