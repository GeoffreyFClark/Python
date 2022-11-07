def method1(): #gets user input for building height, initial speed, and flight time
      h = int(input("Height of building: "))
      v = float(input("Initial Speed: "))
      t = float(input("Flight time: "))
      return(h, v, t)

height, speed, time = method1() #binds method 1 values to variabes

def method2(): #calculates ballheight based on building height, speed, time
      h = height
      v = speed
      t = time
      ballheight = -16*(t**2) + v*t + h
      print("The ball will be {:0.2f} feet above ground "
            "after {:0.2f} seconds of flight time".format(ballheight, t))

method2()