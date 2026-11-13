import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
for k in range(13):
    box(ax,3+k*6,36,5.5,10,'sujet',r=0.5); box(ax,3+k*6,8,5.5,10,'sujet',r=0.5)
box(ax,82,8,4,10,'varie',r=0.5)
brace(ax,3,81,48,'sujet',label=r'13 fois 12',down=False)
text(ax,44,29,r'$12\times13=156$ : reste 0','resultat','s')
text(ax,44,2.5,r'$12\times13+1=157$ : reste 1','varie','s')
save(fig,'21-107')
