import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
y1,y2=70,28
f=numberline(ax,8,68,y1,-5,5,every=5)
disc(ax,f(-5),y1,1.5,'sujet'); disc(ax,f(5),y1,1.5,'resultat')
brace(ax,f(-5),f(0),y1+5,'sujet',label='distance 5',down=False)
text(ax,f(5),y1+6,r'$|-5|=5$','resultat','s')
g=numberline(ax,8,68,y2,-5,5,every=5)
disc(ax,g(5),y2,1.5,'sujet'); disc(ax,g(-5),y2,1.5,'autre')
brace(ax,g(0),g(5),y2+5,'sujet',label='distance 5',down=False)
text(ax,g(-5)+8,y2+6,r'$-|5|=-5$','autre','s')
text(ax,44,49,r'$5\neq-5$ : réponses différentes','limite','s')
save(fig,'13-053')
