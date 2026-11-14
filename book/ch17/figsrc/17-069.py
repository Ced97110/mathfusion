import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(86)
text(ax,44,81,r'$\times(-8)$ = $\times 8$ puis $\times(-1)$','varie','m')
rows=((66,'3','<','7','fixe'),(40,'24','<','56','fixe'),(14,'-24','>','-56','varie'))
for y,a,s,b,r in rows:
    box(ax,12,y,18,9,'sujet',label=f'${a}$'); text(ax,44,y+4.5,f'${s}$',r,'l'); box(ax,58,y,18,9,'sujet',label=f'${b}$')
arrow(ax,(44,64),(44,52),'varie'); text(ax,48,58,r'$\times 8$ : ordre gardé','fixe','s',ha='left')
arrow(ax,(44,38),(44,26),'varie'); text(ax,48,32,r'$\times(-1)$ : ordre retourné','varie','s',ha='left')
save(fig,'17-069')
