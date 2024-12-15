🧩🧩BANK APPLICATION

🧨CONCEPTS:

🧨FEATURES:
      Class  BankAccount
      1. Create Account
      2. Deposit
      3. Withdraw
      4. Transfer
      5. Show Transactions
      6. Save and Exit

🧨PARAMETERS:


🧨APPROACH:
      Option1: CREATE ACCOUNT
           1. call create_account(accounts) method
                 1.1 inside method :
                  User input
                        1)Account number 2)Account holder name
                  Create object called new_Account of BankAccount class with:
                        1)Account number 2)Account holder
                  Append new_Account in accounts:
                        1)accounts = load_accounts()

       Option2: DEPOSIT AMOUNT
           1. User input acc_number
           2. if account exist using next() method then
           3. try: 
                 User input amount
                 call deposit(amount) method 
                             Inside method:
                                   if amount > 0 then balance =+ amount and record_transaction
                                   
              except ValueError:
            4. else account don't exist
      
              
                  

      
           
            

🧨METHODS REQUIRED:

