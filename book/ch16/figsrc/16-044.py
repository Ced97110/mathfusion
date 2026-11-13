import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
import math
for y,l in [(52,r'$x+7=11$'),(30,r'$x-5=-1$'),(8,r'$x=4$')]:
    box(ax,3,y,36,12,'sujet',label=l,size='m')
    p=(39,y+6); c=(66,38); d=math.hypot(c[0]-p[0],c[1]-p[1]); q=(c[0]-9*(c[0]-p[0])/d,c[1]-9*(c[1]-p[1])/d)
    arrow(ax,p,q,'resultat')
disc(ax,66,38,8,'resultat',label='4',size='xl')
text(ax,66,25,'même solution','resultat','s')
save(fig,'16-044')
