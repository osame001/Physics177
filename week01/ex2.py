import numpy as np
import matplotlib.pyplot as plt

homework = np.array([10. , 10. , 8. , 9.5 , 3. , 9. , 0. , 6.])

exam = np.array([10. , 10. , 10. , 10. , 8. , 5. , 10. , 7.])

finalproject = np.array([9. , 10. , 10. , 6. , 10. , 6. , 8. , 9.])


finalgrade = (homework + exam + finalproject)/3
for i in finalgrade:
    if(i<6):
        print "failed" , i
    if(i>9.5):
        print  "awesome" , i
print finalgrade
 
plt.hist(finalgrade)
plt.title("finalgrades of students")
plt.xlabel("student's number")
plt.ylabel(" final grade")
plt.savefig("newplot.jpeg" , format="jpeg")
