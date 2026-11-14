import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
box(ax,2,14,84,36,'fixe',fill=False,dash=True)
text(ax,44,45,r'$R$ : les entiers','fixe','m')
f=numberline(ax,8,74,28,-8,12,labels=False,arrow_right=False)
for v in range(-8,13):
    if v%4==0: disc(ax,f(v),28,1.7,'sujet'); text(ax,f(v),22,f'{v}'.replace('-','−'),'sujet','s')
    else: disc(ax,f(v),28,0.7,'fixe')
box(ax,6,2,76,8,'sujet',label=r'$I$ = les multiples de 4',size='m')
arrow(ax,(44,10.8),(44,16),'sujet')
save(fig,'52-008')
