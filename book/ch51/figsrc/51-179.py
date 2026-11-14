import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
s=11; x0=20; y0=12
for r in range(3):
    for c in range(3):
        x=x0+c*s; y=y0+(2-r)*s
        if r==c: box(ax,x,y,s,s,'fixe',label=r'$-1$',r=0.2)
        else: box(ax,x,y,s,s,'resultat',r=0.2)
for k,n in enumerate('ijk'):
    text(ax,x0+k*s+s/2,y0+3*s+3,'$'+n+'$','sujet','m')
    text(ax,x0-3.5,y0+(2-k)*s+s/2,'$'+n+'$','sujet','m')
box(ax,58,36,5,5,'resultat'); text(ax,64.5,38.5,'6 produits\nde la figure','resultat','s',ha='left')
box(ax,58,22,5,5,'fixe'); text(ax,64.5,24.5,'3 carrés,\ntable seule','fixe','s',ha='left')
text(ax,x0+1.5*s,5.5,r'produit : ligne $\times$ colonne','encre','s')
save(fig,'51-179')
