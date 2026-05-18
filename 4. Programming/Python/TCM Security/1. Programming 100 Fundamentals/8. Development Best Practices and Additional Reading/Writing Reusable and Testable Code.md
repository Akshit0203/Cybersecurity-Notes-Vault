Writing testable code means organizing your code in a way that makes it easy to test individual components (e.g., functions or classes) without relying on external systems (like databases, APIs, or user input). Testable code typically follows principles such as **separation of concerns**, **clear inputs and outputs**, and **minimal side effects**.

### Example of Writing Testable Code

Let’s start with an example of **non-testable code** and refactor it to make it more **testable**.
#### Non-Testable Code Example:
```
def atm_withdrawal():
    balance = int(input("Enter your current balance: "))
    amount = int(input("Enter the amount to withdraw: "))
    
    if amount > balance:
        print("Insufficient funds")
    elif amount <= 0:
        print("Invalid amount")
    else:
        balance -= amount
        print(f"Transaction successful. Your new balance is: {balance}")
```

#### Problems:

1. **Hardcoded I/O**: The `input()` and `print()` functions are directly tied to the function, making it difficult to test without user interaction.
2. **No Clear Inputs or Outputs**: The function doesn't take parameters or return values, which makes it difficult to simulate scenarios in tests.

#### Refactored Testable Code:
```
def atm_withdrawal(balance, amount):
    if amount > balance:
        return "Insufficient funds", balance
    elif amount <= 0:
        return "Invalid amount", balance
    else:
        balance -= amount
        return "Transaction successful", balance
```

### Improvements:

**Clear Inputs and Outputs**:

- - The function now takes two arguments: `balance` and `amount`, making it easy to test with different values.
    - It returns the result message and the new balance, making it possible to verify the results without relying on `print()`.

**No Side Effects**:

- - The function doesn’t interact with external systems like user input, making it easy to test in isolation.

### Example Tests for the Refactored Code

You can now easily write tests for this function, using a testing framework like `unittest`.
```
import unittest

class TestATMWithdrawal(unittest.TestCase):

    def test_insufficient_funds(self):
        message, new_balance = atm_withdrawal(100, 150)
        self.assertEqual(message, "Insufficient funds")
        self.assertEqual(new_balance, 100)

    def test_invalid_amount(self):
        message, new_balance = atm_withdrawal(100, -20)
        self.assertEqual(message, "Invalid amount")
        self.assertEqual(new_balance, 100)

    def test_successful_transaction(self):
        message, new_balance = atm_withdrawal(100, 50)
        self.assertEqual(message, "Transaction successful")
        self.assertEqual(new_balance, 50)

if __name__ == "__main__":
    unittest.main()
```

### Explanation:

1. **Test for Insufficient Funds**: Verifies that when the withdrawal amount exceeds the balance, the correct message is returned and the balance remains unchanged.
2. **Test for Invalid Amount**: Ensures that a withdrawal of a non-positive amount returns the correct error message and doesn’t modify the balance.
3. **Test for Successful Transaction**: Verifies that a valid withdrawal reduces the balance and returns the correct success message.

### Why This is Testable Code:

- **No Dependencies**: The function doesn’t rely on user input, print statements, or external resources like databases or APIs.
- **Easy to Verify**: The function returns values that can easily be checked by test cases.
- **Separation of Concerns**: The function is focused solely on performing the withdrawal logic and returning the result, making it easy to reason about and test different cases.

### Key Principles for Writing Testable Code:

1. **Avoid Side Effects**: Minimize external interactions like file access, database calls, or user input inside functions. These make the function hard to test.
2. **Clear Inputs and Outputs**: Functions should accept parameters and return results. This makes them predictable and easy to test by feeding in specific inputs and checking the outputs.
3. **Small, Focused Functions**: Write functions that do one thing and do it well. This improves testability and reduces complexity.
4. **Use Dependency Injection**: If a function or class relies on an external system, pass those dependencies as parameters (e.g., a database connection or an API client), so you can substitute them with test objects or mocks during testing.
5. **Write Tests in Parallel**: As you write your code, write tests to ensure your code behaves as expected. This promotes writing testable code from the start.

### A Deeper Explanation:

In your setup, the **test_atm.py** file interacts with **atm.py** through **importing** the `atm_withdrawal` function from the `atm.py` module. Here's a detailed explanation of how the interaction works:

### 1. **Importing the Function from** `**atm.py**`:

In **test_atm.py**, you have this line at the top:

```
from atm import atm_withdrawal
```

This line tells Python to import the `atm_withdrawal` function from the file **atm.py** (which in this case is treated as a Python module). Python finds the `atm.py` file, looks for the `atm_withdrawal` function inside it, and makes that function available for use in the **test_atm.py** file.

### 2. **How Import Works**:

- **from atm import atm_withdrawal** looks for a file named `atm.py` in the current directory (or within Python’s module search path). If it finds the file, it will import the `atm_withdrawal` function and make it available in the test script.
- Once imported, the function `atm_withdrawal()` can be used inside the test cases just like any function defined within the same file.

### 3. **Executing Tests in** `**test_atm.py**`:

In **test_atm.py**, you write the unit test cases using the `unittest` framework:

```
import unittest
from atm import atm_withdrawal

class TestATMWithdrawal(unittest.TestCase):

    def test_insufficient_funds(self):
        message, new_balance = atm_withdrawal(100, 150)
        self.assertEqual(message, "Insufficient funds")
        self.assertEqual(new_balance, 100)

    def test_invalid_amount(self):
        message, new_balance = atm_withdrawal(100, -20)
        self.assertEqual(message, "Invalid amount")
        self.assertEqual(new_balance, 100)

    def test_successful_transaction(self):
        message, new_balance = atm_withdrawal(100, 50)
        self.assertEqual(message, "Transaction successful")
        self.assertEqual(new_balance, 50)

if __name__ == "__main__":
    unittest.main()
```

### Key Interactions:

- **Calling the** `**atm_withdrawal**` **Function**: Each test case calls the `atm_withdrawal` function (imported from `atm.py`) with different inputs to simulate different scenarios. For example:
    - `atm_withdrawal(100, 150)` in the first test case simulates trying to withdraw more money than is in the account.
    - `atm_withdrawal(100, -20)` simulates trying to withdraw an invalid amount (negative or zero).
    - `atm_withdrawal(100, 50)` simulates a successful transaction.
- **Assertions**: The test cases then use `self.assertEqual()` to check if the returned values from `atm_withdrawal()` match the expected output. For example:
    - In the `test_insufficient_funds()` test, the test checks if the message returned is `"Insufficient funds"` and if the balance remains unchanged.

### Flow of Interaction:

**Test Setup**:

- `test_atm.py` imports the `atm_withdrawal` function from `atm.py`.

**Test Execution**:

- When you run the tests (e.g., `python3 test_atm.py`), Python executes the code within `test_atm.py`. This causes each test case to run, and each one calls the `atm_withdrawal` function with different inputs.

**Function Execution**:

- When the `atm_withdrawal` function is called from a test, Python switches execution to the `atm_withdrawal` function inside `atm.py`. The logic in `atm_withdrawal` is executed based on the inputs provided by the test case.

**Results Returned**:

- After executing the logic in `atm_withdrawal`, the results (a message and the new balance) are returned to the test case in `test_atm.py`.

**Assertions**:

- The test case then checks whether the returned results match the expected outcomes. If they do, the test passes; if not, the test fails.

**Test Results**:

- After running all test cases, the results are printed to the console, showing which tests passed and which failed.

### Example of the Workflow:

- The `test_insufficient_funds()` test runs and calls `atm_withdrawal(100, 150)`.
- Inside `atm.py`, the `atm_withdrawal` function checks if the amount (`150`) is greater than the balance (`100`). Since it is, the function returns `"Insufficient funds"` and the original balance (`100`).
- The test case in `test_atm.py` then asserts that the returned message is `"Insufficient funds"` and that the balance remains `100`.
- If the assertion passes, the test case is marked as successful.

### Why It Works:

The `import` statement bridges the two files, allowing `test_atm.py` to use the function defined in `atm.py` as if it were written in the same file. This separation of code and tests is a common pattern in software development, making it easier to maintain and organize the project. By running tests in isolation from the code logic, you ensure that each function works as expected under various conditions.


```
def atm_withdrawal(balance, amount):
    if amount > balance:
        return "Insufficient funds", balance
    elif amount <= 0:
        return "Invalid amount", balance
    else:
        balance -= amount
        return "Transaction successful", balance
python
import unittest
from atm import atm_withdrawal

class TestATMWithdrawal(unittest.TestCase):

    def test_insufficient_funds(self):
        message, new_balance = atm_withdrawal(100,150)
        self.assertEqual(message, "Insufficient funds")
        self.assertEqual(new_balance, 100)

    def test_invalid_amount(self):
        message, new_balance = atm_withdrawal(100,-20)
        self.assertEqual(message, "Invalid amount")
        self.assertEqual(new_balance, 100)

    def test_successful_transaction(self):
        message, new_balance = atm_withdrawal(100,50)
        self.assertEqual(message, "Transaction successful")
        self.assertEqual(new_balance, 50)

if __name__ == "__main__":
    unittest.main()
```

