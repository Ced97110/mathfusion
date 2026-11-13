import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
def sec(n,ytop,cp,cm,ok):
    text(ax,2,ytop+10,f'$n={n}$','encre','l',ha='left')
    for k,(c,nm,role,lab) in enumerate(((cp,'permutations','sujet',f'${n}!={cp}$'),(cm,'transformations','autre',f'${n}^{{{n}}}={cm}$'))):
        y=ytop-k*10
        text(ax,2,y+3,nm,role,'s',ha='left')
        for j in range(c): box(ax,30+j*7.5,y,6,6,role)
        text(ax,30+c*7.5+1,y+3,lab,role,'s',ha='left')
    text(ax,44,ytop-18,f'{cp} = {cm} : coïncident' if ok else f'{cp} ≠ {cm} : diffèrent','resultat' if ok else 'limite','m',weight='bold')
sec(1,58,1,1,True); line(ax,[(2,35),(86,35)],'fixe',dash=True); sec(2,22,2,4,False)
save(fig,'44-264')
