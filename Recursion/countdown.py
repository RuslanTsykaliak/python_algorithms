def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        print("Executed after: each countdown")
        countdown(x-1)
        print("Executed after: all countdowns")


countdown(4)



# 1. What will be the exact output of countdown(4)?

# 4 ...
# Executed after: each countdown
# 3 ...
# Executed after: each countdown
# 2 ...
# Executed after: each countdown
# 1 ...
# Executed after: each countdown
# Done!
# Executed after: all countdowns
# Executed after: all countdowns
# Executed after: all countdowns
# Executed after: all countdowns
# 2. Explain the order in which the "Executed after: each countdown" and "Executed after: all countdowns" lines are printed.

# "Executed after: each countdown": This line is printed after each recursive call to countdown(x-1). Therefore, it's printed in the order of the countdown (4, 3, 2, 1).

# "Executed after: all countdowns": This line is printed after the recursive call countdown(x-1) returns. This means it's printed in the reverse order of the countdown (after Done!, then after countdown(1) returns, then after countdown(2) returns, and so on).

# 3. How many times will the countdown function be called in total?

# The countdown function will be called 5 times: countdown(4), countdown(3), countdown(2), countdown(1), and countdown(0).
# 4. What is the role of the if x == 0: condition?

# The if x == 0: condition acts as the base case of the recursion.
# It stops the recursive calls when x reaches 0.
# Without this base case, the recursion would continue indefinitely, leading to a stack overflow error.
# It also prints the "Done!" message when the countdown completes.
# 5. Explain what happens on the call stack as this function executes.

# Call Stack: The call stack is a data structure that keeps track of active function calls.

# Execution:

# countdown(4) is called.
# 4 ... and "Executed after: each countdown" are printed.
# countdown(3) is called and added to the call stack.
# Steps 2 and 3 repeat for countdown(2) and countdown(1).
# countdown(0) is called.
# "Done!" is printed.
# countdown(0) returns.
# "Executed after: all countdowns" is printed (for countdown(1)).
# countdown(1) returns.
# Steps 8 and 9 repeat for countdown(2), countdown(3), and countdown(4).
# Order: The "Executed after" lines are printed as the stack grows, and the "Executed after" lines are printed as the stack shrinks.






