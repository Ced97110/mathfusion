import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax,x,y,cw,ch,rows,roles,size="m"):
    for i,r in enumerate(rows):
        for j,v in enumerate(r):
            box(ax,x+j*cw+0.25,y+(len(rows)-1-i)*ch+0.25,cw-0.5,ch-0.5,roles[i][j],label=v,size=size)

fig,ax=canvas(68)
u=2.8; x0=40
rows=[('5 = 1 + 4',1,2,58),('25 = 9 + 16',3,4,40),('125 = 25 + 100',5,10,6)]
for lab,a,b,y in rows:
    text(ax,2,y+max(a,b)*u/2,lab,'resultat' if y==6 else 'fixe','s',ha='left')
    box(ax,x0,y,a*u,a*u,'sujet',r=0.3); box(ax,x0+a*u+3,y,b*u,b*u,'varie',r=0.3)
text(ax,20,53,'$\\times$','encre','l')
text(ax,20,36,'$=$','encre','l')
save(fig,'77-078')
