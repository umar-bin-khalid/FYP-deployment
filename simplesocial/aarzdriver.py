import pyAarz

##print(ZameenLHRLocations.Locations().getLocations())



def mypythonfunction(loc,minimum,maximum,yourpurpose):

    aarz_listings = pyAarz.Aarz(location= loc,
                                      price_min = minimum,
                                      price_max = maximum,
                                      purpose = yourpurpose,
                                      page = 1).getListings()
    
    return aarz_listings
