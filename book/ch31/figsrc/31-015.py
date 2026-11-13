import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(56)
R=8; cy=34
panels=[(10,0.5,'2 points','fixe'),(38,1.0,'1 point','sujet'),(70,None,'0 point','fixe')]
dists=[0.5,1,2]
for (cx,_,lab,role),d in zip(panels,dists):
    disc(ax,cx,cy,R,'fixe',fill=False,lw=0.8)
    xl=cx+d*R
    line(ax,[(cx,cy),(xl,cy)],'fixe',lw=0.5,dash=True)
    line(ax,[(xl,cy-R-3),(xl,cy+R+3)],role,lw=1.9 if role=='sujet' else 1.1)
    if d==0.5:
        for sgn in (1,-1): disc(ax,xl,cy+sgn*R*math.sqrt(1-d*d),1.0,'fixe')
    if d==1: disc(ax,xl,cy,1.3,'sujet')
    text(ax,cx+d*R/2 if d<2 else cx+R*0.0,cy-R-8,f'à {d:g}'.replace('.',','),role,'s') if False else None
    text(ax,(cx-R+xl)/2,cy-R-7,lab,role,'s')
    text(ax,(cx-R+xl)/2,cy-R-11.5,f'droite à {d:g}'.replace('.',','),role,'s')
text(ax,38,cy+R+8,'tangente','sujet','m',weight='bold')
text(ax,44,4,'rayon du cercle : 1','encre','s')
save(fig,'31-015')
