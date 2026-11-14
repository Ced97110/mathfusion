import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
rows=[(4,3,4,4),(5,4,3,5),(9,1,2,9),(7,5,2,7)]
for k,(m,r,q,mm) in enumerate(rows):
    y=66-k*13
    box(ax,4,y,34,9,'sujet',label=rf'$x\equiv {r}\ (\mathrm{{mod}}\ {m})$',size='s')
    arrow(ax,(38,y+4.5),(48,y+4.5),'varie')
    box(ax,48,y,36,9,'resultat',label=rf'$19={q}\times{m}+{r}$',size='s')
box(ax,4,6,80,10,'resultat',label=r'$x\equiv19\ (\mathrm{mod}\ 1260)$',size='s')
text(ax,44,22,r'$1260=4\times5\times9\times7$','fixe','s')
save(fig,'52-198')
