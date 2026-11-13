import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig,ax=canvas(78)
cx=44; oy=40; sx=11; sy=1.8; s=5
line(ax,[(4,oy),(84,oy)],'fixe')
xs=np.linspace(-3,3,80)
line(ax,[(cx+x*sx,oy+x*x*sy+s) for x in xs],'varie',lw=1.2,dash=True)
line(ax,[(cx+x*sx,oy+x*x*sy-s) for x in xs],'varie',lw=1.2)
line(ax,[(cx+x*sx,oy+x*x*sy) for x in xs],'sujet',lw=1.6)
r=(s/sy)**0.5
for x in (-r,r): disc(ax,cx+x*sx,oy,1.5,'resultat')
disc(ax,cx,oy,1.8,'sujet')
arrow(ax,(cx+8,oy),(cx+8,oy+s*1+0.0),'varie') if False else None
text(ax,44,66,'D = 0 : la frontière','sujet','m')
rows=[('varie',True,'plus haut : aucun point'),('sujet',False,'sur l’axe : un point'),('varie',False,'plus bas : deux points')]
for i,(rl,d,t) in enumerate(rows):
    y=26-i*7
    ax.plot([6,16],[y,y],color=COL[rl],lw=1.4 if i!=1 else 1.8,ls='--' if d else '-',zorder=3)
    text(ax,19,y,t,rl,'s',ha='left')
save(fig,'23-075')
