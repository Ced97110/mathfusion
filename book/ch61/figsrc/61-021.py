import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
box(ax,3,3,82,64,'sujet')
text(ax,44,62,r'$\mathbb{Q}$ : les fractions','sujet','m')
box(ax,20,44,16,10,'encre',label='1/2'); box(ax,52,44,16,10,'encre',label='3/4')
for cxr,lab in ((17,'somme\n5/4'),(44,'produit\n3/8'),(71,'quotient\n2/3')):
    box(ax,cxr-11,8,22,13,'resultat',label=lab,size='s')
    arrow(ax,(44,41),(cxr,22),'varie')
text(ax,44,32,'reste dans l’ensemble','resultat','s') if False else None
save(fig,'61-021')
