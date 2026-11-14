import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,60,r'somme $\approx n \times c$','sujet','l')
for x0,nums,n,c,res in((2,['28','31','29','32'],4,30,'4 × 30 = 120'),(48,['19','21','23'],3,20,'3 × 20 = 60')):
    k=len(nums); x1=x0+k*9.5+(k-1)*1.5; cx=(x0+x1)/2
    for i,t in enumerate(nums):
        box(ax,x0+i*11,44,9.5,8,'sujet',label=t)
        box(ax,x0+i*11,27,9.5,8,'varie')
    arrow(ax,(cx-8,43),(cx-8,36)); text(ax,cx+4,39.5,f'tous → {c}','varie','s')
    brace(ax,x0,x1,27,'varie',label=f'n = {n}')
    text(ax,cx,14,res,'resultat','m')
save(fig,'10-046')
