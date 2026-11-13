import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
cw=9.0; x0=(W-8*cw-7*1.5)/2; cx=lambda i:x0+cw/2+i*(cw+1.5)
text(ax,44,78,r'$x$ de 0 à 7','sujet','s')
for i in range(8): box(ax,cx(i)-cw/2,62,cw,9,'sujet',label=str(i))
tg={0:'sujet',2:'sujet',4:'varie',6:'sujet'}
for j in range(8):
    r=tg.get(j,'fixe')
    if j==5: box(ax,cx(j)-cw/2,16,cw,9,'limite',fill=False,label='5',dash=True)
    else: box(ax,cx(j)-cw/2,16,cw,9,r,label=str(j))
for i in range(8):
    j=(2*i)%8; r='varie' if j==4 else 'fixe'
    arrow(ax,(cx(i),62),(cx(j),26),r,lw=0.8)
text(ax,cx(4),10,'2 flèches','varie','s'); text(ax,cx(5)+8,10,'aucune','limite','s')
text(ax,44,3.5,r'valeurs de $2x$ modulo 8','fixe','s')
save(fig,'44-244')
