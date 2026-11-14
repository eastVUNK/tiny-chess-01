import json,os,urllib.request as u
E=os.environ["MAKEFUN_ENV_URL"]
def P(p,b={}):
 try:
  with u.urlopen(E+p,json.dumps(b).encode())as r:return json.load(r)
 except TO:pass
KN=(33,18,-14,-31,-33,-18,14,31)
QU=(15,17,-15,-17,1,-1,16,-16)
MV=(100,320,330,500,900,0)
L="abcdefgh"
PS="AAAA````KKU_FFKZAAAUF<7AFKK-AAAA"
V=[ord(PS[(7-(s>>4))*4+min(s&7,7-(s&7))])-65 for s in range(128)]
b=[0]*128;w=1;c=0;e=-1;KS=[4,116];n=0;CB={7:1,0:2,119:4,112:8}
D={};K=[0]*16
MT=9999
TO=Exception
def A(s,v):
 for ds,pt in(((-15,-17)if v else(15,17),1),(KN,2),(QU,6)):
  for d in ds:
   t=s+d
   if not t&0x88 and b[t]==(pt if v else -pt):return 1
 for i,d in enumerate(QU):
  t=s
  while 1:
   t+=d
   if t&0x88:break
   q=b[t]
   if q:
    if(q>0)==v and abs(q)in(5,3+(i>3)):return 1
    break
 return 0
def G(x=0):
 ms=[]
 for s in range(128):
  if not(p:=b[s])or(p>0)^w:continue
  t=abs(p)
  if t==1:
   d=32*w-16;pr=7*w;sr=6-5*w
   for o in(s+d,s+d-1,s+d+1):
    if o&0x88:continue
    q=b[o]
    if o==s+d:
     if q or x and(o>>4)!=pr:continue
    elif(q==0 or(q>0)==w)and o!=e:continue
    ms.append((s,o,0))
    if(o>>4)==pr:ms[-1:]=[(s,o,y)for y in(5,4,3,2)]
    elif o==s+d and(s>>4)==sr and not b[o+d]:ms.append((s,o+d,0))
  else:
   for d in(KN,QU[:4],QU[4:],QU)[min(t-2,3)]:
    o=s
    while 1:
     o+=d
     if o&0x88:break
     q=b[o]
     if q and(q>0)^w or not(q or x):ms.append((s,o,0))
     if q or t%4==2:break
 if not x:
  for bt in((1,2)if w else(4,8)):
   kf=116-112*w;dd=1 if bt&5 else-1
   if c&bt and all(not b[kf+i*dd]for i in(1,2,3)if dd<0 or i<3)and all(not A(z,not w)for z in(kf,kf+dd,kf+2*dd)):ms.append((kf,kf+2*dd,0))
 return ms
def M(m):
 global w,c,e
 f,t,pr=m
 cap=b[t];pc=b[f];co=c;eo=e;ec=-1
 b[t]=pc;b[f]=0
 if pr:b[t]=pr*(w or-1)
 if pc*pc==1 and t==eo and not cap:
  ec=t+16-32*w
  cap=b[ec];b[ec]=0
 if pc*pc==36:
  KS[not w]=t
  if abs(t-f)==2:
   rs,rd=f+3-7*(t<f),f+(t>f)*2-1
   b[rd]=b[rs];b[rs]=0
  c&=~(3<<2-2*w)
 for z in(f,t):c&=~CB.get(z,0)
 e=(f+t)//2 if pc*pc==1 and abs(t-f)//32 else-1
 w^=1
 return cap,co,eo,ec
def N(m,u):
 global w,c,e
 f,t,pr=m
 cap,co,eo,ec=u
 w^=1
 pc=b[t]
 b[f]=(w or-1)if pr else pc
 if ec>=0:
  b[ec]=cap;b[t]=0
 else:b[t]=cap
 if pc*pc==36:
  KS[not w]=f
  if abs(t-f)==2:
   rs,rd=f+3-7*(t<f),f+(t>f)*2-1
   b[rs]=b[rd];b[rd]=0
 c=co;e=eo
def O(ms,d,t):
 def k(m):
  f,g,p=m;e=f<<7|g;q=b[g]
  return 9999*(m==t)or(1000+MV[abs(q)-1]if q or p else 900*(e==K[d]))
 ms.sort(key=k,reverse=True)
def F():
 s=0;B=0;C=0
 for q in range(128):
  if p:=b[q]:s+=MV[p-1]+V[q] if p>0 else-MV[-p-1]-V[q^112];B+=p==3;C+=p==-3
 s+=25*((B==2)-(C==2))
 return s if w else-s
def S(d,a,be):
 global n
 n+=1
 if n>=6e4:raise TO
 a0=a;k=(tuple(b),w,c,e);r=D.get(k)
 T=r[2]if r else None
 if r and r[0]>=d and(not r[3]or r[1]>=be):return r[1]
 ch=A(KS[not w],not w)
 q0=d<=0 and not ch
 if q0:
  best=F();a=max(a,best)
  if a>=be:return a
 else:best=-MT-1
 ms=G(q0)
 O(ms,d,T)
 bm=0
 for m in ms:
  u=M(m)
  if A(KS[w],w):
   N(m,u);continue
  s=-S(d-1,-be,-a)
  N(m,u)
  if s>best:best=s;bm=m
  a=max(a,s)
  if a>=be:
   if not b[m[1]]and not m[2]:K[d]=m[0]<<7|m[1]
   break
 if best<-MT:return ch*-MT
 if best>a0:D[k]=(d,best,bm,best>=be)
 return best
def Y(mv):
 global b,w,c,e,KS
 P=[4,2,3,5,6,3,2,4]
 b=P+[0]*8+[1]*8+[0]*72+[-1]*8+[0]*8+[-x for x in P]+[0]*8
 w=1;c=15;e=-1;KS=[4,116]
 for u in mv:M((ord(u[0])-97+(ord(u[1])-49)*16,ord(u[2])-97+(ord(u[3])-49)*16,"nbrq".index(u[4])+2 if u[4:]else 0))
def B():
 global n
 lg=[]
 for m in G():
  u=M(m)
  if not A(KS[w],w):lg.append(m)
  N(m,u)
 if not lg:return None
 D.clear()
 bm=lg[0]
 n=0
 for d in range(12):
  O(lg,d,None);lg.remove(bm);lg.insert(0,bm)
  try:
   a=best=-MT;cur=bm
   for m in lg:
    u=M(m)
    s=-S(d,-MT,-a)
    N(m,u)
    if s>best:best=s;cur=m
    a=max(a,s)
   bm=cur
  except TO:break
 f,t,pr=bm
 return L[f&7]+str(f//16+1)+L[t&7]+str(t//16+1)+("nbrq"[pr-2]if pr else"")
while 1:
 g=P("/game")or{};s=g.get("status")
 if s=="done":break
 if s=="your_move":
  Y(g["moves"]);m=B();gg={"game":g["game"]}
  g=P("/resign",gg)if m is None else P("/move",gg|{"move":m})
