import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(58)
s = 3.2; x0, y0 = 6, 10
m = 10*s; g = 10/math.tan(math.radians(25))*s
B=(x0,y0); T=(x0,y0+m); E=(x0+g,y0)
poly(ax,[B,E,T],'fixe')
line(ax,[B,T],'sujet',lw=1.8); line(ax,[T,E],'resultat',lw=1.8); line(ax,[B,E],'fixe',lw=0.9)
line(ax,[(x0,y0+3),(x0+3,y0+3),(x0+3,y0)],'fixe',lw=0.7)
r=14
line(ax,[(E[0]-r*math.cos(math.radians(a)),y0+r*math.sin(math.radians(a))) for a in range(0,26,3)],'varie',lw=1.0)
text(ax,E[0]-19,y0+2.8,'25°','varie','m')
text(ax,x0+3,y0+m/2+3,'mât','sujet','s',ha='left')
text(ax,x0+3,y0+m/2-1.5,'10 m','sujet','m',ha='left')
text(ax,x0+g*0.55,y0+m*0.5+9,'câble','resultat','m')
text(ax,x0+g*0.55,y0+m*0.5+4.5,'≈ 23,66 m','resultat','m')
text(ax,x0+g/2,y0-4,'sol','fixe','s')
save(fig,'31-003')
