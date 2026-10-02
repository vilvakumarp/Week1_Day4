🧪 How to trigger and test the various HTTP cases
The easiest way to see these cases in action is by opening http://127.0.0 and running tests via Swagger UI:
-------------------------------------------------------------------------------------
🟩 Case 1: 200 OK (Successful calculation)
• Action: Send a POST request to /calculate with this JSON payload:json
{
  "num1": 15,
  "num2": 5,
  "operation": "multiply"
}


Use code with caution.
• Result: You will get a 200 OK response with a computed result of 75.

-------------------------------------------------------------------------------------
🟥 Case 2: 400 Bad Request (Mathematical failure)
• Action: Attempt to divide a number by zero:json
{
  "num1": 10,
  "num2": 0,
  "operation": "divide"
}
Use code with caution.
• Result: Server blocks the action and returns a 400 Bad Request stating "Math Error: Division by zero...".

-------------------------------------------------------------------------------------

🟧 Case 3: 422 Unprocessable Entity (Schema / Data validation failure)
• Action: Pass text strings instead of numbers, or type an operation that isn't allowed:json
{
  "num1": "hello",
  "num2": 5,
  "operation": "invalid_op"
}
Use code with caution.
• Result: FastAPI automatically intercepts the execution before running code, returning a structured 422 error detailing exactly what failed input validation.
-------------------------------------------------------------------------------------

🚫 Case 4: 404 Not Found
• Action: In your browser or client, try accessing an endpoint that isn't built into the code, such as http://127.0.0.
• Result: The system outputs an instantaneous 404 Not Found response.
-------------------------------------------------------------------------------------