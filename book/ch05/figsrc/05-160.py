import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
x0,x1=30,82
f=lambda v: x0+(v-1)/11*(x1-x0)
rows=[(58,'diviseurs de 1','sujet',[1]),(48,'diviseurs de 12','autre',[1,2,3,4,6,12]),
      (30,'multiples de 1','sujet',list(range(1,13))),(20,'multiples de 12','autre',[12])]
line(ax,[(f(1),12),(f(1),64)],'fixe',dash=True); line(ax,[(f(12),12),(f(12),64)],'fixe',dash=True)
for y,lab,role,vals in rows:
    text(ax,2,y,lab,role,'s',ha='left')
    for v in vals:
        common=(y<=48 and y>40 and v==1) or (y==58 and v==1) or (y==20) or (y==30 and v==12)
        disc(ax,f(v),y,2.0,'resultat' if common else role)
line(ax,[(x0,10),(x1,10)])
for v in range(1,13): ax.plot([f(v)]*2,[9,11],color=COL['fixe'],lw=0.8)
text(ax,f(1),5.5,'1','fixe','s'); text(ax,f(12),5.5,'12','fixe','s')
text(ax,42,58,'PGCD(1, 12) = 1','resultat','s',ha='left')
text(ax,f(12)-4,20,'PPCM(1, 12) = 12','resultat','s',ha='right')
save(fig,'05-160')
