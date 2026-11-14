import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,'le corps choisi','sujet','s')
box(ax,32,40,24,14,'sujet',label=r'$F$',size='xl')
for i,l in enumerate(['ℚ','ℝ','ℂ','ℤ/5']):
    x=2+i*21.5
    box(ax,x,19,19,10,'autre',label=l,size='l')
    arrow(ax,(44,39.5),(x+9.5,30),'varie')
box(ax,6,3,76,8,'fixe',label=r'on y calcule : $+\;-\;\times\;\div$',size='s')
save(fig,'71-128')
