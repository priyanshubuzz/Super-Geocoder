from geopy.geocoders import ArcGIS
import pandas

arc = ArcGIS()

def add_latlon(filename):
    df = pandas.read_csv(filename)

    #Making DF capitalized to avoid index error if user has address in lower case
    capitalized_columns = [i.capitalize() for i in df.columns]
    df.columns = capitalized_columns

    df["Address"] = df["Address"].apply(arc.geocode, timeout=20)
 
    #Preparing Lat Lon data with Exception handling
    Lat=[]
    for i in df["Address"]:
        try:
            Lat.append(i[1][0])
        except:
            Lat.append("NaN")
    df["Lat"] = Lat 

    Lon=[]
    for i in df["Address"]:
        try:
            Lon.append(i[1][1])
        except:
            Lon.append("NaN")
    df["Lon"] = Lon 

    #saving Df with Lat and Lon as CSV
    df.to_csv(f"Processed_{filename}")

    #prepairing a nested list with column row and all rows
    nested_list = [df.columns.values.tolist()] + df.values.tolist()
    return nested_list