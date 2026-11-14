import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
text(ax,6,39,r'$RI\subseteq I$','encre','m',ha='left'); text(ax,6,19,r'$IR\subseteq I$','encre','m',ha='left')
for y,a,b,ra,rb in ((36,'5','8','fixe','sujet'),(16,'8','5','sujet','fixe')):
    box(ax,30,y-4.5,9,9,ra,label=a); text(ax,43,y,'×','encre','m'); box(ax,47,y-4.5,9,9,rb,label=b)
    arrow(ax,(58,y),(64,y),'varie'); box(ax,66,y-4.5,16,9,'resultat',label='40')
text(ax,34.5,44,r'$R$','fixe','s'); text(ax,51.5,44,r'$I$','sujet','s'); text(ax,74,44,r'$I$','resultat','s')
text(ax,44,4,r'aussi : 84 et −36 dans $I$','fixe','s')
save(fig,'52-046')
