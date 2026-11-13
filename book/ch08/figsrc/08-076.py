import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,44,54,r'$100 \div 27 = 3{,}703\ 703\ldots$','encre','s')
rs=['reste 19','reste 1','reste 10','reste 19']; ds=['3','7','0','3']
bw=17; g=4.5; x0=3; y=28
for i,(r,d) in enumerate(zip(rs,ds)):
    x=x0+i*(bw+g); role='sujet' if r=='reste 19' else 'fixe'
    box(ax,x,y,bw,9,role,label=r,size='s')
    if i<3: arrow(ax,(x+bw+0.3,y+4.5),(x+bw+g-0.3,y+4.5),'fixe')
    text(ax,x+bw/2,y-5,d,'resultat' if i else 'encre','l')
xa=x0+bw/2; xb=x0+3*(bw+g)+bw/2
line(ax,[(xb,y+9.3),(xb,y+15),(xa+1.5,y+15)],'varie',lw=1.1)
arrow(ax,(xa,y+15),(xa,y+9.3),'varie',lw=1.1)
text(ax,(xa+xb)/2,y+18.5,'19 revient','varie','s')
brace(ax,x0+(bw+g)-1,xb+bw/2,y-9,'resultat',label='période 703',down=True)
save(fig,'08-076')
