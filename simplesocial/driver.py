import ZameenScraper

##print(ZameenLHRLocations.Locations().getLocations())



def mypythonfunction(minimum,maximum,yourpurpose):

    zameen_listings = ZameenScraper.Zameen(location_link = 'https://beta.zameen.com/Homes/Lahore_Johar_Town-93-1.html',
                                                                           price_min = minimum,
                                                                           price_max = maximum,
                                                                           purpose = yourpurpose,
                                                                           page = 1).getListings()

    return zameen_listings
