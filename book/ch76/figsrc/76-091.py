import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
text(ax,44,88,r'colonne 1 : $1\,e_1+3\,e_2$','sujet','m'); text(ax,44,82,r'colonne 2 : $2\,e_1+4\,e_2$','autre','m')
W_=r'$\wedge$'
rows=[('1 × 2   $e_1$ ∧ $e_1$','0 : vecteur répété','fixe','fixe'),('1 × 4   $e_1$ ∧ $e_2$',r'$4\ e_1$ ∧ $e_2$','sujet','sujet'),
      ('3 × 2   $e_2$ ∧ $e_1$',r'$-6\ e_1$ ∧ $e_2$','varie','varie'),('3 × 4   $e_2$ ∧ $e_2$','0 : vecteur répété','fixe','fixe')]
for i,(a,b,r1,r2) in enumerate(rows):
    y=66-i*14
    box(ax,4,y,46,10,r1,label=a,size='m'); arrow(ax,(51,y+5),(59,y+5),r1); box(ax,60,y,24,10,r2,label=b,size='s' if 'répété' in b else 'm')
text(ax,44,15,r'$e_2$ ∧ $e_1=-\,e_1$ ∧ $e_2$','varie','m')
text(ax,44,6,'$4-6=-2$','resultat','xl')
save(fig,'76-091')
