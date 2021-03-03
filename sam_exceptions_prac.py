###########################################################
##  try :
       ## Run this code
## except :
      ## Execute this code when there is an exception
##  else:
     ## Run this code when No exceptions
## finally :
     ## Always run this code irrespective of Exception 
#########################################################
## assert :
        ## Test if condition is true
## This will stop the execution and will not move if any exception

x=14
try:
    if x > 5:
        raise Exception ('X should not be greater than 5')
except:
    print('Exception raised')
else:
    print('Else clause..')
finally:
    print('Execute irrespective of Exceptions ..')
print('After else clause')

##Write a program that creates a log file with errors and critical messages.

