import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,14,60,'ch. 11 : aires','sujet','s'); text(ax,44,60,'ch. 24 : systèmes','autre','s'); text(ax,74,60,'ch. 42 : parties','varie','s')
poly(ax,[(4,34),(18,34),(24,48),(10,48)],'sujet')
line(ax,[(33,36),(55,50)],'autre',lw=1.4); line(ax,[(33,50),(55,36)],'autre',lw=1.4)
for c,n in enumerate([1,3,3,1]):
    for r in range(n):
        y=42+(r-(n-1)/2)*5.2-2; x=62+c*6
        poly(ax,[(x,y),(x+4.4,y),(x+4.4,y+4.4),(x,y+4.4)],'varie')
text(ax,74,29,'8 cases','varie','s')
for x,r in [(14,'sujet'),(44,'autre'),(74,'varie')]:
    arrow(ax,(x,31) if x!=74 else (x,26),(44+(x-44)*0.4,17),r)
box(ax,12,4,64,12,'resultat',label='algèbre extérieure',size='m')
save(fig,'76-150')
