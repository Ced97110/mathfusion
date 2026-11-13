import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(42)
cx=[11.5,24.5,37.5,50.5]
for c in cx: box(ax,c-5.5,4,11,26,'sujet')
for c,s in zip(cx,[r'4$^{\mathrm{e}}$',r'3$^{\mathrm{e}}$',r'2$^{\mathrm{e}}$',r'1$^{\mathrm{re}}$']):
    text(ax,c,34,s,'fixe','s')
arrow(ax,(54,38.5),(8,38.5),'fixe',lw=0.7)
for y,digs in [(23,'4329'),(11,'3429')]:
    for c,d in zip(cx,digs):
        text(ax,c,y,d,'varie' if d=='3' else 'encre','l')
text(ax,59,23,'3 en centaines : 300','resultat','s',ha='left')
text(ax,59,11,'3 en milliers : 3 000','resultat','s',ha='left')
save(fig,'01-063')
