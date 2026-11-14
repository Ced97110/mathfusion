import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
sp=[(3,'varie',[r'$a,\ a^{\prime}$','5','17']),(33,'autre',[r'$b,\ b^{\prime}$','2','14']),(63,'resultat',[r'$ab,\ a^{\prime}b^{\prime}$','10','238'])]
for x,r,(t,n1,n2) in sp:
    box(ax,x,18,22,32,r)
    text(ax,x+11,44.5,t,r,'s'); text(ax,x+11,34,n1,r,'l'); text(ax,x+11,24,n2,r,'l')
text(ax,28,34,'×','encre','l'); text(ax,58,34,'=','encre','l')
text(ax,44,10,r'$a\equiv a^{\prime}$ et $b\equiv b^{\prime}$ : $ab\equiv a^{\prime}b^{\prime}$ ?','encre','s')
text(ax,44,3.5,'238 = 19 × 12 + 10','resultat','s')
save(fig,'52-009')
