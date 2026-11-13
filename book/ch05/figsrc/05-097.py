import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
# rangée générale (haut) et rangée chiffrée (bas), colonnes alignées
cols=[(4,14),(24,26),(56,26)]   # (x, largeur) : d, a*u, b*v
sx=[x+w/2 for x,w in cols]
text(ax,44,57,'forme générale','fixe','s')
rows=[(44,[r'$d$',r'$a\times u$',r'$b\times v$']),(20,['6',r'$12\times(-1)$',r'$18\times 1$'])]
roles=['resultat','sujet','autre']
for y,labs in rows:
    for (x,w),lab,ro in zip(cols,labs,roles): box(ax,x,y,w,10,ro,label=lab,size='m')
    text(ax,19,y+5,'=','encre','l'); text(ax,51,y+5,'+','encre','l')
for (x,w) in cols: arrow(ax,(x+w/2,44),(x+w/2,31),'varie')
text(ax,24,37.5,'avec 12 et 18','varie','s')
text(ax,11,14,'le PGCD','resultat','s')
text(ax,44,7,r'$18-12=6$ : seulement 12 et 18','resultat','s')
save(fig,'05-097')
