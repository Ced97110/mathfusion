import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
rows=[('fixe',[r'$e_1$',r'$e_2$',r'$e_3$'],1),('sujet',[r'$e_1e_2$',r'$e_1e_3$',r'$e_2e_3$'],2),('autre',[r'$e_1e_2e_3$'],3)]
ys=[54,32,10]
for (role,items,r),y in zip(rows,ys):
    text(ax,3,y+9,rf'$\Lambda^{r}(V)$',role,'l',ha='left')
    text(ax,3,y+3,f'r = {r}' if r!=1 else 'r = 1','fixe','s',ha='left')
    n=len(items); x0=44 if n==3 else 62
    for i,l in enumerate(items):
        box(ax,(32+i*18) if n==3 else 48,y,16 if n==3 else 20,12,role,label=l,size='m' if n==3 else 's')
save(fig,'76-087')
