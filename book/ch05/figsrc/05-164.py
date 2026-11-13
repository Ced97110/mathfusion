import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
x0=16; u=5.0
f=lambda v: x0+(v-204)*u
rows=[(46,'2',[204,206,208,210,212,214,216]),(37,'3',[204,207,210,213,216]),(28,'5',[205,210,215]),(19,'7',[210])]
line(ax,[(f(210),12),(f(210),54)],'resultat',dash=True)
line(ax,[(f(211),12),(f(211),54)],'limite',dash=True)
for y,lab,vals in rows:
    text(ax,4,y,lab,'sujet','m',weight='bold')
    line(ax,[(x0-2,y),(f(217)-2,y)],'fixe',lw=0.5)
    for v in vals: disc(ax,f(v),y,1.7,'resultat' if v==210 else 'sujet')
text(ax,f(210)-0.8,58,'210','resultat','s',ha='right')
text(ax,f(211)+0.8,58,'211','limite','s',ha='left')
text(ax,f(204),8,'204','fixe','s'); text(ax,f(216),8,'216','fixe','s')
text(ax,f(211),3,'aucune ligne en 211','limite','s')
text(ax,4,58,'multiples de','sujet','s',ha='left')
save(fig,'05-164')
