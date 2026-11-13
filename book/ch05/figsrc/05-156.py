import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def rowp(y,a,b,ta,tb):
    box(ax,8,y,14,12,'sujet',label=a,size='l'); box(ax,66,y,14,12,'autre',label=b,size='l')
    text(ax,15,y-4,ta,'fixe','s'); text(ax,73,y-4,tb,'fixe','s')
    arrow(ax,(24,y+6),(64,y+6),'resultat',both=True)
    text(ax,44,y+10,'premiers entre eux','resultat','s'); text(ax,44,y+2,'seul commun : 1','fixe','s')
rowp(46,'8','15','pas premier','pas premier')
rowp(14,'7','11','premier','premier')
line(ax,[(2,32),(86,32)],'fixe',dash=True)
save(fig,'05-156')
