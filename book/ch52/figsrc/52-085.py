import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
rows=[(50,r'$\bar4\times0..5$ pgcd 2','limite',[0,4,2,0,4,2]),(22,r'$\bar5\times0..5$ : pgcd 1','resultat',[0,5,4,3,2,1])]
for y,lab,role,vals in rows:
    text(ax,44,y+17,lab,role,'s')
    for i,v in enumerate(vals):
        r2=role if role=='limite' else ('resultat' if v==1 else 'fixe')
        box(ax,3+i*14,y,12,10,r2,label=str(v),size='l')
save(fig,'52-085')
