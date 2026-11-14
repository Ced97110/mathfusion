import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,60,'sin(cθ) = k : 2c solutions','sujet','m')
sols={1:[30,150],2:[15,75,195,255],3:[10,50,130,170,250,290]}
x0,x1=24,66
f=lambda a: x0+a/360*(x1-x0)
for i,c in enumerate((1,2,3)):
    y=46-i*17
    text(ax,10,y,f'c = {c}','fixe','m')
    line(ax,[(x0,y),(x1,y)],'fixe')
    for a in (0,360): line(ax,[(f(a),y-1.2),(f(a),y+1.2)],'fixe')
    for a in sols[c]: disc(ax,f(a),y,1.3,'resultat')
    text(ax,78,y,f'{2*c} solutions','resultat','s')
text(ax,f(0),8,'0°','fixe','s'); text(ax,f(360),8,'360°','fixe','s')
save(fig,'32-099')
