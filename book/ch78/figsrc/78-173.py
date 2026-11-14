import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,20,56,'rotation de 0,01','sujet','s')
vals=[['0,99995','-0,01'],['0,01','0,99995']]
for r in range(2):
    for c in range(2):
        v=vals[r][c].replace('-','−')
        box(ax,5+c*15,36-r*10,14,9,'sujet',label=v,size='s')
arrow(ax,(37,40.5),(51,40.5),'varie')
text(ax,44,45,r'$-\ I$','varie','m')
ev=[['0,00005','-0,01'],['0,01','0,00005']]
for r in range(2):
    for c in range(2):
        v=ev[r][c].replace('-','−'); off=(r!=c)
        box(ax,54+c*15,36-r*10,14,9,'varie' if off else 'fixe',label=v,size='s')
text(ax,68.5,56,'écart','varie','s')
text(ax,68.5,14,'hors diagonale :','varie','s')
text(ax,68.5,9,'antisymétrique','varie','s')
text(ax,20,14,'diagonale : très petite','fixe','s')
save(fig,'78-173')
