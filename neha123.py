import CSV
def write_into_(SV(info_list)):
   with open ('student_onfo.CSV','a',newline='')as CSV_file:
   writer=CSV.writer(CSV_file)
   if CSV_file.tell()==0:
   writer.writerow (["Name,"Age","Contact number","E-mail Id"])
   writer.writerow(info_list)
 if__name__=='__main__':
   condition=True
   Student_num=1
   while(condition):
        student_info=input("Enter student information for student #{} in the following format(Name Age Contact_number E-mail Id):"format(Student_num))
        print("Entered information:"+student_info)
        student_info_list=student_info.split('')
        print("Entered split up information is :"+str(student_info_list))
        print("\n the entered information is-\n Name :{}\n Age:{}\n Contact_number:{}\n Email Id:{}".format (student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3],))
        choice_check=input("Is the entered information correct?(yes/no):")
        if choice_check=="yes":
           write_info_CSV(student_info_list)
           condition_check=input("Enter(yes/no)if you want to enter information for other student:")
           if condition check=="yes":
             condition = true
             student_num=student_num+1
           elif condition check=="no":
             condition = false
       elif choice_check=="no":
           print ("\n please re-enter the values!")
           
        
