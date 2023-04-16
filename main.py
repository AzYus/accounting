from application.salary import calculate_salary
from application.db.people import get_employees
get_employees()
calculate_salary()



from datetime import date
current_date = date.today()
print(current_date)

