import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
g=10
line(ax,[(4,g),(62,g)],'fixe',lw=1.2)
box(ax,10,g,16,18,'sujet'); box(ax,42,g,16,45,'autre')
line(ax,[(8,g+18),(70,g+18)],'fixe',dash=True)
arrow(ax,(66,g+18),(66,g+45),'varie')
text(ax,77,g+18,'100 %','fixe','s'); text(ax,77,g+45,'250 %','autre','m')
text(ax,18,5,'avant : 20 cm','sujet','s'); text(ax,50,5,'après : 50 cm','autre','s')
save(fig,'09-108')
