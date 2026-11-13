import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
c=3.4; x0=3.2; y=26
for i in range(24): box(ax,x0+i*c,y,c,c,'fixe',lw=0.5,r=0.3)
for g in range(3): brace(ax,x0+g*8*c+0.4,x0+(g+1)*8*c-0.4,y+c+1,'sujet',label='8',down=False)
for g in range(2): brace(ax,x0+g*12*c+0.4,x0+(g+1)*12*c-0.4,y-1,'varie',label='12',down=True)
text(ax,44,48,'facteur commun de 8 et 12 : 4','fixe','s')
text(ax,44,12,r'$3\times8=2\times12$ : reste 0, jamais 1','limite','s')
save(fig,'52-230')
