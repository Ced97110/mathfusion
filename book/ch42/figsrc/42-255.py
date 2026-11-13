import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
o=(14,12); u=6.4
arrow(ax,o,(o[0]+6.6*u,o[1]),'fixe',lw=0.7); arrow(ax,o,(o[0],o[1]+7.6*u),'fixe',lw=0.7)
text(ax,o[0]+6.8*u,o[1]-3,r'$x$','fixe','s'); text(ax,o[0]-4,o[1]+7.6*u,r'$y$','fixe','s')
P=lambda a,b:(o[0]+a*u,o[1]+b*u)
arrow(ax,o,P(1,0),'fixe',lw=1.2); arrow(ax,o,P(0,1),'fixe',lw=1.2)
arrow(ax,o,P(3,5),'sujet',lw=1.3); arrow(ax,o,P(1,2),'autre',lw=1.3)
text(ax,P(1,0)[0]+2,o[1]-3.5,'(1, 0)','fixe','s',ha='left'); text(ax,o[0]-2,P(0,1)[1],'(0, 1)','fixe','s',ha='right')
text(ax,P(3,5)[0]+2,P(3,5)[1]+1,'(3, 5)','sujet','s',ha='left'); text(ax,P(1,2)[0]+2,P(1,2)[1]-2,'(1, 2)','autre','s',ha='left')
for j,(c,role) in enumerate((('35','sujet'),('12','autre'))):
    for i,v in enumerate(c): box(ax,58+j*14,36-i*13,13,12,role,label=v)
text(ax,71,52,r'tableau $A$','encre','s')
save(fig,'42-255')
