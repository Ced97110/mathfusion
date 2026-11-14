import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
rows=[('prix','2,35 €'),('longueur','2,35 m'),('pourcentage','37 % = 0,37'),('volume','0,5 L')]
for i,(a,b) in enumerate(rows):
    y=44-i*13
    text(ax,3,y+4,a,'fixe','m',ha='left')
    box(ax,32,y,36,9,'sujet',label=b)
line(ax,[(72,48),(75,48),(75,8),(72,8)],'resultat',lw=1.0)
text(ax,80,28,'même virgule','resultat','s',rot=90)
save(fig,'08-091')
