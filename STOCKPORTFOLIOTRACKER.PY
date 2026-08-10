STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 330,
    "META": 300,
    "NFLX": 480, 
}
def show_avilable_stock():
    print("\nAvailable stock and prices (per share):")
    for symbol, price in STOCK_PRICES.item():
        print(f" {symbol}: ${price}")
def get_portfolio():
            portfolio = {}
            print("\nEnter stock symbol and quantity. Type 'done' as symbol to finish.")
            while True:
                symbol = input("\nStock symbol: ").upper().strip()
                if symbol == "DONE":
                    break
                if symbol not in STOCK_PRICES:
                    print(f"'{symbol}'not found in price list . Please choose from the available stocks.")
                    continue
                try:
                    quantity = int (input (f"Quantity of {symbol}: "))
                    if quantity <= 0:
                        print("Quantity must be a positive number.")
                        continue
                except ValueError:
                    print ("Please enter a valid integer quantity.")
                    continue
                portfolio[symbol] = portfolio.get(symbol,0) + quantity
                print(f"Added {quantity} share( s )of {symbol}.")
                return portfolio
def calculate_investment(portfolio):
                breakdown = {}
                total = 0
                for symbol, quantity in portfolio.items():
                    value = STOCK_PRICES[symbol] * quantity
                    breakdown[symbol] = (quantity,STOCK_PRICES[symbol], value)
                    total += value
                    return breakdown, total
def save_to_file(breakdown, total, filename="portfolio_summary.txt"):
      with open (filename, "W") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("=" * 40 +"\n")
            f.write(f"{'Symbol':<10}{'Qty':8}{'Price':<10}{'Value':<10}\n")
            f.write("_" * 40 + "\n")
            for symbol,(qty, price, value) in breakdown.items():
                  f.write(f"{symbol:<10}{qty:<8}${price:<9}${value:<9}\n")
                  f.write("- "* 40 + "\n")
                  f.write(f"Total Investment :  ${total}\n")
                  print(f"\nSummary saved to '{filename}'.")
      def main():
                    print("=" * 40)
                    print("Stock Portfolio Tracker")
                    print("=" * 40)
                    show_avilable_stock()
                    portfolio = get_portfolio()
                    if not portfolio:
                        print("\nNo stocks entered. Exiting.")
                        return
                    breakdown, total = calculate_investment(portfolio)
                    print("\n" + "=" * 40)
                    print("Portfolio summary")
                    print("=" * 40)
                    print(f"{'Symbol' :<10}{'Qty':<8}{'Price':<10}{'Value':<10}")
                    print("_" * 40)
                    for symbol, (qty , price, value)in breakdown.items():
                        print(f"{symbol:<10}{qty:<8}${price:<9}${value:<9}")
                        print("_" * 40)
                        print(f"Total Investment Value: ${total}")
                        save_choice = input ("\nSave this summary to a file?(y/n):").lower().strip()
                        if save_choice == "y":
                            save_to_file(breakdown, total)
                            if __name__ == "__main__":
                                main()