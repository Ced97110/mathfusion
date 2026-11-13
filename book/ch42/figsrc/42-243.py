import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
rows=[(r"$\beta'$",'autre','départ'),(r"$\beta'\circ 1_T$",'fixe',r'on ajoute $1_T$'),
      (r"$\beta'\circ(\alpha\circ\beta)$",'fixe',r'$1_T=\alpha\circ\beta$'),
      (r"$(\beta'\circ\alpha)\circ\beta$",'varie','on regroupe : associativité'),
      (r"$1_S\circ\beta$",'fixe',r"$\beta'\circ\alpha=1_S$"),(r"$\beta$",'sujet','arrivée')]
y=82
for i,(e,r,why) in enumerate(rows):
    box(ax,2,y-5,40,10,r,label=e,size='m')
    text(ax,46,y,why,'varie' if r=='varie' else 'fixe','s',ha='left')
    if i<len(rows)-1: arrow(ax,(22,y-5.6),(22,y-10.4),'fixe')
    y-=15
save(fig,'42-243')
