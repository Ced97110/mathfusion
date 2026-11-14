import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,24,57,r'$\mathbb{Z}/2$','autre','l')
P=lambda i,j:(14+22*i,24+22*j)
for i in (0,1):
    for j in (0,1):
        role='sujet' if (i,j)==(1,1) else 'fixe'
        disc(ax,*P(i,j),2.5,role)
arrow(ax,(17,24),(33,24),'fixe'); text(ax,25,28,r'$u$','fixe','m')
disc(ax,*P(1,1),4.8,'resultat',fill=False)
text(ax,14,19,'(0, 0)','fixe','s'); text(ax,36,19,'(1, 0)','fixe','s'); text(ax,14,51,'(0, 1)','fixe','s'); text(ax,36,55,r'$x=(1,1)$','sujet','s')
text(ax,63,46,r'$c=2\times1\div1=0$','varie','m'); text(ax,63,36,r'on retire $0\times u$','varie','m'); text(ax,63,26,'image = x','resultat','m')
text(ax,44,9,'la réflexion ne bouge rien','limite','m')
save(fig,'72-103')
