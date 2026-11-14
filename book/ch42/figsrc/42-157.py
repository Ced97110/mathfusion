import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
X0,DX=40,8
for i in range(6): text(ax,X0+i*DX,85,str(i+1),'encre','m')
def row(y,l,r,s):
    text(ax,3,y,l,r,'m',ha='left')
    for i in range(6):
        if i+1 in s: disc(ax,X0+i*DX,y,3,r)
        else: disc(ax,X0+i*DX,y,3,'fixe',fill=False,lw=0.5)
def eq(y): 
    line(ax,[(X0-3,y+0.8),(X0+5*DX+3,y+0.8)],'resultat',lw=1.0); line(ax,[(X0-3,y-0.8),(X0+5*DX+3,y-0.8)],'resultat',lw=1.0)
row(75,'A','sujet',{1,2,3}); row(65,'B','autre',{3,4})
line(ax,[(3,58),(85,58)],'fixe',dash=True)
row(49,r'$(A\cup B)^\prime$','resultat',{5,6}); eq(41.5); row(34,r'$A^\prime\cap B^\prime$','resultat',{5,6})
line(ax,[(3,26.5),(85,26.5)],'fixe',dash=True)
row(19,r'$(A\cap B)^\prime$','resultat',{1,2,4,5,6}); eq(11.5); row(5,r'$A^\prime\cup B^\prime$','resultat',{1,2,4,5,6})
save(fig,'42-157')
