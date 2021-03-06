# Shadman Rakib
# SoftDev
# HW - Amalgamate Random Student Name Printer
# 2021-09-27

# SUMMARY OF TRIO DISCUSSION
# We only used a list of the people we knew from each of the classes. We stored the names in Python lists. The printRandomName takes an array as an input then gets a random index using randrange and then prints the name at that index. We debated whether or not to use randint or randrange, and ultimately settle for randrange because it's exclusive which would make our code cleaner and the name is also more readable.
# DISCOVERIES
# The random.randrange function is cleaner and easier to read than using random.random. The random library has a randint function that is inclusive. This is not ideal for a lot of cases in python. In our case, we used randrange because the stop parameter is exclusive. I also learned that it is hard to find out the names of all the students in each class. One solution I came up with but did not implement because of potential complexity to use a scrapper like beautiful soup to get the links to the repos, and then use that to scrape everyones github to get their display names.
# QUESTIONS
# Does python support typing? I read a while back that the creator wants to implement something similar to types in typescript. Is camelcase the prefered way of naming variables? Is it possible to comment in the middle of a line of code?
# COMMENTS
# Python doesn't seem to have block comments like other languages, but at least editors make it easy to comment and uncomment lines. 

from random import randrange

# List people for periods 1 and 2
pd1 = ["Emma Buller", "Julia Nelson", "Owen Yaggy", "Haotian Gao", "Ishraq Mahid", "Raymond Yeung", "Kevin Cao", "Ivan Lam", "Michelle Lo"]
pd2 = ["Jesse Xie", "Rachel Xiao", "Yuqing Wu", "Liesel Wong", "Josephine Lee", "Patrick Ging", "Yaying Liang", "Shadman Rakib", "Cameron Nelson", "Eric Guo", "Daniel Sooknanen", "Andy Lin"]

KREWES = {
    1: pd1,
    2: pd2
}

def printRandomName(arr):

    # get random name from array
    randomIndex = randrange(0, len(arr))
    randomName = arr[randomIndex]

    print(randomName)

def main():
    for i in KREWES.keys():
        print("KREW" + " " + str(i), end=": ")
        printRandomName(KREWES[1])

if __name__ == "__main__":
    main()
