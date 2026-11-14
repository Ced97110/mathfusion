import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
for i,(n,r,w_,h) in enumerate([('ℂ','fixe',84,62),('ℝ','sujet',72,50),('ℚ','sujet',60,38),('ℤ','sujet',48,26),('ℕ','sujet',36,14)]):
    x=2+6*i; y=2+6*i
    box(ax,x,y,w_,h,r,fill=(i==0))
    text(ax,x+3,y+h-3.3,n,r,'l',ha='left',weight='bold') if i<4 else text(ax,x+w_/2,y+h/2,n,r,'l',weight='bold')
save(fig,'42-054')
