import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
xs=[4,20,36,52,68]
text(ax,43,56,'on lit','fixe','s'); text(ax,43,5,'on écrit','fixe','s')
top=[('P','sujet'),('est','fixe'),('Q','sujet'),('de','fixe'),('B','sujet')]
bot=[('P','sujet'),('=','varie'),('Q','sujet'),('×','varie'),('B','sujet')]
for x,(s,r),(t,r2) in zip(xs,top,bot):
    lab=lambda s: f'${s}$' if len(s)==1 and s.isalpha() else s
    box(ax,x,40,14,12,r,label=lab(s)); box(ax,x,10,14,12,r2,label=lab(t),size='l' if r2=='varie' else 'm')
    arrow(ax,(x+7,39.5),(x+7,22.5),'varie' if r2=='varie' else 'fixe')
save(fig,'09-092')
