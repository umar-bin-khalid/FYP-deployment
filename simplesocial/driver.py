import ZameenScraper

##print(ZameenLHRLocations.Locations().getLocations())



def mypythonfunction(loc,minimum,maximum,yourpurpose):

    zameen_listings = ZameenScraper.Zameen(location_link = loc,
                                            price_min = minimum,
                                            price_max = maximum,
                                            purpose = yourpurpose,
                                            page = 1).getListings()

    return zameen_listings
