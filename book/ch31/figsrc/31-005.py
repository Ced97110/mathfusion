import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
k=1.1547; sc=5.0; x0=14
text(ax,44,74,'même multiplicateur : × 1,1547','varie','m')
for i,L in enumerate([4,6,10]):
    y=56-i*20
    box(ax,x0,y,L*sc,6,'sujet'); box(ax,x0,y-8,L*sc*k,6,'resultat')
    text(ax,x0-2,y+3,f'{L} m','sujet','s',ha='right')
    text(ax,x0+L*sc*k+2,y-5,f'{L*k:.2f}'.replace('.',',')+' m','resultat','s',ha='left')
    arrow(ax,(x0+L*sc-0.5,y+0.5),(x0+L*sc*k-0.5,y-2),'varie',lw=0.9)
text(ax,x0-2,4,'côté','sujet','s',ha='right') if False else None
text(ax,44,3,'vert = poutre, bleu = côté horizontal','encre','s')
save(fig,'31-005')
