import ZameenScraper

##print(ZameenLHRLocations.Locations().getLocations())



def mypythonfunction(yourpurpose):

    
    zameen_current_page, zameen_total_pages, zameen_listings = ZameenScraper.Zameen(location_link = 'https://beta.zameen.com/Homes/Lahore_Johar_Town-93-1.html',
                                                                           price_min = 0,
                                                                           price_max = 0,
                                                                           purpose = yourpurpose,
                                                                           page = 1).getListings()
    
    return zameen_listings
