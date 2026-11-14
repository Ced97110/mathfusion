import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,24,66,r'matrice de $B$','sujet','m')
for (r,c,v,role) in [(0,0,'1','sujet'),(0,1,'2','varie'),(1,0,'0','fixe'),(1,1,'3','sujet')]:
    box(ax,6+c*13,42+(1-r)*11,13,11,role,label=v,size='l')
text(ax,66,66,r'termes de $B(x,x)$','encre','m')
for i,(lab,role) in enumerate([(r'$1\cdot x\cdot x$','sujet'),(r'$2\cdot x\cdot y$','varie'),(r'$3\cdot y\cdot y$','sujet')]):
    box(ax,50,46-i*0+(2-i)*0+ (1-i)*0 + 0 + (0 if True else 0) + (2-i)*0 + 0 + 0 + (0), 0.01,0.01,'fixe',fill=False) if False else None
    box(ax,52,54-i*10,30,8,role,label=lab,size='m')
box(ax,6,6,76,12,'resultat',label=r'$Q(x)=B(x,x)=x^2+2xy+3y^2$',size='s')
text(ax,44,24,r'en $(1,\,1)$ : $1+2+3=6$','resultat','m')
save(fig,'71-115')
