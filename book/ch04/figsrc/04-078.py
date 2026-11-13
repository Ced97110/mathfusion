import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
# carré 4 × 4 de carreaux de 5 mm, coin (6, 20)
x0,y0,c=6,20,5
poly(ax,[(x0,y0),(x0+4*c,y0),(x0+4*c,y0+4*c),(x0,y0+4*c)],'sujet')
for i in range(1,4):
    line(ax,[(x0+i*c,y0),(x0+i*c,y0+4*c)],'fixe',lw=0.3)
    line(ax,[(x0,y0+i*c),(x0+4*c,y0+i*c)],'fixe',lw=0.3)
text(ax,16,30,'aire 16','sujet','m').set_bbox(dict(boxstyle='square,pad=0.15',fc='white',ec='none'))
brace(ax,6,26,19,'fixe')
text(ax,16,15.5,'côté 4','sujet','s')
text(ax,16,51,'√16 = 4','encre','l')
text(ax,16,7,'racine < nombre','resultat','m')
line(ax,[(40,4),(40,56)],'fixe',dash=True)
# carrés emboîtés de côtés 16, 10, 4 centrés en (64, 28)
for s in (16,10,4):
    h=s/2
    line(ax,[(64-h,28-h),(64+h,28-h),(64+h,28+h),(64-h,28+h),(64-h,28-h)],'varie',dash=True)
arrow(ax,(71,35),(65.2,29.2),'varie')
ax.add_patch(Circle((64,28),1.2,color=COL['sujet'],zorder=6))
text(ax,64,15.5,'aire 0, côté 0','sujet','s')
text(ax,64,51,'√0 = 0','encre','l')
text(ax,64,43.5,'0 × 0 = 0','resultat','m')
text(ax,64,7,'racine = nombre','limite','m')
save(fig,'04-078')
