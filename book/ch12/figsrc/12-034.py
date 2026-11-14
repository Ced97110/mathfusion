import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(42)
text(ax,44,37,'les deux nombres diffèrent','sujet','m')
for i,(a,b,ok) in enumerate([(8,5,1),(5,8,1),(8,8,0)]):
    r='resultat' if ok else 'limite'; x=3+i*28.5
    box(ax,x,10,25,16,r,label=rf'${a}\neq{b}$',size='l')
    text(ax,x+12.5,5,'vrai' if ok else 'faux',r,'m')
save(fig,'12-034')
