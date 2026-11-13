import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
def row(y,a,o,els,lab):
    box(ax,3,y,22,10,'sujet',label=a)
    text(ax,14,y-3.5,f'ordre {o}','varie','s')
    arrow(ax,(26,y+5),(33,y+5),'varie')
    x=34
    for e in els:
        box(ax,x,y,16,10,'resultat',label=e,size='s'); x+=17.5
    text(ax,34,y+14.5,lab,'resultat','s',ha='left')
row(8,'(1 2)',2,['(1)','(1 2)'],'sous-groupe de 2 éléments')
row(32,'(1 2 3)',3,['(1)','(1 2 3)','(1 3 2)'],'sous-groupe de 3 éléments')
save(fig,'46-279')
