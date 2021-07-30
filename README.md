# Budget Timeline

## Roadmap
- [ ] Make plot of cash flow vs time
- [ ] Pull budget data from Google Sheet
- [ ] Make Flask app (or maybe do this in Go?)
   - [ ] Add authentication
- [ ] Deploy on home-server

## Data Structure
- Transactions: an object of individual transactions that occur throughout the month
    - Parameters
      - Description
      - Day of month
      - Amount

- Timeline: An object of sorted transactions which can also read in transaction data from various sources
   - Parameters:
      - Start date
      - Start cash
