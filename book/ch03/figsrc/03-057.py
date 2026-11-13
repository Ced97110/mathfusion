import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
for x,s,r in [(14,r'$n$','sujet'),(24,'=','encre'),(34,r'$d$','varie'),(44,'×','encre'),(54,r'$q$','varie'),(64,'+','encre'),(74,r'$r$','resultat')]:
    pass
fig,ax=canvas(62)
for x,s,r in [(14,r'$n$','sujet'),(24,'=','encre'),(34,r'$d$','varie'),(44,'×','encre'),(54,r'$q$','varie'),(64,'+','encre'),(74,r'$r$','resultat')]:
    text(ax,x,56,s,r,'l')
for x,s,r in [(14,'14','sujet'),(34,'4','varie'),(54,'3','varie'),(74,'2','resultat')]:
    text(ax,x,49,s,r,'m')
f=numberline(ax,6,82,24,0,16,1,labels=False,arrow_right=False)
for v in (0,4,8,12,16): disc(ax,f(v),24,1.0,'fixe',fill=False)
ax.add_patch(Circle((f(14),24),1.2,ec=COL['sujet'],fc=COL['sujet'],zorder=4))
for a,b in [(0,4),(4,8),(8,12)]: arrow(ax,(f(a),24.8),(f(b),24.8),'varie',curve=-0.5)
# 4e saut impossible : pointillé rouge de 12 à 16
ax.add_patch(FancyArrowPatch((f(12),24.8),(f(16),24.8),arrowstyle='-|>',mutation_scale=7,lw=1.0,ls='--',
             color=COL['limite'],connectionstyle='arc3,rad=-0.5',zorder=4,shrinkA=0,shrinkB=0))
line(ax,[(f(12),24),(f(14),24)],'resultat',lw=2.5)
text(ax,34,35,'3 sauts de 4 : on arrive à 12','varie','s')
text(ax,f(14),35,'pas de 4e saut','limite','s')
text(ax,61.5,19.5,'reste 2','resultat','s',ha='right')
box(ax,63,18,19,3,'resultat')
line(ax,[(82,17),(82,22)],'limite',lw=1.5)
text(ax,72.5,13,r'$0 \leq r < d$','resultat','m')
save(fig,'03-057')
