import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import matplotlib.patches as mp
fig,ax=canvas(74)
rows=[(62,'x1','sujet'),(40,'x2','autre'),(18,'x3','fixe')]
box(ax,3,56.5,16,11,'sujet',label=r'$x_1$'); box(ax,3,34.5,16,11,'autre',label=r'$x_2$'); box(ax,3,12.5,16,11,'fixe',label=r'$x_1x_2$')
for y in (62,40,18): arrow(ax,(19,y),(40,y),'varie')
text(ax,29.5,66.5,r'$\eta$','varie','m')
text(ax,44,62,'quart de tour','sujet','s',ha='left'); text(ax,44,40,'réflexion','autre','s',ha='left')
text(ax,44,18,'quart de tour, puis réflexion','encre','s',ha='left')
for y in (62,40): poly(ax,[(74,y-5),(84,y-5),(84,y+5),(74,y+5)],'fixe')
ax.add_patch(mp.Arc((79,62),6,6,theta1=40,theta2=320,color=COL['sujet'],lw=1.0,zorder=4))
arrow(ax,(81.5,60.2),(82.3,61.4),'sujet')
line(ax,[(79,35.5),(79,44.5)],'autre',dash=True); arrow(ax,(75.5,40),(82.5,40),'autre',both=True)
text(ax,44,6,'une seule image possible','resultat','s',ha='left')
save(fig,'49-062')
