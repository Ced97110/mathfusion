import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
RL=['sujet','varie','resultat','limite']
f=numberline(ax,6,76,52,-6,6,labels=False,arrow_right=False)
bx=[14,34,54,74]
for v in range(-6,7):
    r=v%4; disc(ax,f(v),52,1.6,RL[r])
    line(ax,[(f(v),50),(bx[r],24)],'fixe',lw=0.35)
for v in (-6,0,6): text(ax,f(v),58,f'{v}'.replace('-','−'),'fixe','s')
text(ax,f(-1),58,'−1','limite','s'); text(ax,f(3),58,'3','limite','s')
text(ax,2,61,'ℤ','fixe','m',ha='left')
for i in range(4): box(ax,bx[i]-8,10,16,13,RL[i],label=f'reste {i}',size='s')
text(ax,44,3.5,'ℤ/4ℤ : quatre objets','sujet','m')
save(fig,'52-016')
