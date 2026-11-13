import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def plus(ax,x,y,role="fixe",s=1.4):
    line(ax,[(x-s,y),(x+s,y)],role,lw=1.1); line(ax,[(x,y-s),(x,y+s)],role,lw=1.1)
def times(ax,x,y,role="fixe",s=1.1):
    line(ax,[(x-s,y-s),(x+s,y+s)],role,lw=1.1); line(ax,[(x-s,y+s),(x+s,y-s)],role,lw=1.1)

fig,ax=canvas(82)
text(ax,4,76,r'$x=3$','fixe','m',ha='left')
for y0,role,op,lab,res in [(56,'sujet','+',r'$4x$ : termes identiques',r'$3+3+3+3=12$'),(22,'autre','x',r'$x^4$ : facteurs identiques',r'$3\times3\times3\times3=81$')]:
    text(ax,4,y0+14,lab,role,'m',ha='left')
    xs=[14,34,54,74]
    for x in xs: disc(ax,x,y0+3,5,role,label='3')
    for a,b in zip(xs,xs[1:]):
        (plus if op=='+' else times)(ax,(a+b)/2,y0+3,role)
    text(ax,44,y0-10,res,role,'l',weight='bold')
save(fig,'15-034')
