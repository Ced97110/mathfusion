import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
cols=[14,34,54,74]
couples=['(198, 54)','(54, 36)','(36, 18)','(18, 0)']
restes=[54,36,18,0]
text(ax,2,78,'couple après chaque division','sujet','s',ha='left')
text(ax,2,29.5,'reste de cette division','varie','s',ha='left')
for c,cp,r in zip(cols,couples,restes):
    box(ax,c-9,62,18,9,'sujet',label=cp,size='s')
    role='resultat' if r==18 else ('fixe' if r==0 else 'varie')
    box(ax,c-9,34,18,9,role,label=str(r),size='l',lw=1.6 if r==18 else 0.8)
    line(ax,[(c,61.5),(c,43.5)],'fixe',dash=True)
text(ax,74,29.5,'on s\'arrête','fixe','s')
box(ax,6,4,76,10,'resultat',label='PGCD(252, 198) = 18',size='l')
arrow(ax,(54,33.5),(54,14.5),'resultat',lw=1.4)
text(ax,56,24,'dernier reste non nul','resultat','s',ha='left')
save(fig,'05-088')
