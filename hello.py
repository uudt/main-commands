import random

print("Hello, GitHub users!")
print("I wish all of you a good day!")
print("Let's figure out how lucky you are today: ")
print("""
     _____     _____
  ,gdPPPPRb, ,dPPPPRbg,
 dP'      `YdP'      `Yb
 8)        `8'        (8
 Yb,        "        ,dP
  "8bggg         gggd8"
  ,gdP""         ""Ybg,
 dP'        a        `Yb
 8)        ,8,        (8
 Yb,      ,d8b       ,dP
  "8baaaadP"8"Ybaaaad8"
    `"`"'   8   `"'"'
            8
            8
            8    
            8    
            8
"""
luckiness = random.randint(1, 11)
print(f"Today you're lucky for {luckiness} out of 10")
