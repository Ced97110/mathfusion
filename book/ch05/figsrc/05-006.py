import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tiles(ax,x,y,rows,cols,t,role="sujet"):
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(Rectangle((x+c*t,y+r*t),t,t,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))

fig,ax=canvas(84)
C=[16,44,72]
for c,s in zip(C,['carreaux','bus','planches']): text(ax,c,79,s,'encre','m',weight='bold')
# carreaux : 3 rangées de 4
tiles(ax,C[0]-6,52,3,4,3)
brace(ax,C[0]-6,C[0]+6,62,'fixe',label='12 carreaux',down=False)
text(ax,C[0],47,r'$3 \times 4$','sujet','m')
# bus : 3 passages de 4 min, 2 passages de 6 min
for i in range(3): box(ax,C[1]-12+i*8,57,8,5,'sujet',r=0.4)
text(ax,C[1],53,r'$3 \times 4$','sujet','m')
for i in range(2): box(ax,C[1]-12+i*12,44,12,5,'autre',r=0.4)
text(ax,C[1],40,r'$2 \times 6$','autre','m')
brace(ax,C[1]-12,C[1]+12,63,'fixe',label='12 min',down=False)
# planche : 2 morceaux de 6 cm
for i in range(2): box(ax,C[2]-12+i*12,52,12,6,'sujet',r=0.4)
brace(ax,C[2]-12,C[2]+12,59,'fixe',label='12 cm',down=False)
text(ax,C[2],47,r'$2 \times 6$','sujet','m')
for c in C: arrow(ax,(c,36),(44+(c-44)*0.4,26),'resultat')
box(ax,10,9,68,16,'resultat',label=r'$12 = a \times b$',size='l',weight='bold')
save(fig,'05-006')
