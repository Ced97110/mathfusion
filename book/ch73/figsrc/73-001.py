import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
# haut : le but, un quart de tour (compliqué)
s2=0.025; w2,h2=1000*s2,800*s2
xa,ya=8,54
poly(ax,[(xa,ya),(xa+w2,ya),(xa+w2,ya+h2),(xa,ya+h2)],'sujet')
text(ax,xa+w2/2,ya+h2/2,'photo','sujet','s')
xb=52
poly(ax,[(xb,ya-2.5),(xb+h2,ya-2.5),(xb+h2,ya-2.5+w2),(xb,ya-2.5+w2)],'sujet')
text(ax,xb+h2/2,ya-2.5+w2/2,'tournée','sujet','s')
arrow(ax,(xa+w2+3,ya+h2/2+1),(xb-3,ya+h2/2+1),'varie',curve=-0.45)
text(ax,39,ya+h2+5.5,'un quart de tour','varie','s')
text(ax,39,ya+h2+2,'(compliqué)','fixe','s')
# bas : un glissement de lignes (simple)
text(ax,44,48,'à la place : 3 glissements','resultat','m')
s=0.03; w,h,sh=1000*s,800*s,200*s
x0,x1,y0=8,50,12
poly(ax,[(x0,y0),(x0+w,y0),(x0+w,y0+h),(x0,y0+h)],'sujet')
text(ax,x0+w/2,y0+h/2,'photo','sujet')
brace(ax,x0,x0+w,y0,'sujet','1 000 px')
text(ax,x0-3.5,y0+h/2,'800 px','sujet','s',rot=90)
line(ax,[(x1,y0),(x1,y0+h),(x1+w,y0+h),(x1+w,y0)],'fixe',dash=True)
poly(ax,[(x1,y0),(x1+w,y0),(x1+w+sh,y0+h),(x1+sh,y0+h)],'sujet')
arrow(ax,(x1,y0+h+2.5),(x1+sh,y0+h+2.5),'varie')
text(ax,x1+sh/2+8,y0+h+6.5,'glisse de 200 px','varie','s')
text(ax,x1+w/2,y0-3,'ligne du bas : ne bouge pas','fixe','s')
arrow(ax,(x0+w+3,y0+h/2),(x1-4,y0+h/2),'varie')
text(ax,43,y0+h/2+3.2,'glisser','varie','s')
save(fig,'73-001')
