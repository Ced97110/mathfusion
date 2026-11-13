import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
text(ax,22,66,'de quoi est-il fait ?','limite','s'); line(ax,[(9,66),(35,66)],'limite',lw=1.0)
arrow(ax,(37,66),(49,66),'varie')
text(ax,66,66,'que fait-on avec lui ?','resultat','s')
for i in range(5):
    for j in range(5):
        ax.add_patch(Rectangle((6+5*i,24+5*j),5,5,ec=COL['autre'],fc='none',lw=0.4,zorder=1))
for i,j in [(0,1),(0,3),(1,0),(1,4),(3,0),(3,4),(4,1),(4,3)]:
    disc(ax,8.5+5*i,26.5+5*j,1.0,'resultat')
line(ax,[(18.5,38.5),(18.5,46.5),(22.4,46.5)],'varie',lw=1.0)
arrow(ax,(21.4,46.5),(22.5,46.5),'varie',lw=1.0)
disc(ax,18.5,36.5,2.0,'autre',label='C',size='s',lw=1.0)
text(ax,19,18,'cavalier = ses coups','fixe','s')
text(ax,19,12,'bois ou plastique : égal','fixe','s')
for name,ly,by,shape in (('boîtes',57,46,'sq'),('pommes',39,28,'ci')):
    text(ax,46,ly,name,'fixe','s',ha='left')
    for k,x in enumerate((46,56,66,76)):
        box(ax,x,by,8,8,'fixe')
        for n in range(k):
            cx=x+4+(n-(k-1)/2)*2.2; cy=by+4
            if shape=='sq': ax.add_patch(Rectangle((cx-0.9,cy-0.9),1.8,1.8,fc=COL['fixe'],ec=COL['fixe'],lw=0.3,zorder=3))
            else: ax.add_patch(Circle((cx,cy),0.9,fc=COL['fixe'],ec=COL['fixe'],lw=0.3,zorder=3))
    ay=by-1
    for a in (50,60,70): arrow(ax,(a,ay),(a+10,ay),'varie',curve=0.3)
text(ax,65,21,'même règle : +1','resultat','s')
text(ax,44,5,'défini par ses règles','resultat','m')
save(fig,'01-024')
