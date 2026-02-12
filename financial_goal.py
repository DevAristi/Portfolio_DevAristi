# --- RETIREMENT PREDICTOR V1.0 ---
# Author: Sebastian Aristi
# Objective: Calculate the exact age of financial freedom based on current habits.

print ("\n" + "#"*60)
print ("LIFETIME FINANCIAL PLANNING TOOL")
print ("#"*60 + "\n")

# --- PHASE 1: DATA INGESTION (Inputs) ---
print(">> SECTION A: USER PROFILE")
name = input("Enter your Name: ")
current_age_str = input("Enter your Current Age (e.g., 19): ")

print("\n>> SECTION B: FINANCIAL STATUS")
currency = input("Currency Symbol ($, MXN, €): ")
current_savings_str = input(f"How much have you save SO FAR? ({currency}): ")

print("\n>> SECTION C: CASH FLOW (Monthly)")
income_str = input(f"Monthly Income ({currency}): ")
expenses_str = input(f"Monthly Expenses ({currency}): ")

print("\n>> SECTION D: THE TARGET")
retirement_goal_str = input(f"What is your 'Freedom Number' (Net Worth Goal)? ({currency}): ")

# --- PHASE 2: DATA PROCESSING (Calculations) ---

# 1. Casting types (Text -> Numbers)
# Age is an integer (whole number), Money is float (decimals)
current_age = int(current_age_str)
current_savings = float(current_savings_str)
income = float(income_str)
expenses = float(expenses_str)
goal = float(retirement_goal_str)

# 2. Financial Math Logic
monthly_savings = income - expenses
annual_savings = monthly_savings * 12

# 3. Gap Analisys (How much is missing?)
money_needed = goal - current_savings

# 4. Time Projections (The most important part)
# Rule: Amount Needed / Monthly Savings = Months Left
months_to_freedom = money_needed / monthly_savings
years_to_freedom = months_to_freedom / 12

# 5. Age Projection
retirement_age = current_age + years_to_freedom

# --- PHASE 3: ANALYTICS REPORT (Output) ---
# This will be improved the next days in order to prioritize the optimization of the code >:)