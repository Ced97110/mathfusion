import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(46)
X=[24,46]; Y=[10,24]
for x,l in zip(X,[r'$a$',r'$-b$']): text(ax,x+10,40,l,'sujet','m')
for y,l in zip([Y[1],Y[0]],[r'$a$',r'$-b$']): text(ax,16,y+6,l,'sujet','m')
cells=[(0,1,'sujet',r'$a^2$','25'),(1,1,'varie',r'$-ab$','−10'),(0,0,'varie',r'$-ab$','−10'),(1,0,'autre',r'$+b^2$','+4')]
for i,j,r,l,n in cells:
    box(ax,X[i],Y[j],20,12,r); text(ax,X[i]+10,Y[j]+7.5,l,r,'m'); text(ax,X[i]+10,Y[j]+3.3,n,r,'s')
text(ax,44,4.5,r'$25-10-10+4=9$','resultat','m')
save(fig,'15-103')
