import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(46)
c=3.2; gp=0.4; x0=5; y0=14
for j in range(21):
    for r in range(3):
        role='resultat' if j==0 else 'sujet'
        box(ax,x0+j*(c+gp),y0+r*c,c,c,role,lw=0.4,r=0.2)
brace(ax,x0,x0+20*(c+gp)+c,y0,'sujet',r'$2^{6}-1=63$ cases',down=True,depth=2.2)
brace(ax,x0,x0+c,y0+3*c+0.5,'resultat',None,down=False,depth=1.8)
text(ax,x0,y0+3*c+7,r'$\Phi_{6}(2)=3$ cases','resultat','m',ha='left')
text(ax,x0+34,y0+3*c+7,r'21 groupes de 3 : $3\times21=63$','sujet','m',ha='left')
text(ax,44,y0+3*c+17,r'$\Phi_{6}$ divise $\lambda^{6}-1$','fixe','m')
save(fig,'78-119')
