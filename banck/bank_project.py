class BalanceException(Exception):
    """Raised when an account has insufficient funds for an operation."""
    pass


class BankAccount:
    """Simple bank account with deposit, withdraw and transfer support."""

    def __init__(self, initial_amount: float, account_name: str):
        if initial_amount < 0:
            raise ValueError("initial_amount must be >= 0")
        self.balance = float(initial_amount)
        self.name = str(account_name)
        print(f"Account '{self.name}' created. Balance = ${self.balance:.2f}")

    def get_balance(self) -> float:
        """Return the current balance and print a user-friendly message."""
        print(f"Account '{self.name}' balance: ${self.balance:.2f}")
        return self.balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self.balance += amount
        print('\nDeposit complete.')
        self.get_balance()

    def _ensure_sufficient_funds(self, amount: float) -> None:
        """Raise BalanceException if the account doesn't have enough balance."""
        if amount <= 0:
            raise ValueError("amount must be positive")
        if self.balance < amount:
            raise BalanceException(
                f"Sorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount: float) -> None:
        """Withdraw amount from the account after validating funds."""
        # Let BalanceException propagate to the caller so calling code/tests
        # can handle it. Validation for amount positivity is done in
        # _ensure_sufficient_funds.
        self._ensure_sufficient_funds(amount)
        self.balance -= amount
        print('\nWithdraw complete.')
        self.get_balance()

    def transfer_to(self, target: 'BankAccount', amount: float) -> None:
        """Transfer amount from this account to target account with validation.

        Raises BalanceException if insufficient funds.
        """
        if not isinstance(target, BankAccount):
            raise TypeError("target must be a BankAccount instance")
        if amount <= 0:
            raise ValueError("transfer amount must be positive")

        # ensure funds and perform atomic transfer
        self._ensure_sufficient_funds(amount)
        self.balance -= amount
        target.balance += amount
        print(f"\nTransferred ${amount:.2f} from '{self.name}' to '{target.name}'.")
        print("Source:")
        self.get_balance()
        print("Target:")
        target.get_balance()
