import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cell(ax,x,y,w,h,role,fill=True,lw=0.6): ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=lw,zorder=2))
fig,ax=canvas(104)
x0=8; c=2.4
for i in range(30): cell(ax,x0+i*c,86,c,8,'sujet',lw=0.2)
for k in range(6):
    cell(ax,x0+k*12,86,12,8,'sujet',fill=False,lw=1.0)
    text(ax,x0+k*12+6,90,f'{k+1}','sujet','s')
text(ax,44,100,r'planche : $15/4$ m $= 30/8$ m','sujet','m')
brace(ax,8,20,86,'varie',label=r'$5/8$ m')
steps=[('1. ',r'$15/4 \div 5/8$','sujet'),('2. ',r'$15/4 \times 8/5$','varie'),('3. ',r'$3\times 2 \,/\, (1\times 1)$','varie'),('4. ',r'$= 6$ morceaux','resultat'),('5. ',r'$6\times 5/8 = 15/4$','resultat')]
for k,(a,b,r) in enumerate(steps):
    text(ax,10,64-k*10,a+b,r,'m',ha='left')
save(fig,'06-073')
