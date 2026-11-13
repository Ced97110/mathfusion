import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
rows=[(r'$8\times8=64$','resultat'),(r'$(-8)\times(-8)=64$','resultat'),(r'$?\times?=-64$','limite')]
for k,(t,r) in enumerate(rows):
    y=44-k*15
    box(ax,2,y-5,50,10,r,label=t,size='m')
text(ax,70,44,'positif','resultat','m'); text(ax,70,29,'positif','resultat','m'); text(ax,70,14,'aucun','limite','m',weight='bold')
text(ax,62,3,'même signe : produit positif','fixe','s')
save(fig,'18-106')
