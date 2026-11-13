import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax,x,y,w,h,roles):
    for i,r in enumerate(roles):
        x0=x+i*w
        poly(ax,[(x0,y),(x0+w,y),(x0+w,y+h),(x0,y+h)],r or "fixe",fill=r is not None)
fig,ax=canvas(90)
text(ax,44,85,'2/9 + 5/9','encre','l')
X,C=38,5.5
text(ax,2,70,'1  même 9 ?','encre','s',ha='left')
row(ax,X,72,C,5,['sujet']*2+[None]*7)
row(ax,X,65,C,5,['autre']*5+[None]*4)
text(ax,2,47,'2  haut : 2 + 5 = 7','encre','s',ha='left')
row(ax,X,42,C,9,['sujet']*2+['autre']*5+[None]*2)
text(ax,2,19,'3  on garde le 9','encre','s',ha='left')
row(ax,X,14,C,9,['resultat']*7+[None]*2)
text(ax,X+C*4.5,6,'résultat : 7/9','resultat','m')
save(fig,'07-022')
