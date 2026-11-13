import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
f=numberline(ax,6,70,36,-7,7,every=7,arrow_right=False)
for v,hy,ha in [(3,42,'right'),(5,49,'center'),(10,42,'left')]:
    r=(4*v-5)**0.5
    disc(ax,f(r),36,1.5,'resultat')
    dx={'right':-0.4,'center':0,'left':0.4}[ha]
    line(ax,[(f(r),37.6),(f(r),hy-2.2 if ha=='center' else hy-1.0)],'resultat',lw=0.6)
    text(ax,f(r)+dx,hy,'x = %d → %s'%(v,('%.2f'%r).replace('.',',')),'resultat','s',ha=ha)
disc(ax,f(-6),36,1.8,'limite',fill=False,lw=1.2)
text(ax,f(-6),42,'−6 impossible','limite','s')
brace(ax,f(0),f(7),28,'resultat',label='une racine donne ≥ 0')
save(fig,'22-145')
