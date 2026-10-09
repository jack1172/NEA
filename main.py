#suvat calculator
import math

def suvat():
    print("s = distance travelled u = initial velocity v = final velocity a = acceleration t = time passed")
    x = input("do you want to workout s,u,v,a or t?")

    if x == "s":
        missing = input("what input are you missing?:")
        if missing == "u":
            v = float(input("please input v:"))
            a = float(input("please input a:"))
            t = float(input("please input t:"))
            s = float((v * t) - 0.5 * (a * (t * t)))
            print("s =")
            print(float(s))
        elif missing == "v":
            u = float(input("please input u:"))
            a = float(input("please input a:"))
            t = float(input("please input t:"))
            s = float((u * t) + 0.5 * (a * (t * t)))
            print("s =")
            print(float(s))
        elif missing == "a":
            u = float(input("please input u:"))
            v = float(input("please input v:"))
            t = float(input("please input t:"))
            s = float((u + v) * 0.5 * t)
            print("s =")
            print(float(s))
        elif missing == "t":
            u = float(input("please input u:"))
            v = float(input("please input v:"))
            a = float(input("please input a:"))
            s = float((v * v) - (u * u) / (2 * a))
            print("s =")
            print(float(s))
    elif x == "u":
        missing = input("what input are you missing?:")
        if missing == "s":
            v = float(input("please input v:"))
            a = float(input("please input a:"))
            t = float(input("please input t:"))
            u = float((v * t) - 0.5 * (a * (t * t)))
            print("s =")
            print(float(u))
        elif missing == "v":
            s = float(input("please input s:"))
            a = float(input("please input a:"))
            t = float(input("please input t:"))
            u = float((s - 0.5 * a * t * t) / t)
            print("u =")
            print(float(u))
        elif missing == "a":
            s = float(input("please input s:"))
            v = float(input("please input v:"))
            t = float(input("please input t:"))
            u = float((2))
            print("u =")
            print(float(s))
        elif missing == "t":
            u = float(input("please input u:"))
            v = float(input("please input v:"))
            a = float(input("please input a:"))
            s = float((v * v) - (u * u) / (2 * a))
            print("s =")
            print(float(s))
    elif x == "v":
        missing = input("what input are you missing?:")
        if missing == "s":
            u = float(input("please input v:"))
            a = float(input("please input a:"))
            t = float(input("please input t:"))
            v = float((u * t) + 0.5 * (a * (t * t)))
            print("v =")
            print(float(v))
        elif missing == "u":
            s = float(input("please input s:"))
            a = float(input("please input a:"))
            t = float(input("please input t:"))
            v = float((s / t) + 0.5 * a * t)
            print("v =")
            print(float(v))
        elif missing == "a":
            s = float(input("please input s:"))
            u = float(input("please input a:"))
            t = float(input("please input t:"))
            v = float((2 * s / t) - u)
            print("v =")
            print(float(v))
        elif missing == "t":
            s = float(input("please input s:"))
            u = float(input("please input u:"))
            a = float(input("please input a:"))
            v = math.sqrt(((u * u) + 2 * a * s))
            print("v =")
            print(float(v))
    elif x == "a":
        missing = input("what input are you missing?:")
        if missing == "s":
            v = float(input("please input v:"))
            u = float(input("please input u:"))
            t = float(input("please input t:"))
            a = float((v - u) / t)
            print("a =")
            print(float(a))
        elif missing == "u":
            v = float(input("please input v:"))
            s = float(input("please input s:"))
            t = float(input("please input t:"))
            a = float(2 * ((v * t) - s) / (t * t))
            print("a =")
            print(float(a))
        elif missing == "v":
            u = float(input("please input u:"))
            s = float(input("please input s:"))
            t = float(input("please input t:"))
            a = float(2 * ((u * t) + s) / (t * t))
            print("a =")
            print(float(a))
        elif missing == "t":
            u = float(input("please input u:"))
            s = float(input("please input s:"))
            v = float(input("please input v:"))
            a = float(((v * v) - (u * u)) / (2 * s))
            print("a =")
            print(float(a))
    elif x == "t":
        missing = input("what input are you missing?:")
        if missing == "s":
            u = float(input("please input u:"))
            a = float(input("please input a:"))
            v = float(input("please input v:"))
            t = float(((v - u)) / a)
            print("t =")
            print(float(t))
        elif missing == "u":
            s = float(input("please input s:"))
            a = float(input("please input a:"))
            v = float(input("please input v:"))
            t1 = (v + math.sqrt((v * v) - (2 * a * s))) / a
            t2 = (v - math.sqrt((v * v) - (2 * a * s))) / a
            if t1 < 0:
                print("t =")
                print(float(t2))
            else:
                print("t =")
                print(float(t1))
        elif missing == "a":
            s = float(input("please input s: "))
            u = float(input("please input u: "))
            v = float(input("please input v: "))
            t = (2 * s) / (u + v)
            print("t =")
            print(t)
        elif missing == "v":
            u = float(input("please input u: "))
            a = float(input("please input a: "))
            s = float(input("please input s: "))
            t1 = (-u + math.sqrt((u * u) + (2 * a * s))) / a
            t2 = (-u - math.sqrt((u * u) + (2 * a * s))) / a
            if t1 >= 0 and t2 >= 0:
                print("t =", min(t1, t2))
            elif t1 >= 0:
                print("t =", t1)
            else:
                print("t =", t2)



            #conservation of momentum:
            # m1*u1 + m2*u2 = m1*v1 + m2*v2
def momentum_calculator():
    mass1 = float(input("please enter mass of object 1:"))
    mass2 = float(input("please enter mass of object 2:"))

    initial_velocity1 = float(input("Please enter velocity of object 1:"))
    initial_velocity2 = float(input("Please enter velocity of object 2:"))
    print("-" * 40)  # separator line

    final_velocity1 = (((mass1 - mass2) * initial_velocity1) + (2 * mass2 * initial_velocity2)) / (
            mass1 + mass2)

    final_velocity2 = ((2 * mass1 * initial_velocity1) + ((mass2 - mass1) * initial_velocity2)) / (
            mass1 + mass2)

    # final momentum = final velocity x mass
    # if statements to make sure negative values are not outputted
    if final_velocity1 > 0:
        print("Final momentum of object 1:", final_velocity1 * mass1)
        print("Final velocity of object 1:", final_velocity1)
        print("mass of object 1", mass1)
        print("-" * 40)  # separator line


    else:
        print("Final momentum of object 1:", final_velocity1 * mass1)
        print("Final velocity of object 1:", final_velocity1)
        print("mass of object 1", mass1)
        print("going in the opposite object as started")
        print("-" * 40)  # separator line

    if final_velocity2 > 0:
        print("Final momentum of object 2:", final_velocity2 * mass2)
        print("Final velocity of object 2:", final_velocity2)
        print("mass of object 2", mass2)
        print("-" * 40)  # separator line

    else:
        print("Final momentum of object 2:", final_velocity2 * mass2)
        print("Final velocity of object 2:", final_velocity2)
        print("mass of object 2", mass2)
        print("going in the opposite object as started")
        print("-" * 40)  # separator line


choice = input("Choose calculator (suvat/momentum): ")

if choice == "momentum":
    momentum_calculator()

elif choice == "suvat":
    suvat()

else:
    print("Invalid choice")