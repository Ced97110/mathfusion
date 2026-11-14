import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,62,r'$|G|=8=2^3$','encre','l')
labs=[r'$2^0=1$',r'$2^1=2$',r'$2^2=4$',r'$2^3=8$ : $G$']
for k,(lab,y) in enumerate(zip(labs,[50,40,30,20])):
    n=2**k; role='resultat' if k==3 else 'sujet'
    for i in range(8):
        box(ax,4+6*i,y,5.6,6,role if i<n else 'fixe',r=0.3,lw=0.6)
    text(ax,56,y+3,lab,role,'s',ha='left')
box(ax,2.4,19.2,51.2,7.6,'resultat',fill=False,lw=1.4)
text(ax,44,9,r'$n_2=1$ : le seul 2-Sylow est $G$','resultat','s')
save(fig,'50-239')
