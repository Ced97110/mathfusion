import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
text(ax,50,66,'m : entier','fixe','s'); text(ax,72,66,'n : entier','fixe','s')
rows=[('nombre',r'$1$',r'$+\,1\sqrt{2}$','sujet'),('nombre',r'$2$',r'$+\,3\sqrt{2}$','sujet'),
      ('somme',r'$3$',r'$+\,4\sqrt{2}$','resultat'),('produit',r'$8$',r'$+\,5\sqrt{2}$','resultat')]
for i,(lab,a,b,role) in enumerate(rows):
    y=48-i*15 
    text(ax,4,y+5,lab,role,'m',ha='left')
    box(ax,40,y,20,10,role,label=a,size='l'); box(ax,62,y,22,10,role,label=b,size='l')
line(ax,[(4,30.5),(84,30.5)],'fixe',dash=True)
save(fig,'51-068')
