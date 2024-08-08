# Bad:

my_list = ( dog[ 2 ] , 5 , { "year": 1980 } , "string" )
if 5 in my_list : print( "Hello!" ) ; print( "Goodbye!" )
bread[0 : 3], roll[1: 3 :5], bun[3: 5:], donut[ 1: :5 ]

# Good:

my_list = (dog[2], 5, {"year": 1980}, "string")
if 5 in my_list: print("Hello!"); print("Goodbye!")
bread[0:3], roll[1:3:5], bun[3:5:], donut[1::5]
