import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig,ax=canvas(56)
text(ax,44,50,r'$a\times a\times a = 2$','sujet',16)
f=numberline(ax,8,76,26,1.5,2.5,0.5)
for v,r,lab,y,low in ((1.728,'varie','1,2³ = 1,728',34,'trop petit'),(2,'resultat','cible : 2',41,None),(2.197,'varie','1,3³ = 2,197',34,'trop grand')):
    disc(ax,f(v),26,1.7,r); text(ax,f(v),y,lab,r,'s')
    if low: text(ax,f(v),16,low,r,'s')
save(fig,'61-006')
