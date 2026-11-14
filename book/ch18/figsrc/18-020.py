import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
cols=[(2,30),(34,26),(62,24)]
for (x,w),s in zip(cols,['deux nombres','produit : 6','somme : 5']): box(ax,x,52,w,8,'fixe',label=s,size='s')
rows=[('1 et 6','1 × 6 = 6','resultat','1 + 6 = 7','limite'),('2 et 3','2 × 3 = 6','resultat','2 + 3 = 5','resultat'),('1 et 4','1 × 4 = 4','limite','1 + 4 = 5','resultat')]
for i,(p,a,ra,b,rb) in enumerate(rows):
    y=40-12*i; both=(ra=='resultat' and rb=='resultat')
    box(ax,cols[0][0],y,cols[0][1],9,'resultat' if both else 'fixe',label=p)
    box(ax,cols[1][0],y,cols[1][1],9,ra,label=a,size='s')
    box(ax,cols[2][0],y,cols[2][1],9,rb,label=b,size='s')
text(ax,44,8,'les deux conditions ensemble','resultat','s')
save(fig,'18-020')
