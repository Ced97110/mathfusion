import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(c,R,a0,a1,n=60): return [(c[0]+R*math.cos(a0+(a1-a0)*i/n), c[1]+R*math.sin(a0+(a1-a0)*i/n)) for i in range(n+1)]
fig,ax=canvas(62)
O=(34,10); u=9
arrow(ax,(8,O[1]),(82,O[1]),'fixe',lw=0.8); arrow(ax,(O[0],4),(O[0],58),'fixe',lw=0.8)
p=(O[0]+2*u,O[1]+3*u)
al=math.atan2(3,2)
# quarter turn between the two axes (pi/2), gray
line(ax,arc(O,26,0,math.pi/2),'fixe',lw=0.8,dash=True)
text(ax,O[0]+26+5,O[1]+4,r'$\frac{\pi}{2}$','fixe','s')
# point 1 on the real axis, and the point a+bi
disc(ax,O[0]+u,O[1],1.0,'fixe'); text(ax,O[0]+u,O[1]-3.2,'1','fixe','s')
line(ax,[(p[0],O[1]),p],'fixe',dash=True); line(ax,[(O[0],p[1]),p],'fixe',dash=True)
text(ax,p[0],O[1]-3.2,r'$a$','fixe','s'); text(ax,O[0]-3,p[1],r'$b$','fixe','s')
arrow(ax,O,p,'sujet',lw=1.3); text(ax,p[0]+8,p[1]-1,r'$a+bi$','sujet','m')
# theta: from the real axis (point 1) to the vector a+bi
pts=arc(O,17,0,al)
line(ax,pts[:-3],'varie',lw=1.6); arrow(ax,pts[-4],pts[-1],'varie',lw=1.6)
text(ax,O[0]+12*math.cos(al/2)+3,O[1]+12*math.sin(al/2)-0.5,r'$\theta$','varie','m')
text(ax,64,54,'multiplier par $a+bi$','encre','s')
text(ax,64,49,'tourne le plan de $\\theta$','varie','s')
text(ax,64,44,'quart de tour : $\\frac{\\pi}{2}$ ≈ 1,571','fixe','s')
save(fig,'29-142')
