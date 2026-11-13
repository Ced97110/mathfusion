import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
r2=r'$\sqrt{2}$'; m2=r'$-\sqrt{2}$'
for cx,cross,role,t in [(14,False,'fixe','ne rien changer'),(56,True,'varie','échanger')]:
    for k,(y,l) in enumerate([(40,r2),(22,m2)]):
        disc(ax,cx,y,5,'sujet',label=l,size='s'); disc(ax,cx+22,y,5,'sujet',label=l if not cross else (m2 if k==0 else r2),size='s')
    if cross:
        arrow(ax,(cx+5,40),(cx+17,22),role); arrow(ax,(cx+5,22),(cx+17,40),role)
    else:
        arrow(ax,(cx+5,40),(cx+17,40),role); arrow(ax,(cx+5,22),(cx+17,22),role)
    text(ax,cx+11,10,t,role,'s')
text(ax,44,58,'racines de x² − 2 : 2 réordonnements','sujet','s')
save(fig,'45-260')
