import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
cx,cy=44,45
for j in range(8):
    a=math.radians(22.5+45*j)
    line(ax,[(cx+3.6*math.cos(a),cy+3.6*math.sin(a)),(cx+34.5*math.cos(a),cy+34.5*math.sin(a))],'sujet',lw=0.8)
    for i in range(6):
        d=7+5.5*i
        disc(ax,cx+d*math.cos(a),cy+d*math.sin(a),1.9,'varie')
disc(ax,cx,cy,3.6,'sujet',label=r'$e$')
text(ax,44,85,r"$8 \times 6 = 48$ éléments d'ordre 7",'varie','m')
text(ax,44,4,r'chaque ligne : $e$ + 6 autres','sujet','s')
save(fig,'50-229')
