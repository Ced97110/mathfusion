import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
text(ax,17,87,r'$(a,b)$','sujet','l',weight='bold')
text(ax,71,87,r'$(b,r)$','autre','l',weight='bold')
for y,c1,c2,p in [(68,'(18, 12)','(12, 6)','6'),(30,'(252, 198)','(198, 54)','18')]:
    box(ax,2,y+4,30,10,'sujet',label=c1,size='m')
    box(ax,56,y+4,30,10,'autre',label=c2,size='m')
    arrow(ax,(33,y+9),(55,y+9),'varie',lw=1.6)
    text(ax,44,y+13,'une division','varie','s')
    box(ax,2,y-14,30,9,'resultat',label='PGCD = '+p,size='m')
    box(ax,56,y-14,30,9,'resultat',label='PGCD = '+p,size='m')
    line(ax,[(17,y+3.5),(17,y-4.5)],'fixe'); line(ax,[(71,y+3.5),(71,y-4.5)],'fixe')
    line(ax,[(34,y-8.2),(54,y-8.2)],'resultat',lw=1.2); line(ax,[(34,y-10.8),(54,y-10.8)],'resultat',lw=1.2)
save(fig,'05-085')
