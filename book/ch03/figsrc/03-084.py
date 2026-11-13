import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(63)
text(ax,44,59,'4 × 426 = 4 × 400 + 4 × 20 + 4 × 6','encre','s')
for x,l in [(26,'4'),(44,'2'),(62,'6')]: box(ax,x,42,14,10,'sujet',label=l,size='l')
box(ax,6,42,14,10,'fixe',fill=False,dash=True,label='+1 chiffre',size='s')
for x,v in [(33,'400'),(51,'20'),(69,'6')]:
    arrow(ax,(x,41.5),(x,35),'fixe'); text(ax,x,32,v,'sujet','m')
brace(ax,46,74,29.5,'varie',label='26',down=True,size='s')
text(ax,12,19.5,'× 4','varie','m')
for x,v in [(33,'1 600'),(51,'80'),(69,'24')]:
    arrow(ax,(x,23.5),(x,15.5),'varie'); text(ax,x,12,v,'resultat','m')
brace(ax,26,76,9.5,'resultat',label='1 600 + 80 + 24 = 1 704',down=True,size='m')
save(fig,'03-084')
