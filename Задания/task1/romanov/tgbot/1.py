try:
    2/0
except ZeroDivisionError as a:
    print('ofibka delit na nool', a)
except:
    print("Ofibka")
else:
    print('ofibok net')
finally:
    print("выполнятеся в любом случае")

    #def summ(a,b):
     #   c=a+b
      #  return c