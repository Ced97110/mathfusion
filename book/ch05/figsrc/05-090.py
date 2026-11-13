import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
steps=['1. diviser','2. garder le reste','3. recommencer avec le reste']
ys=[64,44,24]
for y,s in zip(ys,steps): box(ax,14,y,44,10,'sujet',label=s,size='s')
for a,b in zip(ys,ys[1:]): arrow(ax,(36,a-0.3),(36,b+10.3),'varie',lw=1.4)
arrow(ax,(14.5,29),(14.5,69),'varie',curve=-0.25,lw=1.2)
# sortie
arrow(ax,(58.5,49),(64,49),'resultat',lw=1.4)
box(ax,64,44,22,10,'resultat',label='reste 0 : fin',size='s')
# barres des restes
base=22; sc=14/54
for i,r in enumerate([54,36,18,0]):
    x=64+i*6
    if r>0: ax.add_patch(Rectangle((x,base),5,r*sc,ec=COL['varie'],fc=FILL['varie'],lw=0.8,zorder=2))
    else: ax.plot([x,x+5],[base,base],color=COL['fixe'],lw=1.6,zorder=3)
    text(ax,x+2.5,base-2.6,str(r),'varie','s')
text(ax,75,base-8,'restes qui diminuent','varie','s')
save(fig,'05-090')
