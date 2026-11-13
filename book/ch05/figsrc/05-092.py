import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
box(ax,2,76,48,10,'fixe',label=r'le reste de $a\div b$',size='m')
text(ax,59,85,'s\'écrit','encre','s')
box(ax,68,76,18,10,'varie',label=r'$r$',size='l',lw=1.4)
arrow(ax,(50.5,81),(67.5,81),'varie',lw=1.4)
text(ax,2,66,'même lettre, valeur qui change :','encre','s',ha='left')
for i,(p,r) in enumerate([('252, 198',54),('198, 54',36),('54, 36',18),('36, 18',0)]):
    y=50-13*i+4
    a,b=p.split(', ')
    box(ax,2,y,34,10,'sujet',label=rf'${a}\div{b}$',size='m')
    arrow(ax,(37,y+5),(52,y+5),'varie',lw=1.2)
    box(ax,53,y,33,10,'varie',label=rf'$r={r}$',size='m')
save(fig,'05-092')
