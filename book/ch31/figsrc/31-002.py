import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
s = 15.0; x0, y0 = 8, 10
pole = 3*s; sh = 3/math.tan(math.radians(40))*s
P0=(x0,y0); T=(x0,y0+pole); E=(x0+sh,y0)
poly(ax,[P0,E,T],'fixe')
line(ax,[P0,T],'sujet',lw=1.8); line(ax,[P0,E],'resultat',lw=1.8)
line(ax,[T,E],'varie',lw=0.9,dash=True)
line(ax,[(x0,y0+3),(x0+3,y0+3),(x0+3,y0)],'fixe',lw=0.7)
r=12
line(ax,[(E[0]-r*math.cos(math.radians(a)),y0+r*math.sin(math.radians(a))) for a in range(0,41,4)],'varie',lw=1.0)
text(ax,E[0]-17,y0+3,'40°','varie','m')
text(ax,x0+3,y0+pole/2,'poteau','sujet','s',ha='left')
text(ax,x0+3,y0+pole/2-4,'3 m','sujet','m',ha='left')
text(ax,x0+sh/2,y0-4,'ombre ≈ 3,58 m','resultat','m')
text(ax,x0+sh*0.62,y0+pole*0.55+4,'rayon du soleil','varie','s',ha='left') if False else text(ax,x0+sh*0.55,y0+pole*0.48+5,'rayon','varie','s'); 
save(fig,'31-002')
