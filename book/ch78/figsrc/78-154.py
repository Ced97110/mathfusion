import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(104)
T=[r'$l(ij)$',r'$(li)j$',r'$-(il)j$',r'$-i(lj)$',r'$i(jl)$',r'$(ij)l$']
S=[('parenthèse','fixe'),(r'signe : $li=-il$','varie'),('parenthèse','fixe'),(r'signe : $lj=-jl$','varie'),('parenthèse','fixe')]
ys=[92-i*17 for i in range(6)]
for i,t in enumerate(T):
    box(ax,8,ys[i]-2,34,10,'sujet' if i==0 else ('resultat' if i==5 else 'fixe'),label=t)
for i,(s,r) in enumerate(S):
    arrow(ax,(25,ys[i]-2),(25,ys[i+1]+8),r)
    text(ax,48,(ys[i]+ys[i+1])/2+3,s,r,'s',ha='left')
text(ax,48,ys[5]+3,r'$lk=kl$','resultat','m',ha='left')
save(fig,'78-154')
