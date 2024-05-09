print("Enter the marks:")
maths=int(input())
physics=int(input())
telugu=int(input())
english=int(input())
hindi=int(input())
social=int(input())
total = maths + physics + telugu + english + hindi + social 
avg = total / 6
if avg >= 91 and avg <= 100:
    print("your Grade is A")
elif avg >= 81 and avg <= 90:
    print("your grade is B")
elif avg >= 71 and avg <= 80:
    print("your Grade is C")
elif avg >= 61 and avg <= 70:
    print("your Grade is D")
elif avg >= 51 and avg <= 60:
    print("your Grade is E")
elif avg >= 41 and avg <= 50:
    print("your Grade is F")
elif avg >= 0 and avg <= 40:
    print("You are Fail")
else:
    print("Invalid Input")
