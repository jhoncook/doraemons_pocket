total   = int(input("enter time in seconds="))
seconds = int( total%60)
total   = total - seconds
hours   = int(total / 3600)
total   = total - (hours * 3600)
mins    = int(total / 60)
print("time in hh:mm:ss=",hours,":",mins,":",seconds)
