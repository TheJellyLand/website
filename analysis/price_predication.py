from matplotlib import pyplot as plt

#The Token Supply
tokenIds = range(0,10000)

#Price Multipler
PRICE_FACTOR = 0.00001

#Calculate Price
price = [x * PRICE_FACTOR if x not in range(0,100) else 0 for x in tokenIds]

#Plot
#plt.theme('windows')
plt.style.use('classic')
plt.title("NFT Price vs. Token ID", fontsize=22)
plt.ylabel("Price (ETH)", fontsize=18)
plt.xlabel("Token ID", fontsize=18)
plt.xlim([0,10000])
plt.ylim([0,.102])
plt.scatter(list(tokenIds), list(price))
plt.show()
plt.savefig("price_prediction")
