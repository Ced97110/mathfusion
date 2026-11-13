import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
cols=[('30 jetons',[]),('mult. de 5',['5']),('mult. de 6',['2','3']),('mult. de 30',['2','3','5'])]
for i,(h,ds) in enumerate(cols):
    x=2+i*21; cx=x+9.5
    box(ax,x,48,19,9,'fixe',label=h,size='s')
    n=len(ds)
    if n==0: text(ax,cx,34,'aucun','fixe','s')
    for k,d in enumerate(ds): disc(ax,cx+(k-(n-1)/2)*6.2,34,2.6,'sujet',label=d,size='s')
    box(ax,cx-5,12,10,10,'varie')
    line(ax,[(cx-2.5,17),(cx+2.5,17)],'varie',lw=1.6)
    if n%2==0: line(ax,[(cx,14.5),(cx,19.5)],'varie',lw=1.6)
text(ax,44,5,'le signe suit le nombre de facteurs','encre','s')
save(fig,'80-010')
