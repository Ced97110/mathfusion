import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
text(ax,44,72,r'$(a,b)=(252,198)$ au départ','sujet','m',weight='bold')
y=50
xs=dict(a=12,eq=22,b=34,t=46,u=53,p=60,r=70)
text(ax,xs['a'],y,'252','sujet','l'); text(ax,xs['eq'],y,'=','encre','l')
text(ax,xs['b'],y,'198','autre','l'); text(ax,xs['t'],y,r'$\times$','encre','l')
text(ax,xs['u'],y,'1','encre','l'); text(ax,xs['p'],y,'+','encre','l'); text(ax,xs['r'],y,'54','varie','l')
y2=18
text(ax,14,y2,r'$(b,r)=$','autre','m',ha='left')
text(ax,36,y2,'(','fixe','l'); text(ax,46,y2,'198','autre','l'); text(ax,56,y2,',','fixe','l')
text(ax,64,y2,'54','varie','l'); text(ax,72,y2,')','fixe','l')
arrow(ax,(xs['b'],45),(46,23),'autre',lw=1.4)
arrow(ax,(xs['r'],45),(64,23),'varie',lw=1.4,curve=-0.15)
text(ax,20,35,'une division','encre','s')
save(fig,'05-093')
