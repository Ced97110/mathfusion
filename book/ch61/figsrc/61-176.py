import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
text(ax,44,53,r'$x^2+y^2+dx+ey+f=0$','sujet','l')
text(ax,44,46,'la forme ne change pas','fixe','s')
xs=[38,54,70]
for x,l in zip(xs,['d','e','f']):
    box(ax,x,34,14,8,'varie',label='$%s$'%l)
rows=[('rayon 2, centre (0 ; 0)',['0','0','−4'],20),('rayon 5, centre (1 ; 2)',['−2','−4','−20'],6)]
for lab,vals,y in rows:
    text(ax,3,y+4,lab,'encre','s',ha='left')
    for x,v in zip(xs,vals):
        box(ax,x,y,14,8,'fixe',label=v)
save(fig,'61-176')
