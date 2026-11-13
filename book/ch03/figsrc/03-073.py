import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tile(ax,x,y,t,role,fill=True,dash=False,lw=0.5):
    box(ax,x,y,t,t,role,fill=fill,r=min(0.3,t/10),lw=lw,dash=dash)
def grid(ax,x,y,nr,nc,t,role):
    for i in range(nr):
        for j in range(nc): tile(ax,x+j*t,y+i*t,t,role)

fig,ax=canvas(80)
text(ax,4,68,'addition','encre','s',rot=90); text(ax,4,36,'multiplication','encre','s',rot=90)
line(ax,[(2,57),(76,57)],'fixe',lw=0.7,dash=True)
text(ax,13,68,'7 + 0','sujet','m')
for j in range(7): tile(ax,22+4*j,66,4,'sujet')
text(ax,53,68,'= 7, inchangé','resultat','s',ha='left')
text(ax,13,46,'7 × 1','sujet','m')
for j in range(7): tile(ax,22+4*j,44,4,'sujet')
box(ax,21,43,30,6,'varie',fill=False,lw=1.0,r=0.5)
text(ax,53,46,'= 7, inchangé','resultat','s',ha='left')
text(ax,13,26,'7 × 0','limite','m')
for j in range(7): tile(ax,22+4*j,24,4,'limite',fill=False,dash=True,lw=0.8)
line(ax,[(22,24),(50,28)],'limite')
text(ax,53,26,'= 0, détruit','limite','s',ha='left')
line(ax,[(78,42),(78,72)],'resultat',lw=1.0); line(ax,[(76,42),(78,42)],'resultat',lw=1.0); line(ax,[(76,72),(78,72)],'resultat',lw=1.0)
text(ax,82,57,'élément neutre','resultat','s',rot=90)
save(fig,'03-073')
