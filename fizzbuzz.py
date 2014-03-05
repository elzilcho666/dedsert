for x in xrange(1, 101):
 if(x % 5 == 0 and x % 3 == 0):
  print 'fizzbuzz'
 else:
  if(x % 5 == 0):
   print 'buzz'
  else:
   if(x % 3 == 0):
    print 'fizz'
   else:
    print x