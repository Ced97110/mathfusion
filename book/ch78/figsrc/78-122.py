import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
def row(y,role,head,terms,res):
    text(ax,2,y+15,head,role,'m',ha='left')
    for i,t in enumerate(terms):
        box(ax,2+i*21,y,19,11,role,label=t,size='s')
    box(ax,66,y,20,11,'resultat',label=res,size='s')
row(44,'sujet',r'$u\cdot(u\times v)$',[r'$1\times6=6$',r'$2\times(-3)=-6$',r'$0\times1=0$'],'somme = 0')
row(14,'autre',r'$v\cdot(u\times v)$',[r'$0\times6=0$',r'$1\times(-3)=-3$',r'$3\times1=3$'],'somme = 0')
text(ax,44,72,'produit scalaire nul = angle droit','resultat','m')
save(fig,'78-122')
