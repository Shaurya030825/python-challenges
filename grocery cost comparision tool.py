print("====GROCERY COST COMPARISION CHECKER===")

rice_price = 12
milk_price = 4
fruit_price = 8
number_of_baskets = 2
family_members = 4

basket_cost_per_person = (rice_price + milk_price + fruit_price)
number_of_baskets/family_members

print("/n Part1- This week's shop")
print("Cost per person:", basket_cost_per_person)

print("/n Part2- Sharing he items")
total_items= int(input("Enter the total number of grocery items:"))

people= int(input("Enter the number of people sharing them:"))

if people== 0:
    print("You can't sahre items with 0 people")
else:
    if total_items % people == 0:
        print(total_items,"Items divide equally among", people,"people-",total_items//people, "each.")
    else:
        print(total_items,"Items do not didvide equally among",people,"people-",total_items//people,"left over.")

print("/n Part3- Fixing the weekly average")

recorded_average= 65
total_weeks= 4
wrong_week_cost= 50
correct_week_cost= 80

recorded_total= recorded_average*total_weeks
corrected_total= recorded_total-wrong_week_cost+correct_week_cost
corrected_average = corrected_total/total_weeks

print("Recorded total was:", recorded_total)
print("Corrected total is:", corrected_total)
print("Corrected weekly avearge:", corrected_average)

print("/n Part4- Comparing the stores")

store_a_average  =70
store_b_average= 75
store_c_average= 80

print("Store A:", store_a_average,"| Store B:", store_b_average,"| Store C:", store_c_average)

if corrected_average<store_a_average and corrected_average<store_b_average and corrected_average<store_c_average:
    verdict= "cheaper than all three stores"

elif corrected_average>store_a_average and corrected_average>store_b_average and corrected_average>store_c_average:
    verdict="More expensive than all three stores"
else:
    print("Somewhere in between the three stores")

print("your average is", verdict)

print("/n====SUMMARY====")
print("Cost per person this week:", basket_cost_per_person)
print("Corrected weekly average:", corrected_average)
print("Verdict:", verdict)
