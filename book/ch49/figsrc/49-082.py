import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
# FG / K = G'
box(ax,3,36,24,14,'fixe',label='FG',size='l')
text(ax,15,31.5,'mots libres','fixe','s')
text(ax,34,43,'/','encre','xl')
box(ax,41,36,20,14,'varie',label='K',size='l')
text(ax,51,31.5,'mots égaux à 1','varie','s')
text(ax,67,43,'=','encre','xl')
box(ax,72,36,14,14,'sujet',label=r'$G^\prime$',size='l')
text(ax,79,31.5,'nommé','sujet','s')
# comparison with G
line(ax,[(79,28),(79,20)],'sujet',dash=True)
box(ax,3,6,40,12,'autre',label='G : groupe diédral',size='m')
text(ax,62,12,'même groupe ?','encre','s')
arrow(ax,(46,12),(53,12),'varie',both=True)
box(ax,72,6,14,12,'sujet',label=r'$G^\prime$',size='l')
line(ax,[(79,28),(79,19)],'sujet',dash=True)
save(fig,'49-082')
