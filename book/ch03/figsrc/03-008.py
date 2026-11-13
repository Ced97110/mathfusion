import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
for x0 in (14,50):
    for r in range(4):
        for c in range(6): box(ax,x0+5*c,22+5*r,5,5,'sujet',r=0.3,lw=0.5)
text(ax,8,32,'a = 4','fixe','s')
brace(ax,14,44,44,'fixe',label='b = 6',down=False)
pts=[(16.5,24.5),(41.5,24.5),(41.5,29.5),(19.5,29.5)]
line(ax,[(16.5,24.5),(41.5,24.5),(41.5,29.5),(16.5,29.5),(16.5,34.5),(41.5,34.5),(41.5,39.5),(19.5,39.5)],'varie',lw=1.0)
arrow(ax,(19.5,39.5),(16.5,39.5),'varie')
disc(ax,16.5,24.5,0.8,'varie')
for x0 in (14,50):
    for r in range(4):
        for c in range(6):
            if (x0,r,c) not in ((14,0,0),(14,3,0)): ax.add_patch(Circle((x0+5*c+2.5,22+5*r+2.5),0.75,ec='none',fc=COL['sujet'],zorder=3.6))
text(ax,29,16,'un par un : 24\nchaque carreau, une fois','varie','s')
for y,t in ((24.5,'6'),(29.5,'12'),(34.5,'18'),(39.5,'24')):
    arrow(ax,(50.5,y),(79.5,y),'varie'); text(ax,82,y,t,'varie','s',ha='left')
text(ax,65,16,'rangée par rangée : 24\nchaque carreau, une fois','varie','s')
text(ax,44,5.5,'a × b = 4 × 6 = 24','resultat','m',weight='bold')
save(fig,'03-008')
