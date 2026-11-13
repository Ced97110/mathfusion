import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,44,51,r'$x=1$','encre','m')
def row(y,items,end,role):
    xs=[4,22,38]
    box(ax,4,y,10,10,'sujet',label='1')
    text(ax,19,y+5,items,'varie','l')
    box(ax,24,y,10,10,'sujet',label='1')
    text(ax,39,y+5,'=','encre','l')
    box(ax,44,y,10,10,role,label=end,weight='bold')
row(30,'ou','1','resultat'); row(10,'+','2','limite')
text(ax,72,35,'« ou » : au moins\nun vrai','resultat','s')
text(ax,72,15,'2 n’est ni 0\nni 1','limite','s')
save(fig,'80-019')
