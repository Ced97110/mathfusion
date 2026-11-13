import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
line(ax,[(4,49),(84,49)],'sujet',lw=1.2)
for i,t in enumerate(['4 choix','3 choix','2 choix','1 choix']):
    box(ax,6+20*i,50,16,10,'sujet',fill=False,label=t,size='s')
text(ax,44,65,'4 × 3 × 2 × 1 = 24','resultat','l')
for g in range(4):
    x0=4+21*g
    for r in range(6):
        y=14+4.2*r
        for c in range(4):
            box(ax,x0+4.5*c,y,4.5,3,'varie' if c==0 else 'fixe',lw=0.4,r=0.2)
    text(ax,13+21*g,42,'ABCD'[g]+' en 1er','varie','s')
brace(ax,4,22,12,'fixe',label='6 pour les 3 autres',down=True)
text(ax,62,7,'4 × 6 = 24 rangements','resultat','s')
save(fig,'01-050')
