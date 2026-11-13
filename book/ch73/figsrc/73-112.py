import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50); s=10; OL=(12,22); OR=(52,22)
pl=lambda o,x,y:(o[0]+s*x,o[1]+s*y)
def seg(o,a,b,r): line(ax,[pl(o,*a),pl(o,*b)],r,lw=1.8); disc(ax,*pl(o,*a),1.0,r); disc(ax,*pl(o,*b),1.0,r)
for o in (OL,OR): seg(o,(0,0),(0,1),'sujet')
seg(OL,(2,0),(1,0),'resultat'); seg(OR,(2,0),(3,1),'limite')
text(ax,OL[0]-3,OL[1]+5,'1','sujet','s',ha='right'); text(ax,OR[0]-3,OR[1]+5,'1','sujet','s',ha='right')
text(ax,OL[0]+15,OL[1]+4,'1','resultat','s'); text(ax,OR[0]+19,OR[1]+8,r'$\sqrt{2}$','limite','m',ha='right')
for o,rr in ((OL,'resultat'),(OR,'limite')):
    text(ax,o[0],o[1]-5,'départ','sujet','s'); text(ax,o[0]+25 if o is OR else o[0]+15,o[1]-5,'images',rr,'s')
text(ax,26,44,r'$A$ orthogonale + translation','resultat','s'); text(ax,68,44,'cisaillement + translation','limite','s')
text(ax,26,5,'distance gardée','resultat','m'); text(ax,68,5,'distance changée','limite','m')
save(fig,'73-112')
