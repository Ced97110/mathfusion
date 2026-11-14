import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(46)
def row(y,n,role):
    for i in range(n):
        ax.add_patch(Rectangle((3+i*1.7,y),1.5,3,ec=COL[role],fc=FILL[role],lw=0.4,zorder=2))
row(36,48,'fixe'); row(22,24,'sujet'); row(8,12,'resultat')
text(ax,3,42.5,r'$|GL_2|=48$','fixe','m',ha='left')
text(ax,3,28.5,r'$|SL_2|=24$','sujet','m',ha='left')
text(ax,3,14.5,r'$|PSL_2|=12$','resultat','m',ha='left')
arrow(ax,(36,35),(36,26),'varie'); text(ax,39,30.5,'÷ 2','varie','m',ha='left')
arrow(ax,(36,21),(36,12),'varie'); text(ax,39,16.5,'centre {1, −1} : ÷ 2','varie','s',ha='left')
save(fig,'73-178')
