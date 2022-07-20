principal = 5000
rate = 0.05
time = 5
goal = 7000

#   amount = principal * e ^ (rate * time)
#
#Those three variables are given above again, as well as a
#fourth: goal. We want to see if the investment given by
#these values will exceed the goal. If it will, we want to
#print this message:
#
#  "You'll exceed your goal by [extra money]"
#
#If it will not, we want to print this message:
#
#  "You'll fall short of your goal by [needed money]"
#
#If the investor will meet their goal, [extra money] should
#be the final amount minus the goal. If the investor will
#not meet their goal, [needed money] will be the goal minus
#the final amount.

import math

amount = principal * math.e ** (rate * time)
extraMoney = (amount - goal)
neededMoney = (goal - amount)

if amount >= goal:
    print("You'll exceed your goal by", round(extraMoney, 2))
elif goal >= amount:
    print("You'll fall short of your goal by", round(neededMoney,2))