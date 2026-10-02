from enum import Enum
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Robust Calculator API",
    description="An API testing various HTTP responses using JSON payloads.",
    version="2.0.0"
)

# 1. Define allowed operations using an Enum
class OperationType(str, Enum):
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"

# 2. Define the JSON Request Structure using Pydantic
class CalculationRequest(BaseModel):
    num1: float = Field(..., description="The first number", example=10.5)
    num2: float = Field(..., description="The second number", example=2.0)
    operation: OperationType = Field(..., description="Operation: add, subtract, multiply, or divide")

# --- ROUTES & HTTP CASES ---

# Case: 200 OK (Root landing)
@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {
        "status": "online",
        "message": "Send a POST request to /calculate with a JSON body.",
        "test_docs": "http://127.0.0"
    }

# Case: Dynamic Error Testing and 200 OK Payload processing
@app.post("/calculate", status_code=status.HTTP_200_OK)
def calculate(payload: CalculationRequest):
    op = payload.operation
    a = payload.num1
    b = payload.num2
    
    # Case: 400 Bad Request (Mathematical or Logical rule broken)
    if op == OperationType.DIVIDE and b == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Math Error: Division by zero is mathematically undefined."
        )
        
    # Process valid operations
    if op == OperationType.ADD:
        result = a + b
    elif op == OperationType.SUBTRACT:
        result = a - b
    elif op == OperationType.MULTIPLY:
        result = a * b
    elif op == OperationType.DIVIDE:
        result = a / b
    else:
        # Fallback safety validation error
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported operation type."
        )

    return {
        "success": True,
        "operation": op,
        "inputs": {"num1": a, "num2": b},
        "result": result
    }

# Case: 403 Forbidden Simulation (Example of a restricted endpoint)
@app.get("/admin-metrics")
def read_admin():
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Access Denied: You do not have the required administrative clearance."
    )
