import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax,x,y,r,role): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],lw=0.5,zorder=3))
fig,ax=canvas(56)
rows=[(50,1,'14 = 4 × 1 + 10',51),(35,2,'14 = 4 × 2 + 6',36),(20,3,'14 = 4 × 3 + 2',21)]
for y,n,lab,ty in rows:
    for i in range(14):
        role='fixe' if i<4*n else ('resultat' if n==3 else 'limite')
        dot(ax,34+3.6*i,y,1.1,role)
    for k in range(n): box(ax,32.4+14.4*k,y-2.4,14,4.8,'fixe',fill=False)
    text(ax,2,ty,lab,'encre','m',ha='left')
box(ax,46.8,47.6,35.6,4.8,'limite',fill=False)
box(ax,61.2,32.6,21.2,4.8,'limite',fill=False)
text(ax,2,46,'10 < 4 est faux','limite','s',ha='left')
text(ax,2,31,'6 < 4 est faux','limite','s',ha='left')
for x,y in [(47.1,48.2),(61.5,48.2),(61.5,33.2)]: box(ax,x,y,13.4,3.6,'varie',fill=False,dash=True)
box(ax,75.6,17.6,6.8,4.8,'resultat',fill=False)
text(ax,2,16,'2 < 4 est vrai','resultat','s',ha='left')
brace(ax,32.4,75.2,16.5,'fixe','q = 3 paquets')
brace(ax,75.6,82.4,16.5,'resultat','r = 2')
save(fig,'03-056')
