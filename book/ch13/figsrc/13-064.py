import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,44,67,r'$a-b$ : part de $a$, retire $b$','sujet','s')
text(ax,44,62,r'$b-a$ : part de $b$, retire $a$','autre','s')
for y,a,b in [(38,7,4),(18,10,6)]:
    x0=10; c=5
    for k in range(a): box(ax,x0+c*k,y,c,6,'sujet' if k<a-b else 'varie')
    brace(ax,x0,x0+c*a,y+6.5,'sujet',label=rf'$a={a}$',down=False)
    brace(ax,x0+c*(a-b),x0+c*a,y-0.5,'varie',label=rf'$b={b}$ retiré')
    xt=x0+c*a+4
    text(ax,xt,y+4.5,rf'${a}-{b}$','sujet','s',ha='left')
    text(ax,xt,y+0.5,rf'${b}-{a}$','autre','s',ha='left')
text(ax,44,4,"l'ordre des lettres compte",'encre','s')
save(fig,'13-064')
