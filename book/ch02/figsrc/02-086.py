import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(82)
text(ax,22,78,'pour 43, 16, 27','resultat','s'); text(ax,66,78,'pour tout nombre','sujet','s')
for y,a,b in ((68,'43+16 = 16+43 = 59','a + b = b + a'),(58,'(43+16)+27 = 43+(16+27)','(a+b)+c = a+(b+c)'),(48,'43 + 0 = 43','a + 0 = a')):
    text(ax,22,y,a,'resultat','s'); text(ax,66,y,b,'sujet','m'); arrow(ax,(39,y),(51,y),'varie')
f=numberline(ax,4,84,24,-10,50,step=10,labels=False,role='fixe',arrow_right=False)
arrow(ax,(84,24),(86,24),'fixe'); arrow(ax,(8,24),(3,24),'fixe')
text(ax,f(0),19,'0','fixe','s')
box(ax,4,26.5,80,1.6,'sujet',fill=True,r=0.6)
text(ax,44,33,'a, b, c : tout point','sujet','s')
for v in (16,27,43):
    disc(ax,f(v),24,1.2,'resultat'); text(ax,f(v),19,str(v),'resultat','s')
save(fig,'02-086')
