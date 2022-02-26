"""
Jonathan Roberts
9/25/2021
M5 A3 Capital Gain Problem

Write a program that takes as input a sequence of transactions of the form "buy x share(s) at y each" or "sell x share(s) at y each"
assuming that the transactions occur on consecutive days and the values x and y are integers. Given this input sequence the output should be the total 
capital gain (or loss) for the entire sequence, using the FIFO protocol to identify shares. 
"""

#This creates the queue. The variable buyorsell is set to "buy" so that the while loop will run based on the condition that I set.
queue = []
buyOrSell = "buy"

#This function calculates the price of the stock that was bought and stores it into the queue and displays the values currently in the queue. 
def buyShares():
    x= input("How many shares are you buying?: ")
    y= input("How much does each share cost?: ")
    buyTotal = (int(x)*int(y))
    queue.append(buyTotal)
    print(queue)
    

#This function calculates how much the stocks being sold are worth and adds a negative number to the queue so that the capital gain or loss can be calculated in another function 
def sellShares():
    x= input("How many shares are you selling?: ")
    y= input("How much are the shares selling for?: ")
    sellTotal= -abs((int(x)*int(y)))
    queue.append(sellTotal)
    print(queue)

#This function takes all the numbers in the queue and adds them together to calculate the capital gain or loss.
def capitalGainsLoss():
   gainOrLoss = 0
   while len(queue) != 0 :
    gainOrLoss += (queue.pop(0))
   print("Your total capital gain or loss is: $" + str(gainOrLoss))


#This is a while loop created so that the user can decided wether they are buying, selling, and/or ending a transaction. This also calls the other functions so that the correct info will be displayed
while buyOrSell != "end" :
    buyOrSell =input ("Type 'buy' if you are buying stocks and 'sell' if you are selling them. Type 'end' when you have no more transactions to input: ")
    if buyOrSell == "buy":
        buyShares()
    if buyOrSell == "sell":
       sellShares()
    else:
        buyOrSell == "end"

if buyOrSell == "end":
        capitalGainsLoss()
