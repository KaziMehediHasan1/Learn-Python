# দুইটা সংখ্যা ইনপুট নিয়ে যোগফল বের করো।
"""def add_two_numbers(num1, num2):
    print(num1 + num2) 

add_two_numbers(5, 10) """

# ব্যবহারকারীর নাম ইনপুট নিয়ে “Hello, <name>!” প্রিন্ট করো।
"""def greet_user(name):
    print("Hello", name)
greet_user("Alice")"""

# একটি সংখ্যা জোড় নাকি বিজোড়—চেক করো।
"""number = [2,5,6,9,3,4,7,8]
odd = []
even = []
for num in number:
    # print("number dekhi",num)
    if num % 2 == 0:
        even.append(num)
    elif num % 2 != 0:
        odd.append(num)
print("Even numbers are:", even)
print("Odd numbers are:", odd)"""

# তিনটি সংখ্যার মধ্যে সবচেয়ে বড় সংখ্যা বের করো।
"""bignum = [3,90,32]
num=0
for i in bignum:
    print(i,"ii")
    if i>num:
        num=i   
print("Biggest number is:", num)"""

# একটি সংখ্যা পর্যন্ত (n) 1–n পর্যন্ত সব নাম্বারের যোগফল বের করো।
"""sum_of_numbers = [2, 4, 6, 75, 45, 32, 1, 34, 68]
sum_number = 0

for num in sum_of_numbers:
    sum_number += num
    print(sum_number, "jog holo")"""
    
# একটি শব্দ ইনপুট নিয়ে তার length প্রিন্ট করো।
"""def take_word(word):
    return word

answer = take_word("Mehedi")
print(answer,"word")"""

# list থেকে সবচেয়ে বড় সংখ্যা বের করো (max without using max()).
"""all_list = [2,3,4,23,246,688,57]
big_num = 0
for num in all_list:
    # print(num, "big ni")
    if num>big_num:
        big_num = num
    print(big_num,"check")"""
    
# একটি string কে reverse করে দেখাও।
"""orginal_string = "Kazi Mehedi"
for i in orginal_string:
    reversed_string = orginal_string[::-1]
    print(reversed_string,"reversed_string")"""
    
    
# একটি list থেকে even number গুলো filter করে নতুন list বানাও।
"""list_item=[3,46,7,2,1,4,6,88,0,98,6,57,55]
even_num=[]
for i in list_item:
    if i % 2 == 0:
        ans = even_num.append(i)
        list([ans])
        
print("even num",even_num)"""

# dictionary থেকে সব keys প্রিন্ট করো।
"""dict_name ={"Name":"Kazi Mehedi", "Age":24,"Institute":"ICST"}
# print(dict_name.keys())

for i in dict_name.keys():
    print(i)"""
    
# একটি sentence এ কয়টি word আছে—count করো।
count_word = "kazi mehedi hasan"
print(count_word)
