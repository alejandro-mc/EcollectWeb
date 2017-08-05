#read data file
with open ('weatherdata','r') as wd:
     lines = wd.readlines()



#map data to sql insert statement
insert = 'insert into newentry_weatherdata'
columns = '(time_recorded,station_id,temperature,humidity,preassure)'
insert = insert + ' ' + columns

#-remove end of line
stripped = map(lambda x : x.replace('\n','') ,lines)

#-map station letter codes to integer
ids= {'KNYC':1,'KLGA':2,'KJRB':3,'KJFK':4}

separate = map(lambda x : x.split(',') ,stripped)
with_numid = map(lambda x :[ x[0] ]  + [ str (ids[x[1]]) ] + x[2:] ,separate)



#compose psql statement
sql_lines = []
for values in with_numid:
   time_recorded,station_id,temperature,humidity,preassure = values
   data = "VALUES ('{0}',{1},{2},{3},{4})".format(time_recorded,station_id,temperature,humidity,preassure)
   sql_lines.append('{0} {1};\n'.format(insert,data))


with open('insertWeatherData','a') as wd:
    for line in sql_lines:
        wd.write(line) 
   




