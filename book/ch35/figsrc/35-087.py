import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
cs=((3,'varie',[36.87,143.13],'c = 3','25 − 9 = 16 > 0','2 solutions'),
    (5,'resultat',[90],'c = 5','25 − 25 = 0','1 solution'),
    (6,'limite',[],'c = 6','25 − 36 = −11 < 0','0 solution'))
y0=36;k=2.2
for i,(c,role,ts,l1,l2,l3) in enumerate(cs):
    px=3+i*29.5; f=lambda t:px+t/360*25
    line(ax,[(px,y0),(px+25,y0)],'fixe',lw=0.6)
    line(ax,[(f(t),y0+k*5*math.sin(math.radians(t))) for t in range(0,361,4)],'sujet',lw=1.1)
    line(ax,[(px,y0+c*k),(px+25,y0+c*k)],role,lw=1.1)
    for t in ts: disc(ax,f(t),y0+c*k,0.9,'encre')
    text(ax,px+12.5,23,l1,role,'s'); text(ax,px+12.5,18,l2,role,'s'); text(ax,px+12.5,12,l3,role,'m',weight='bold')
text(ax,44,58,r'$a=3,\ b=4,\ a^2+b^2=25$','encre','m')
save(fig,'35-087')
