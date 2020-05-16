#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:19:23 2020

@author: karun
"""

# MIT 60001 pset1

# Define variables

portion_down_payment = 0.25
current_savings = 0.0
r = 0.04

# Retrieve user input

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the precent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

monthly_salary = annual_salary/12.0
down_payment_needed = total_cost * portion_down_payment
number_of_months = 0

while current_savings < down_payment_needed:
    current_savings += (monthly_salary * portion_saved)
    # Savings have returns
    current_savings += current_savings * r/12
    # Increment month counter
    number_of_months += 1
    
print("Number of months: ",number_of_months)
    

