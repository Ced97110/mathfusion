import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
cw,ch=22,12; x0,y0=22,46
ent=[[('$a$','sujet'),('$b$','varie')],[(r'$-\bar{b}$','varie'),(r'$\bar{a}$','sujet')]]
for r in range(2):
    for c in range(2):
        l,ro=ent[r][c]; box(ax,x0+c*cw,y0+(1-r)*ch,cw,ch,ro,label=l,size='l',r=0.3)
for x,d in ((x0-1.5,1),(x0+2*cw+1.5,-1)):
    line(ax,[(x+d*1.5,y0-0.5),(x,y0-0.5),(x,y0+2*ch+0.5),(x+d*1.5,y0+2*ch+0.5)],'encre')
text(ax,44,40,'bleu : a et son conjugué','sujet','s')
text(ax,44,35,'orange : b et moins son conjugué','varie','s')
box(ax,2,2,84,26,'fixe')
text(ax,6,23,r'$M_2(\mathbb{C})$','fixe','m',ha='left')
box(ax,36,5,46,14,'sujet',label=r'$\mathbb{H}$ : de la forme ci-dessus',size='s')
save(fig,'51-182')
