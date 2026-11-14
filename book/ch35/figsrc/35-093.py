import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(82)
x0,x1=8,84;k=3
f=lambda x:x0+x/(4*math.pi)*(x1-x0)
xs=[i*4*math.pi/1500 for i in range(1501)]
rows=((68,'autre',lambda x:2*math.cos(x/2),'facteur lent : 2 cos(x/2)'),
      (44,'sujet',lambda x:math.sin(10.5*x),'facteur rapide : sin(10,5x)'),
      (18,'resultat',lambda x:2*math.cos(x/2)*math.sin(10.5*x),'produit : hauteur réglée par le lent'))
for yc,role,fn,lab in rows:
    line(ax,[(x0,yc),(x1,yc)],'fixe',lw=0.5)
    line(ax,[(f(x),yc+k*fn(x)) for x in xs],role,lw=0.9 if role!='autre' else 1.3)
    text(ax,46,yc+10.5,lab,role,'s')
for sg in (1,-1):
    line(ax,[(f(x),18+sg*k*2*math.cos(x/2)) for x in xs],'autre',dash=True,lw=0.7)
text(ax,4,56,'×','encre','l'); text(ax,4,31,'=','encre','l')
save(fig,'35-093')
