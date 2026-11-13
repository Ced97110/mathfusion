import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
X0,DX=40,8
for i in range(6): text(ax,X0+i*DX,64,str(i+1),'encre','m')
rows=[(54,r'$A^\prime$','sujet',{4,5,6}),(44,r'$B^\prime$','varie',{1,2,5,6}),(26,r'$A^\prime\cup B^\prime$','resultat',{1,2,4,5,6}),(10,r'$(A\cap B)^\prime$','resultat',{1,2,4,5,6})]
for y,l,r,s in rows:
    text(ax,3,y,l,r,'m',ha='left')
    for i in range(6):
        if i+1 in s: disc(ax,X0+i*DX,y,3,r)
        else: disc(ax,X0+i*DX,y,3,'fixe',fill=False,lw=0.5)
line(ax,[(3,35),(84,35)],'fixe',dash=True)
text(ax,44,18,'=','resultat','xl')
save(fig,'42-154')
