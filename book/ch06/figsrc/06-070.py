import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cell(ax,x,y,w,h,role,fill=True,lw=0.6): ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=lw,zorder=2))
fig,ax=canvas(88)
x0,L=20,62
def bar(y,d,n,role,lab,lw):
    c=L/d
    for i in range(d): cell(ax,x0+i*c,y,c,6,role,fill=i<n,lw=lw)
    text(ax,2,y+3,lab,role,'m',ha='left')
bar(76,4,3,'sujet',r'$3/4$',0.6); bar(60,28,21,'varie',r'$21/28$',0.25)
bar(42,7,5,'autre',r'$5/7$',0.6); bar(26,28,20,'varie',r'$20/28$',0.25)
arrow(ax,(50,75),(50,67),'varie'); text(ax,58,71,r'$\times 7$','varie','s',ha='left')
arrow(ax,(50,41),(50,33),'varie'); text(ax,58,37,r'$\times 4$','varie','s',ha='left')
text(ax,44,12,'même bas 28 : hauts 21, 20','resultat','m')
save(fig,'06-070')
