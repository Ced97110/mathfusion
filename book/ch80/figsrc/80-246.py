import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(96)
text(ax,44,90,r'$b$ → atomes sous $b$','encre','m')
oy,dy=16,20
pos={'1':(44,0,'{ }'),'2':(22,1,'{2}'),'3':(44,1,'{3}'),'5':(66,1,'{5}'),'6':(22,2,'{2, 3}'),'10':(44,2,'{2, 5}'),'15':(66,2,'{3, 5}'),'30':(44,3,'{2, 3, 5}')}
E=[('1','2'),('1','3'),('1','5'),('2','6'),('2','10'),('3','6'),('3','15'),('5','10'),('5','15'),('6','30'),('10','30'),('15','30')]
c=lambda n:(pos[n][0],oy+pos[n][1]*dy+6)
for a,b in E: line(ax,[c(a),c(b)],'fixe')
for n,(x,l,s) in pos.items():
    box(ax,x-10,oy+l*dy,20,12,'sujet',label=n+'\n'+s,size='s')
text(ax,44,5,'8 diviseurs ↔ 8 parties','encre','s')
[l.set_zorder(1.5) for l in ax.lines]
save(fig,'80-246')
