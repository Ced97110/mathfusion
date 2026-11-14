import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,58,r'$|HK| = 16\times16\,/\,|H\cap K|$','encre','m')
x0=26; s=0.2
for (k,v),y in zip([(8,32),(4,64),(2,128),(1,256)],[40,30,20,10]):
    role='resultat' if v<=48 else 'limite'
    box(ax,x0,y-3,v*s,6,role,r=0.4,lw=0.6)
    text(ax,2,y,rf'$|H\cap K|={k}$','encre','s',ha='left')
    text(ax,86,y,str(v),role,'m',ha='right')
xg=x0+48*s
line(ax,[(xg,5),(xg,47)],'sujet',dash=True)
text(ax,xg,50,r'$G$ : 48','sujet','s')
save(fig,'50-233')
