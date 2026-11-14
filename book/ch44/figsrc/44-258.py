import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,r'$mg+ng=(m+n)g$','encre','l')
w,gp=8.5,1.2; xs=[]; x=(88-(7*w+5*gp+3.0))/2
for i in range(7):
    xs.append(x); x+=w+(3.0 if i==2 else gp)
for i,x in enumerate(xs): box(ax,x,30,w,9,'sujet' if i<3 else 'autre',label='2')
brace(ax,xs[0],xs[2]+w,40,'sujet',label=r'$3\cdot2\equiv1$',down=False)
brace(ax,xs[3],xs[6]+w,40,'autre',label=r'$4\cdot2\equiv3$',down=False)
brace(ax,xs[0],xs[6]+w,29,'resultat',label=r'$7\cdot2=14\equiv4$')
text(ax,44,10,r'dans $\mathbb{Z}_5$ : $1+3=4$, même reste','resultat','m')
save(fig,'44-258')
