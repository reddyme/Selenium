import webbrowser,sys
sourceAdd=raw_input("Enter source address")
destAdd=raw_input("Enter dest address")
webbrowser.open('https://www.google.com/maps/dir/'+sourceAdd+'/'+destAdd)
