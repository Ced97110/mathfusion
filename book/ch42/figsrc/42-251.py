import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
def row(a): return '    '.join(a)
T=[(78-16,'123','231','fixe','sujet','fixe',r'$\pi$'),
   (34,'231','123','varie','fixe','varie','les lignes échangées'),
   (6,'123','312','fixe','resultat','resultat',r'$\pi^{-1}$')]
for y,t,b,rt,rb,rbox,lab in T:
    box(ax,4,y,36,16,rbox,label=None)
    text(ax,22,y+11,row(t),rt,'m',weight='bold'); text(ax,22,y+5,row(b),rb,'m',weight='bold')
    text(ax,46,y+8,lab,rbox if rbox!='varie' else 'varie','m' if len(lab)<4 else 's',ha='left')
for y0,l in ((62,'échanger les lignes'),(34,'ranger selon le haut')):
    arrow(ax,(22,y0-0.6),(22,y0-11.4),'varie'); text(ax,46,y0-6,l,'varie','s',ha='left')
save(fig,'42-251')
