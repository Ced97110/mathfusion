import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f=numberline(ax,8,76,22,0,120,step=20,arrow_right=False,size='s')
for a in (20,35,60):
    disc(ax,f(a),22,2.4,'resultat',label='1',size='s'); text(ax,f(a),30,f'{a}°','resultat','s')
line(ax,[(f(65),22),(f(120),22)],'autre',lw=2.0,dash=True)
brace(ax,f(65),f(120),30,'autre',label='pas essayés : ?',down=False)
text(ax,44,50,'20° : 1,1325 × 0,8830 = 1,0000','encre','s')
text(ax,44,5,'trois angles donnent 1, pas tous les angles','encre','s')
save(fig,'31-009')
