import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
for i,n in enumerate((1,2,3)):
    y=40-i*16
    text(ax,2,y+4,r'$10^%d = 2^%d \times 5^%d$'%(n,n,n),'encre','m',ha='left')
    for k in range(n):
        disc(ax,51+k*6,y+4,2.3,'sujet'); disc(ax,69+k*6-0,y+4,2.3,'autre')
disc(ax,12,5,2.3,'sujet'); text(ax,16,5,'facteur 2','sujet','s',ha='left')
disc(ax,44,5,2.3,'autre'); text(ax,48,5,'facteur 5','autre','s',ha='left')
text(ax,44,57,'autant de 2 que de 5','resultat','m',weight='bold')
save(fig,'08-084')
