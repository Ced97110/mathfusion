import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
text(ax,44,74,'les d : diviseurs communs de 12 et 18','encre','s')
base=10; k=7
for i,v in enumerate([1,2,3,6]):
    x=14+i*16; r='resultat' if v==6 else 'sujet'
    box(ax,x,base,12,v*k,r,label=str(v),size='l',lw=(1.6 if v==6 else 0.8)) if v>=2 else box(ax,x,base,12,k,r,label=str(v),size='l')
line(ax,[(10,base+6*k),(84,base+6*k)],'resultat',dash=True)
line(ax,[(10,base),(84,base)],'fixe')
text(ax,66,base+6*k+4.5,'PGCD = le plus grand d','resultat','s',weight='bold')
save(fig,'05-080')
