#1.try 2.except 3.else 4.finally
try:
   number = int(input("Type a number pls: "))
   1/number
except:
   print("You can't do this girl :c")
except ZeroDivisonError:
    print("it doesn't work this way pookie")
else:
   print("You can do this girl :D ")
finally:
   print("It's jover girl")