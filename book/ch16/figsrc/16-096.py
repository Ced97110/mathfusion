import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
def row(y,n,role,lab):
    per=12//n
    for g in range(n):
        w=(76-(n-1)*3)/n; x0=6+g*(w+3); box(ax,x0,y,w,13,role)
        for k in range(per): disc(ax,x0+w/2+(k-(per-1)/2)*(min(5,(w-4)/per)),y+6.5,1.8,'sujet')
    text(ax,44,y+17,lab,role,'m')
text(ax,44,70,'12','sujet','l')
row(42,2,'sujet',r'la moitié : $x\div2=6$'); row(14,3,'autre',r'le tiers : $x\div3=4$')
save(fig,'16-096')
