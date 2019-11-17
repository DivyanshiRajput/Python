def banner(m): #function for printing message 'm' with borders.
    i=0
    end= ""
    while i< len(m)+4: #prints first line of border.
        end= end + "*"
        i=i+1
    print end
    print ("* " + str(m) + " *") #prints message along with "*".
    print end
    return 0

    
