import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
a=4.5
POS=dict(TL=(-a,a),TR=(a,a),BR=(a,-a),BL=(-a,-a))
def sq(cx,cy,p,role):
    box(ax,cx-8,cy-8,16,16,role)
    for k,v in POS.items():
        disc(ax,cx+v[0],cy+v[1],2.0,role if k==p else 'fixe',fill=(k==p))
box(ax,2,16,52,32,'fixe',fill=False,dash=True)
text(ax,38,43.5,'couple (g, x)','fixe','s')
box(ax,5,20,18,18,'sujet',label=r'$g$',size='l')
text(ax,14,14,'quart de tour','sujet','s')
sq(40,29,'TL','autre')
text(ax,40,14,r'$x\in S$ : coloration','autre','s')
arrow(ax,(56,29),(64,29),'varie')
text(ax,60,34,'action','varie','s')
sq(76,29,'TR','resultat')
text(ax,76,14,r'$gx\in S$','resultat','s')
text(ax,12,43.5,r'$g\in G$','sujet','s')
text(ax,44,5,r'$G\times S\to S$','encre','m')
save(fig,'49-093')
