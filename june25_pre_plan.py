#our "monthly" global variables
salary = 12400
google_one = 34.99
bedroom_suit_or_phone = 1091.4
yt_prem = 104.99
tfg = 200
rent_water_fee = 4400
uber = 900 #(catered for afternoons only)
wifi = 679
stokvel_amount = 500
#upwork_freelancer_plus = 200 #(I think)

month_list = [google_one, bedroom_suit_or_phone, yt_prem, tfg, rent_water_fee,
              uber, wifi, stokvel_amount]

bar_fridge_sixty60 = 2050
#shein_sneakers_roughly = 200
#infl_ushaped_sofa_roughly = 250
office_chair = 564 #: https://www.takealot.com/eay-eay-thing-mesh-office-chair-ergonomic-computer-armchair-typi/PLID96906234

#june_tot_july_purchases = {"bar_fridge_sixty60":2000,
                           #"shein_sneakers_roughly":200,
                           #"infl_ushaped_sofa_roughly":250}

june_tot_july_purchases = [bar_fridge_sixty60, office_chair]

rem_after_monthly_costs = salary - sum(month_list) - sum(june_tot_july_purchases)

avail_weekly_spend = rem_after_monthly_costs / 4

print(salary)

print("\n--------------------- purchases for our 25 June 2026 salary --------------------\n")

print(f"\nremaining after all monthly costs: \n{rem_after_monthly_costs}\n")

print("-"*80)

print(f"\navailable weekly spend: \n{avail_weekly_spend}\n")

print("-"*80)

#okay, it's fine. after I buy the fridge and HAVE IT IN THE KITCHEN, I will put together i-plan for the office chair

#this one was a success...I managed to get both the office chair and the fridge