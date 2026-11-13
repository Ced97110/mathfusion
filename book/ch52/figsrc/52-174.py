import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
box(ax,4,57,36,9,'sujet',label='ℤ/2ℤ',size='m'); box(ax,48,57,36,9,'autre',label='ℤ/3ℤ',size='m')
for k,(op,sym,res,a,b) in enumerate([('+','+','(0, 1)','1 + 1 = 0','2 + 2 = 1'),('×','×','(1, 1)','1 × 1 = 1','2 × 2 = 1')]):
    y=30-k*26+ (0)
    text(ax,44,y+19,f'(1, 2) {sym} (1, 2) = {res}','encre','s')
    line(ax,[(44,y+1),(44,y+14)],'fixe',dash=True); box(ax,4,y+2,36,11,'sujet',label=a,size='m'); box(ax,48,y+2,36,11,'autre',label=b,size='m')
save(fig,'52-174')
