import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
def row(y,vals,title,sub,hl):
    text(ax,44,y+16,title,'sujet','s')
    f=numberline(ax,6,72,y,0,24,1,labels=False,arrow_right=True)
    for v in vals:
        r='resultat' if v==hl else 'sujet'
        disc(ax,f(v),y,1.7,r)
        text(ax,f(v),y-5,str(v),r,'s',weight='bold' if v==hl else 'normal')
    text(ax,44,y+10.5,sub,'fixe','s')
    return f
f=row(48,[1,2,3,6],'par la division : le plus grand','diviseurs communs de 12 et 18',6)
row(10,[6,12,18,24],'par l\'addition : le plus petit','combinaisons strictement positives',6)
arrow(ax,(f(6),40),(f(6),33),'resultat',both=True); text(ax,f(6)+3,36.5,'même nombre : 6','resultat','s',ha='left')
save(fig,'05-105')
