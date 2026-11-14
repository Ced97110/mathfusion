import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
cx=[12,34,56]; X=76
for x,h in zip(cx,['porte','mode nuit','fenêtre']): text(ax,x,52,h,'encre','s')
text(ax,X,52,'alarme','encre','s')
R=[(36,[1,0,0],'silence'),(24,[1,1,0],'sonne'),(12,[0,None,1],'sonne')]
for y,st,res in R:
    for x,s in zip(cx,st):
        if s is None:
            ax.add_patch(Circle((x,y),3.2,ec=COL['fixe'],fc='none',lw=0.8,ls='--',zorder=2)); text(ax,x,y,'?','fixe','s')
        else: disc(ax,x,y,3.2,'sujet',fill=bool(s))
    text(ax,X,y,res,'resultat' if res=='sonne' else 'fixe','m',weight='bold')
text(ax,2,6,'plein : ouverte ou activé','fixe','s',ha='left'); text(ax,2,2,'vide : fermée ou éteint · pointillé : non précisé','fixe','s',ha='left')
save(fig,'80-016')
