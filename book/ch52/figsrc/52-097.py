import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,61,r'$p \mid ab \Rightarrow p \mid a$ ou $p \mid b$','sujet','m')
line(ax,[(44,4),(44,54)],'fixe',dash=True)
cases=[(22,'5','35','5','7','resultat','fixe','5 divise 5','resultat'),(66,'6','12','3','4','limite','limite','6 ne divise ni 3 ni 4','limite')]
for cx,p,ab,a,b,ra,rb,cap,role in cases:
    box(ax,cx-9,45,18,7,role,label=f'$p={p}$')
    box(ax,cx-9,32,18,7,'sujet',label=ab)
    for s,k,r in ((-8,a,ra),(8,b,rb)):
        arrow(ax,(cx,32),(cx+s,24),'fixe')
        box(ax,cx+s-6,16,12,8,r,label=k)
    text(ax,cx,20,r'$\times$','fixe','s')
    text(ax,cx,9,cap,role,'s')
save(fig,'52-097')
