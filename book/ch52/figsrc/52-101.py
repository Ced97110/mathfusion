import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
rows=[(44,'idéal premier','R/I sans diviseur de 0',r'(0) : quotient $\mathbb{Z}$ intègre'),(14,'idéal maximal','R/I est un corps',r'(5) : $\mathbb{Z}/5\mathbb{Z}$ est un corps')]
for y,a,b,ex in rows:
    box(ax,2,y,32,10,'sujet',label=a,size='s')
    arrow(ax,(36,y+5),(46,y+5),'fixe',both=True)
    box(ax,48,y,38,10,'autre',label=b,size='s')
    text(ax,67,y-5,ex,'resultat','s')
save(fig,'52-101')
