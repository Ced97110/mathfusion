import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(86)
X=[2,31.5,61]; w_=25; h=15
for x,t in zip(X,['nombre','condition lue','ligne choisie']): text(ax,x+w_/2,78,t,'fixe','s')
rows=[(52,'sujet',r'$a=4$','resultat',r'$a\geq0$ : vrai','resultat',r'$|a|=a$',False),
      (30,'sujet',r'$a=-4$','resultat',r'$a<0$ : vrai','resultat',r'$|a|=-a$',False),
      (8,'fixe',r'$a$ inconnu','limite','condition ?','limite','barres restent',True)]
for y,r1,t1,r2,t2,r3,t3,dash in rows:
    box(ax,X[0],y,w_,h,r1,label=t1,size='s'); box(ax,X[1],y,w_,h,r2,label=t2,size='s',dash=dash)
    box(ax,X[2],y,w_,h,r3,label=t3,size='s',dash=dash)
    arrow(ax,(X[0]+w_+0.5,y+h/2),(X[1]-0.5,y+h/2),'fixe')
    if not dash: arrow(ax,(X[1]+w_+0.5,y+h/2),(X[2]-0.5,y+h/2),'fixe')
save(fig,'13-051')
