import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,61,r'$(g^{m})^{n}=g^{mn}$','encre','l')
bw,bh,x0=10,8,30
for r,y in enumerate((32,20)):
    box(ax,x0-2,y-2,2*bw+5.5,bh+4,'fixe',fill=False,dash=True)
    for c in range(2): box(ax,x0+c*(bw+1.5),y,bw,bh,'sujet',label='$g$')
    text(ax,2,y+4,f'copie {r+1}','fixe','s',ha='left')
    text(ax,57,y+4,r'$g^{m}$','sujet','m',ha='left')
text(ax,2,44,'n = 2 copies','varie','s',ha='left')
brace(ax,x0,x0+bw*2+1.5,43,'varie',label='m = 2 facteurs',down=False)
brace(ax,x0,x0+bw*2+1.5,16,'resultat',label='2 × 2 = 4 facteurs')
box(ax,22,1,44,7,'resultat',label=r'$g^{mn}=g^{4}$')
save(fig,'44-255')
