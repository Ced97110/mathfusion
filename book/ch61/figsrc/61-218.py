import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
y0=14; xs=[14,30,46,62]; hs=[6,12,24,48]
roots=[r'$\sqrt{2}$',r'$\sqrt[4]{2}$',r'$\sqrt[8]{2}$',r'$\sqrt[16]{2}$']
for x,h,d,r in zip(xs,hs,[2,4,8,16],roots):
    box(ax,x-5,y0,10,h,'sujet',r=0.5)
    text(ax,x,y0+h+3,str(d),'sujet','m'); text(ax,x,y0-4.5,r,'encre','s')
text(ax,78,38,'…','varie','xl'); text(ax,78,30,'sans fin','varie','s')
text(ax,34,66,r'degré $2^k$ au rang $k$','sujet','m')
save(fig,'61-218')
