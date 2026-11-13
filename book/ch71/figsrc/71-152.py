import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
cx=[40,68]
text(ax,cx[0],61,r'$i=1$','encre','m'); text(ax,cx[1],61,r'$i=2$','encre','m')
rows=[(50,'sujet',r'$b_i$',['2','2']),(38,'varie',r'$s_i$',['3','1']),(26,'resultat',r'$b_is_i^2$',[r'$2\times9=18$',r'$2\times1=2$'])]
for y,role,lab,vals in rows:
    text(ax,10,y,lab,role,'m')
    for c,v in zip(cx,vals): box(ax,c-12,y-4.5,24,9,role,label=v)
for c in cx: arrow(ax,(c,45.5),(c,42.5),'fixe',lw=0.7); arrow(ax,(c,33.5),(c,30.5),'fixe',lw=0.7)
arrow(ax,(40,21.5),(48,15),'resultat'); arrow(ax,(68,21.5),(60,15),'resultat')
box(ax,24,3,56,12,'resultat',label=r'$18+2=20$',size='l',weight='bold')
save(fig,'71-152')
