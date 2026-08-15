#july25_2026

#our "monthly" global variables
salary = 12400 #paid
google_one = 34.99 
bedroom_suit_or_phone = 1091.4 #paid
yt_prem = 104.99 #paid
tfg = 400 
rent_water_fee = 4400 #paid
uber = 900 #(catered for afternoons only)
wifi = 679 #paid
stokvel_amount = 500 #reserved
upwork_freelancer_plus = 200 #(I think)

month_list = [google_one, bedroom_suit_or_phone, yt_prem, tfg, rent_water_fee,
              uber, wifi, stokvel_amount, upwork_freelancer_plus]

two_man_sofa = 1400
#more purchases to potentially be added...still to decide which
two_sweats_outfits = 300 #(assuming I target two that are 150 each)
shein_sneakers = 250
fifty_piece_love_capsules = 16

july_tot_august_purchases = []

rem_after_monthly_costs = salary - sum(month_list) - sum(july_tot_august_purchases)

avail_weekly_spend = rem_after_monthly_costs / 4

print(salary)

print("\n--------------------- purchases for our 25 July 2026 salary --------------------\n")

print(f"\nremaining after all monthly costs: \n{rem_after_monthly_costs}\n")

print("-"*80)

print(f"\navailable weekly spend: \n{avail_weekly_spend}\n")

print("-"*80)



#I have a feeling, to make this easire / user friendly, that I am going to have
#to figure out how to take input from a user of what they want to purchase,
#how much it is and append that shit to the 'purchases' list

#yah nor because adding the items into the list manually is dumb and error-prone

