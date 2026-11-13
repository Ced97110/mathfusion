import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
def solid(x,y,r,role):
    ax.add_patch(Circle((x,y),r,fc=COL[role],ec=COL[role],lw=0.5,zorder=3))
line(ax,[(44,26),(44,88)],'fixe',lw=0.6,dash=True)
text(ax,22,84,'groupes de 4 donnés','varie','s'); text(ax,65,84,'4 parts données','varie','s')
text(ax,22,78,'combien de groupes ?','varie','s'); text(ax,65,78,'combien par part ?','varie','s')
for k,y in enumerate((66,57,48)):
    box(ax,6,y,18,6,'sujet')
    for x in (9.5,13.5,17.5,21.5): solid(x,y+3,1.2,'sujet')
    text(ax,28,y+3,str(k+1),'sujet','s')
for x in (48,57,66,75):
    box(ax,x,48,7,18,'autre')
    for y in (52,57,62): solid(x+3.5,y,1.2,'autre')
for x in (8,12): solid(x,41,1.2,'fixe')
text(ax,27,41,'2 : pas un groupe','fixe','s')
for x in (50,54): solid(x,41,1.2,'fixe')
text(ax,71,41,'2 : non partagés','fixe','s')
text(ax,22,33,'3 groupes','resultat','m'); text(ax,65,33,'3 par part','resultat','m')
text(ax,44,20,'même calcul : 14 ÷ 4','encre','l'); text(ax,44,10,'question différente','encre','m')
save(fig,'03-050')
