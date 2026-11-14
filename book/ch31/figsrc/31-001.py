import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(52)
s = 15.0; x0, y0 = 6, 12
w = 4*s; h = 4*math.tan(math.radians(30))*s
A=(x0,y0); B=(x0+w,y0); C=(x0+w,y0+h)
poly(ax,[A,B,C],'fixe')
line(ax,[A,B],'sujet',lw=1.8); line(ax,[A,C],'resultat',lw=1.8)
line(ax,[(B[0]-3,y0),(B[0]-3,y0+3),(B[0],y0+3)],'fixe',lw=0.7)
pts=[(A[0]+11*math.cos(math.radians(a)),y0+11*math.sin(math.radians(a))) for a in np.linspace(0,30,12)] if False else [(A[0]+11*math.cos(math.radians(a)),y0+11*math.sin(math.radians(a))) for a in range(0,31,3)]
line(ax,pts,'varie',lw=1.0)
text(ax,A[0]+14,y0+2.6,'30°','varie','m')
text(ax,x0+w/2,y0-4,'côté horizontal : 4 m','sujet','s')
text(ax,x0+w*0.42,y0+h*0.5+5,'poutre','resultat','m',rot=0)
text(ax,x0+w*0.42,y0+h*0.5+9.5,'≈ 4,62 m','resultat','m')
text(ax,B[0]+1,y0+h+4,'faîte','fixe','s',ha='center')
text(ax,70,y0+2.5,'4 / cos 30°','encre','s',ha='left') if False else None
save(fig,'31-001')
