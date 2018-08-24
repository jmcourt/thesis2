delim='&'

a=open(raw_input('infile: '))

cols=int(raw_input('cols: '))
rows=int(raw_input('rows: '))

dump=[]
for line in a:
   dump.append(line[:-1])
a.close()
d=len(dump)

num=int(d/(cols*rows))+1

got=False
s=0

for n in range(num):
   print ''
   for i in range(rows):
      st=''
      for j in range(cols):
         k=rows*j+i+n*rows*cols
         if k>=d:
            st+='&'*s
            break
         sel=dump[k].split(delim)
         if not got:
            got=True
            s=len(sel)
         for l in range(len(sel)):
            st+=sel[l]+'&'
      print st[:-1]+'\\\\'
   print ''
   print '==================='
