import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
for x in (12,30): line(ax,[(x,12),(x,48)],'sujet',lw=1.4)
for y in range(14,48,5): line(ax,[(12,y),(30,y)],'fixe',lw=0.7)
VP=(66,44)
box(ax,46,10,40,46,'fixe',fill=False,lw=0.8)
line(ax,[(47,VP[1]),(85,VP[1])],'fixe',lw=0.8)
for sx in (53,79): line(ax,[(sx,11),VP],'sujet',lw=1.4)
for k in range(6):
    t=0.8**k*1.0; y=VP[1]-33*t
    xl=VP[0]+(53-VP[0])*t; xr=VP[0]+(79-VP[0])*t
    line(ax,[(xl,y),(xr,y)],'fixe',lw=0.7)
disc(ax,*VP,1.3,'varie')
text(ax,66,52,'point de rencontre','varie','s')
text(ax,84,41,'horizon','fixe','s',ha='right')
text(ax,21,52,'rails parallèles','sujet','s')
text(ax,21,5,'sur le sol','encre','m'); text(ax,66,5,'sur la photo','encre','m')
save(fig,'80-013')
