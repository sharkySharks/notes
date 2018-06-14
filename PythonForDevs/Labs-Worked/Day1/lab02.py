
shares = 125
sharePrice = 25.32
sellPrice = 48.97
profit = shares * (sellPrice - sharePrice)

print 'The profit from selling my {0} shares at ${2:.2f} is ${1:,.2f}.'.format(shares, profit, sellPrice)

productPrice = 127.99
salePercent = .16
reducedPrice = productPrice - productPrice * salePercent

print 'The new price for the product is ${:.2f}.'.format(reducedPrice)
