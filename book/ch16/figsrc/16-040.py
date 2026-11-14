import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
xs=[11+8.5*i for i in range(9)]
text(ax,44,56,r'$x+3=7$ : un seul essai','sujet','s')
for i,x in enumerate(xs):
    if i==4: disc(ax,x,46,3.2,'resultat',label='4',size='s')
    else: disc(ax,x,46,3.2,'fixe',fill=False,lw=0.6)
text(ax,44,38,'les autres : non testés','fixe','s')
line(ax,[(4,32),(84,32)],'fixe',lw=0.5,dash=True)
text(ax,44,26,'résoudre : tous testés','sujet','s')
for i,x in enumerate(xs):
    r='resultat' if i==4 else 'limite'
    disc(ax,x,16,3.2,r,label=str(i),size='s')
text(ax,44,7,'une seule solution','resultat','s')
save(fig,'16-040')
