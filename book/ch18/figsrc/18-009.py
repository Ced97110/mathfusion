import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,22,57,'somme = 0','fixe','m',weight='bold'); text(ax,66,57,'produit = 0','resultat','m',weight='bold')
line(ax,[(44,6),(44,52)],'fixe',dash=True)
for i,s in enumerate([r'$3+(-3)$',r'$10+(-10)$',r'$0+0$']):
    box(ax,5,40-i*12,34,9,'fixe',label=s)
for i,(a,b) in enumerate([('5','0'),('0','8')]):
    y=40-i*12
    za=a=='0'
    box(ax,50,y,10,9,'resultat' if za else 'fixe',label=a); text(ax,66,y+4.5,r'$\times$','encre','m')
    box(ax,71,y,10,9,'resultat' if b=='0' else 'fixe',label=b)
text(ax,22,8,'on ne sait rien','limite','s'); text(ax,66,20,'un facteur vaut 0','resultat','s')
save(fig,'18-009')
