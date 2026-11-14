import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def cells(x,y,n,role,cw=2.8,h=4.5):
    for i in range(n): box(ax,x+i*cw,y,cw,h,role,r=0.3,lw=0.6)
box(ax,2,52,40,11,'sujet',label=r'$Q(ax)=a^2Q(x)$',size='s')
box(ax,46,52,40,11,'sujet',label=r'$Q(x+y)-Q(x)-Q(y)$',size='s')
text(ax,22,45,r'$a=2$ : le vecteur double','fixe','s')
for y,n,role,lab in [(35,3,'sujet',r'$Q(x)=3$'),(24,6,'limite','obtenu : 6'),(13,12,'resultat',r'attendu : $4\times 3$')]:
    text(ax,2,y+7.2,lab,role,'s',ha='left'); cells(4,y,n,role)
text(ax,66,43,r'$=0$','encre','l')
text(ax,66,33,'bilinéaire','resultat','m')
text(ax,66,26,'condition vérifiée','resultat','s')
text(ax,22,3,'première condition : non','limite','s')
save(fig,'71-114')
