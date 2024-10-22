# Payment Gateway System

## Overview

This repository contains the implementation of a **Payment Gateway System** designed to manage users, their balances, and transaction services including top-ups, withdrawals, transfers, and saldo management. The system is built using Python and utilizes SQLite for database operations

## Usage
To run the application, simply execute the main script:

```python
python main.py
```

## Objectives
The main objectives of this system are to provide the basic functionality required in a financial application, including:

1. **User Registration**: Allows users to create an account with an email and password, and a number used for transfers.
2. **Balance Management**: Allows users to view, update, and add to their balances.
3. **Balance Top-up**: Provides options for users to add to their balances through certain methods.
4. **Balance Transfer**: Facilitates balance transfers between users in the system.
5. **Balance Withdrawal**: Allows users to withdraw their balance.

## Key Features
- User Registration and Authentication: Users can create an account and authenticate to access other features.
- Balance Management: Users can view their balance, top up, and withdraw money.
- Transfer Between Users: Users can transfer balances to other users in the system.
- Activity Logging: All activities in the system are recorded for auditing and troubleshooting purposes.

## Workflow
1. New users register by filling in their email, password, and transfer number.
2. The system creates an initial balance for new users with a total balance of 0.

3. Users can view their balances and top up using their preferred method.
4. The system updates the balance every time a user tops up, transfers, or withdraws.
5. Users can transfer balances to other users and view transfer history.
6. Users can withdraw balances according to the desired amount, and the system will update the balance automatically.

## Use Case Study
1. User Registration
    - New users can register with the email "yanto@example.com" and a predetermined password.

    - After successfully registering, users will get a unique ID that will be used in subsequent transactions.

2. Balance Management

    - Users can top up their balance with a certain amount.

    - After top-up, users can view the updated balance and ensure the transaction is successful.

3. Transfer Between Users
    - Users can transfer balances from one user to another by entering the recipient user ID and the amount they want to transfer.

    - The system will update the balance for both users after the transfer is successful.

4. Balance Withdrawal
    - Users can withdraw an amount of balance from their accounts.

    - After withdrawal, the balance will be updated to reflect the amount withdrawn.

## Technologies Used
- Programming Language: Python
- Database: SQLite
- Design Pattern: Repository Service
- Logging: Python logging to record system activity.