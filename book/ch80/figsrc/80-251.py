import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
xs=(20,43,66)
for i,x in enumerate(xs):
    text(ax,x+10,72,'contrôle %d'%(i+1),'encre','s')
    box(ax,x,56,20,10,'sujet',label=str((12,19,27)[i]))
    box(ax,x,14,20,10,'resultat',label=str((12,7,8)[i]))
    arrow(ax,(x+4,55),(x+4,25),'varie')
    text(ax,x+6.5,40,('rien avant','19 − 12','27 − 19')[i],'varie','s',ha='left')
text(ax,2,63,r'totaux $g$','sujet','s',ha='left')
text(ax,2,19,r'points $f$','resultat','s',ha='left')
save(fig,'80-251')
