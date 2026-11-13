import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
text(ax,75,68,r'$B$','sujet','l')
rows=[(48,'15','est 30 % de','50',False),(28,'50','est 200 % de','25',False),(8,'15','est 30 % de','?',True)]
for y,a,m,b,d in rows:
    box(ax,3,y,18,12,'fixe',label=a); text(ax,44,y+6,m,'encre','m'); box(ax,66,y,18,12,'sujet',label=b,dash=d)
save(fig,'09-091')
