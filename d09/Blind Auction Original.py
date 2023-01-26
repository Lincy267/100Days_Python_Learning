from replit import clear
from d09 import art

#HINT: You can call clear() to clear the output in the console.

print(art.logo)

no_other_user = True
user_name = []
user_bid = []
user_dict = {}
max_bid = 0


while no_other_user == True:

    user_name.append(input("What is your name?\n"))
    user_bid.append(input("What is your bid?\n$"))

    user_dict["bidder"] = user_name
    user_dict["bid"] = user_bid

    if_no_other_user = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if if_no_other_user == "yes":
        no_other_user = True
        clear()
    elif if_no_other_user == "no":
        no_other_user = False
        clear()
    else:
        print(f"ERROR")
        no_other_user = True
        clear()

for bid in user_dict["bid"]:
    if int(bid) > max_bid:
        max_bid = int(bid)
        max_bid_str = str(max_bid)

max_bidder_index = user_bid.index(max_bid_str)
max_bidder = user_name[max_bidder_index]
print(f"The winner is {max_bidder} with the bid of ${max_bid}")
