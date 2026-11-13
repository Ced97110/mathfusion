import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
a=4.5
POS=dict(TL=(-a,a),TR=(a,a),BR=(a,-a),BL=(-a,-a))
def sq(cx,cy,p1,p2,role='fixe'):
    box(ax,cx-7,cy-7,14,14,role)
    for p,r in ((p1,'varie'),(p2,'sujet')):
        disc(ax,cx+POS[p][0],cy+POS[p][1],1.9,r)
S=(12,33); MT=(42,49); MB=(42,17); E=(74,33)
sq(*S,'TL','TR'); sq(*MT,'BL','TL'); sq(*MB,'TR','TL'); sq(*E,'BR','TR','resultat')
text(ax,S[0],S[1]-10,'départ','fixe','s')
# legend digits next to start
text(ax,S[0]-a,S[1]+a+3.6,'1','varie','s'); text(ax,S[0]+a,S[1]+a+3.6,'2','sujet','s')
arrow(ax,(20,38),(34,46),'varie'); text(ax,24,46,r'$x$','varie','m')
arrow(ax,(50,46),(66,38),'varie'); text(ax,61,46,r'$y$','varie','m')
arrow(ax,(20,28),(34,20),'varie'); text(ax,24,20,r'$y$','varie','m')
arrow(ax,(50,20),(66,28),'varie'); text(ax,61,20,r'$x^{-1}$','varie','m')
text(ax,42,62,r'$yx$ : d’abord $x$, puis $y$','varie','s')
text(ax,42,5,r'$x^{-1}y$ : d’abord $y$, puis $x^{-1}$','varie','s')
text(ax,74,19,'même résultat','resultat','s')
save(fig,'49-083')
