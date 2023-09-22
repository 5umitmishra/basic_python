from replit import clear
from art import logo
print(logo)

print("Hii there, welcome to the secret aucation program")
bidding = {}
bidding_continue = True

def highest_bidding(high_prise):
    highest_bid = 0
    winner = ""
    for bidders in high_prise:
        bid_amount = high_prise[bidders]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidders
    print(f"the winner is {winner}, with the bid of {highest_bid}")


while bidding_continue:
    name = input("what is your name: ")
    bidding_amount = int(input("whats your bidding amount: ₹ "))
    bidding[name] = bidding_amount
    bidders_in_bidding = input("is there any bidders? type 'Y' for yes and 'N' for no ")

    if bidders_in_bidding == "n":
        bidding_continue = False
        highest_bidding(bidding)

    elif bidders_in_bidding == "y":
        clear()


# if this program diden't work in your ide then 
# comment off frist 3 line and also comment off line 31 clear() in very last line
# after that your program works without any error
