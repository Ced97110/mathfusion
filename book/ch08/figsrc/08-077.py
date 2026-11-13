import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,44,52,r'$100 \div 27$ : on note les restes','encre','s')
vals=['19','1','10','19']; bw=15; g=6; x0=6; y=28
for i,v in enumerate(vals):
    x=x0+i*(bw+g); role='limite' if i==3 else 'sujet' if i==0 else 'fixe'
    box(ax,x,y,bw,9,role,label=v,size='m')
    if i<3: arrow(ax,(x+bw+0.3,y+4.5),(x+bw+g-0.3,y+4.5),'fixe')
xa=x0+bw/2; xb=x0+3*(bw+g)+bw/2
line(ax,[(xb,y+9.3),(xb,y+15),(xa+1.5,y+15)],'limite',lw=1.1)
arrow(ax,(xa,y+15),(xa,y+9.3),'limite',lw=1.1)
text(ax,xb,y-4,'déjà vu : on arrête','limite','s')
box(ax,6,6,15,9,'resultat',label='0',size='m')
text(ax,26,10.5,'reste 0 : on arrête aussi','resultat','s',ha='left')
save(fig,'08-077')
