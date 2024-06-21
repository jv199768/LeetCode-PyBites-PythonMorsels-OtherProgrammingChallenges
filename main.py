# main.py

from fastapi import FastAPI, HTTPException
import stripe

# Replace with your Stripe secret key
stripe.api_key = "your-stripe-key"

app = FastAPI()

@app.post("/process-payment/")
async def process_payment(amount: int, currency: str, token: str):
    try:
        # Create a charge using the Stripe API
        charge = stripe.Charge.create(
            amount=amount,
            currency=currency,
            source=token,  # Stripe token obtained from the client-side (e.g., Stripe.js)
            description="Payment for FastAPI Store",  # Add a description for the payment
        )

        # You can handle the charge object as per your requirements
        # For example, log the payment or perform other actions

        # Return a success response
        return {"status": "success", "charge_id": charge.id}

    except stripe.error.CardError as e:
        # Handle specific Stripe errors
        return {"status": "error", "message": str(e)}
    except stripe.error.StripeError as e:
        # Handle generic Stripe errors
        return {"status": "error", "message": "Something went wrong. Please try again later."}


# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
    print(process_payment(1, "USD", {
  "id": "cpt_1PUCXiP5jaLWbHpDjcbo9bR3",
  "object": "token",
  "client_ip": "71.178.184.226",
  "created": 1718995838,
  "livemode": false,
  "type": "person",
  "used": false
}))
