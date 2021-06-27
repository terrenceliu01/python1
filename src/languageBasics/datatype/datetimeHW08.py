from datetime import date, timedelta

current_date = date.today().isoformat()   
days_before = (date.today()-timedelta(days=30)).isoformat()
days_after = (date.today()+timedelta(days=30)).isoformat()  

print("\nCurrent Date: ",current_date)
print("30 days before current date: ",days_before)
print("30 days after current date : ",days_after)
