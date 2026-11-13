import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,44,51,r'$H$ : multiples de 3','sujet','m')
f=numberline(ax,6,70,30,-12,24,step=3,labels=False,arrow_right=False,tick=1.4)
for v,r,l in [(12,'sujet','12'),(21,'sujet','21'),(-9,'resultat','−9'),(0,'fixe','0')]:
    disc(ax,f(v),30,2.0,r); text(ax,f(v),24.5,l,r,'s')
arrow(ax,(f(12),33.5),(f(-9),33.5),'varie',curve=0.35)
text(ax,f(1.5),43,r'$12-21=-9$','varie','s')
text(ax,44,10,r'$gh^{-1}$ reste dans $H$','resultat','m')
save(fig,'46-287')
