employee_file= open("../File.txt", "r")
# for employee in employee_file.readlines():
 #   print(employee)
print(employee_file.read())
employee_file.close()