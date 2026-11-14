import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,2,4,40,68,'sujet',fill=False); box(ax,46,4,40,68,'autre',fill=False)
text(ax,22,66,r'$156\div12$','sujet','m'); text(ax,66,66,r'$(x^2+5x+6)\div(x+2)$','autre','s')
L=[('156','sujet'),('−12','varie'),('36','sujet'),('−36','varie'),('0','resultat')]
R=[(r'$x^2+5x+6$','autre'),(r'$-(x^2+2x)$','varie'),(r'$3x+6$','autre'),(r'$-(3x+6)$','varie'),(r'$0$','resultat')]
for i,(a,r) in enumerate(L):
    y=56-i*10
    text(ax,30-(3 if i==1 else 0),y,a,r,'m',ha='right')
    if i in(1,3): line(ax,[(10,y-4.5),(32,y-4.5)],'fixe')
for i,(a,r) in enumerate(R):
    y=56-i*10
    text(ax,78-(8 if i==1 else 0),y,a,r,'s',ha='right')
    if i in(1,3): line(ax,[(52,y-4.5),(80,y-4.5)],'fixe')
text(ax,66,9,'même disposition','fixe','s'); text(ax,22,9,'reste 0','resultat','s')
save(fig,'21-106')
