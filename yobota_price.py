import sys
import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import datetime
import math
from dateutil.relativedelta import *

class Loan(object):
    
    @property
    def principal(self): 
        return self._principal
    @principal.setter
    def principal(self, principal):
        if type(principal) == int or type(principal) == float:
            self._principal = principal
        else:
            raise TypeError("principal must be an int or float")
    
    
    @property
    def interest(self): 
        return self._interest
    @interest.setter
    def interest(self, interest):
        if type(interest) == int or type(interest) == float:
            self._interest = interest
        else:
            raise TypeError("interest must be an int or float")
    
    @property
    def n(self): return self._n
    @n.setter
    def n(self, n):
        if type(n) == int and n > 0:
            self._n = n
        else:
            raise ValueError("n must be an int > 0")
     
    @property
    def loan_date(self): return self._loan_date
    @loan_date.setter
    def loan_date(self, loan_date):
        if type(loan_date) == datetime.date or type(loan_date) == type(None):
            self._loan_date = loan_date
        else:
            raise TypeError("date must be a datetime.date object")
            
            
    @property
    def pay_date(self): return self._pay_date
    @pay_date.setter
    def pay_date(self, pay_date):
        if type(pay_date) == datetime.date or type(pay_date) == type(None):
            self._pay_date = pay_date
        else:
            raise TypeError("date must be a datetime.date object")
            
            
            
    def __init__(self, principal, n, apr, loan_date, pay_day):
        self.principal = principal
        self.n = n
        self.interest = (apr/100)/12
        self.loan_date = loan_date
        self.pay_day = pay_day
        year,month,day = loan_date.year,loan_date.month, loan_date.day
        self.pay_date = datetime.date(year,month,pay_day)
        
    def __str__(self):
        if self.loan_date:
            return str('%15s   APR: %g   Term: %g   Amount: %g ' %
                       (self.loan_date, self.interest, self.n, self.principal))
        return str('APR: %g   Term: %g   Amount: %g' %
                   (self.interest, self.n, self.principal)) 
    
    def payment_m(self):
        '''Returns the monthly payment due'''
        payments = np.pmt(self.interest, self.n, self.principal)
        return abs(payments)

    def capital_m(self):
        '''Returns the capital component of monthly payment due'''
        per = 1
        ppmt = np.ppmt(self.interest, per, self.n, self.principal)
        return abs(ppmt)

    def interest_m(self):
        '''Returns the interest component of monthly payment due'''
        per = 1
        ipmt = np.ipmt(self.interest, per, self.n, self.principal)
        return abs(ipmt)
    
    
    def schedule(self, startPeriod=1, endPeriod=None):
        '''Returns Future Cashflow Schedule'''
        periods = []
        
        if not endPeriod:
            endPeriod = self.n
            
        period = startPeriod  
        term_months = endPeriod
        
        while period <= endPeriod:
            self.n = term_months
            monthly_annuity_payment = self.payment_m()
            annuity_capital = self.capital_m()
            annuity_interest = self.interest_m()
            
            balance = self.principal - annuity_capital 
            #print(monthly_annuity_payment, annuity_capital, annuity_interest, balance, term_months)
            data = (self.pay_date, monthly_annuity_payment, annuity_capital, annuity_interest, balance, period)
            periods.append(list(data))

            self.principal = float(balance)
            term_months -=1
            self.pay_date = self.pay_date+relativedelta(months=+1)
            period += 1

        return periods


if __name__=='__main__':
    
    principal_amount = float(sys.argv[1])  
    term = int(sys.argv[2])
    apr = int(sys.argv[3])
    lend_date = str(sys.argv[4])  #format yyyy-mm-dd
    repay_day = int(sys.argv[5])

    year,month,day = lend_date.split('-')
    print(year, month,day)
    lend_date = datetime.date(int(year), int(month), int(day))
    
    loan1 = Loan(principal_amount, term, apr, lend_date, repay_day) 
    schedule = loan1.schedule()

    col_names = ['date', 'Payment Amount', 'Ammount Applied to Primcipal', 'Amount Applied to Interest', \
            'Remaining Balance', 'Current Period']

    df_schedule = pd.DataFrame(schedule, columns = col_names)
    df_schedule = df_schedule.round(2)
    print(df_schedule)
