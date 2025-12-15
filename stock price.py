# Stock Portfolio Tracker

# Predefined stock prices (you can update these)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "AMZN": 130
}

portfolio = {}  # To store user's stocks

print("Welcome to Stock Portfolio Tracker!\n")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("Stock not available. Try again.")
        continue
    
    try:
        shares = int(input(f"Enter number of shares for {stock}: "))
        if shares <= 0:
            print("Number of shares must be positive.")
            continue
        # Add or update the portfolio
        if stock in portfolio:
            portfolio[stock] += shares
        else:
            portfolio[stock] = shares
    except ValueError:
        print("Please enter a valid number for shares.")
        continue

# Calculate total value
total_value = 0
print("\nYour Portfolio:")
for stock, shares in portfolio.items():
    value = shares * stock_prices[stock]
    total_value += value
    print(f"{stock}: {shares} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal Portfolio Value: ${total_value}")