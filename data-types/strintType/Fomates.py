age = 30
name = "Kazi Mehedi Hasan"
# answer = name + age # wrong answer, it's wrong way
#answerTwo = "Kazi Mehedi Hasan" + age # TypeError: can only concatenate str (not "int") to str
correctAns = f"{name}, I'm {age}th"
print(correctAns)

# calculate one line using formater 
thisAns= f"I Have {20} taka but next 2 years is double months ! {20 *24 }"
print(thisAns)