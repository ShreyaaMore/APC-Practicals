"""Payment gateway simulation module."""

def process_payment(amount, method="UPI"):
    print(f"Processing payment of Rs. {amount:.2f} via {method}...")
    return {
        "status": "SUCCESS",
        "method": method,
        "amount": amount,
        "tx_id": "TXN987654321"
    }

