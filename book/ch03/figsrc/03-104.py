import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
def rect(x0,c,r):
    for i in range(c):
        for j in range(r): box(ax,x0+3*i,18+3*j,3,3,'sujet',r=0.3,lw=0.5)
rect(6,4,3); rect(28,2,6); rect(46,1,12)
text(ax,12,30.5,r'4 $\times$ 3 = 12','sujet','m')
text(ax,31,39.5,r'2 $\times$ 6 = 12','sujet','m')
text(ax,47.5,57.5,r'1 $\times$ 12 = 12','sujet','m')
line(ax,[(66,18),(66,54)],'limite',lw=1.6)
text(ax,72,58.5,r'0 $\times$ $q$ = 0 : aire 0,'+'\njamais 12','limite','s')
for x,s in ((12,r'$d$ = 4, $q$ = 3'),(29.5,r'$d$ = 2, $q$ = 6'),(49.5,r'$d$ = 1, $q$ = 12'),(66,r'$d$ = 0')):
    text(ax,x,13,s,'varie','s')
arrow(ax,(6,5),(58,5),'varie')
text(ax,73,5,'$d$ diminue,\n'+r'$d$ $\times$ $q$ = 12','varie','s')
save(fig,'03-104')
