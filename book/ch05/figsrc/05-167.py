import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
def row(y,role,labels,wall=True):
    for i,l in enumerate(labels):
        disc(ax,10+i*10,y,3.2,role,label=l,size='s')
    if wall: line(ax,[(46,y-5),(46,y+5)],'varie',lw=1.6)
text(ax,2,67,'1. On suppose : la liste finit','varie','s',ha='left')
row(59,'sujet',['2','3','5','7'])
text(ax,2,45,'2. Un premier de plus !','limite','s',ha='left')
row(37,'fixe',['','','',''])
disc(ax,56,37,3.2,'limite',label='?',size='s')
text(ax,2,23,'3. La liste ne finit pas','resultat','s',ha='left')
row(15,'resultat',['2','3','5','7'],wall=False)
arrow(ax,(44,15),(58,15),'resultat'); text(ax,63,15,'…','resultat','l')
save(fig,'05-167')
