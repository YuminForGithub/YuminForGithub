# hello there!  
today, i will otter or sea otter program.
```py
isSeaOtter = None # sea otter is resetted
otterGender = '' # usally in otter, see a gender. resetted
print('this is pass is a otter or sea otter with question.') # tutorial
animalia = input('is this animalia?(y/n) ') # animalia check
if animalia.lower() == 'y':
  pass # if animalia is 'y', that returns none and end
else:
  print('not a otter or a sea otter.') # if not a otter or a sea otter, alarm it
  import os
  os._exit(1) # error end
length = int(input('length(cm)? ')) # get a length from a console
if length <= 95 and length >= 57:
  isSeaOtter = True # this returns sea otter is true
elif length >= 100 and length <= 150:
  isSeaOtter = False # this returns otter
  if length <= 150 and length >= 120:
    otterGender = 'men' # get a otter gender. this is a men.
  elif length >= 100 and length <= 140:
    otterGender = 'women' # get a otter gender. this is a women.
else:
  print('not a otter or a sea otter, or a baby otter or baby sea otter.') # not a otter or a baby otter
  import os
  os._exit(1) # error exit

if isSeaOtter:
  print('this is a sea otter.') # this is sea otter
else: #             vvvvvvvvvvvvv this is a function organic text, that means 'this is a ' + otterGender + ' otter.'
  print(f'this is a {otterGender} otter.') # this is otter
print('end') # that means end(finish)
```
*****
