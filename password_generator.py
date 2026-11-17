import random
import string

all_chars = string.ascii_letters + string.digits + string.punctuation  #This creates one big pool of every allowed character: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

length = int(input("Enter how long the password should be: "))

password = ""
for i in range(length):
    password += random.choice(all_chars)
print (f"Your password is: {password}")    #random.choice(all_chars) — picks one random character from the pool. We do this length times, gluing each character onto passworda AND prints...
