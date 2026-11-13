import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
L=60; x0=14
for row,(n,seg,role,y,t1,t2) in enumerate([(10,12,'sujet',44,'15 × 8 = 120','10 tours de 12'),(14,60,'autre',20,'15 × 56 = 840','14 tours de 60')]):
    w_=L/n
    for i in range(n): box(ax,x0+i*w_,y,w_,6,role,r=0.3,lw=0.6)
    text(ax,x0,y+10,t1,role,'m',ha='left')
    text(ax,x0+L,y+10,t2,role,'s',ha='right')
line(ax,[(x0+L,14),(x0+L,53)],'resultat',dash=True)
text(ax,x0+L+2,10,'retour à 0','resultat','s',ha='right')
text(ax,x0-1,47,'0','fixe','s',ha='right'); text(ax,x0-1,23,'0','fixe','s',ha='right')
text(ax,44,61,'au pas 15, les deux cases valent 0','resultat','s')
save(fig,'45-242')
