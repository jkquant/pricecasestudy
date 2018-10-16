# pricecasestudy

Python module containing a set of classes / functions which can price a basic consumer loan given the following inputs:
-amount,
-term in months,
-apr,
-lending date,
-repayment_day_of_month

returns:
-the annuity amount
-the future cashflow schedule (due date, amount due on date, capital component, interest component, and any other relevant info)

Files:
File1 = yobota_price.py
File2 = test_yobotaprice.py

File1:-
Loan Class: Contains the following data and methods
class inputs:
-self.principal = principal amount
-self.n = number of periods in months
-self.interest = (apr/100)/12
-self.loan_date = lending date
-self.pay_day = repayment_day_of_month

class output: 
-future cash flow schedule
Execute file with command line parameters: 
  para1=amount para2=term_in_months para3=APR para4=lending_date(format=yyyy-mm-dd) para5=repayment_day_of_month
  
from command line run: 
          python yobota_price.py 10000 12 5 2018-10-11 1
outputs cash flow schedule in a pandas dataframe

File2: Unittest for ValueErrors and TypeErrors
from command line run: 
          pyhton -m unittest
          
