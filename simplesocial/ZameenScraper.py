# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:47:14 2018

@author: Umar Bin Khalid
"""

import requests
from bs4 import BeautifulSoup


"""
This module parses listings on 'zameen.com'.
By 10 March 2018, it was tested on Lahore city on houses for sale and for rent.
Please, see the following functions to understand how it works:
    __init__(self, ... )
    getListings(self)
"""
class Zameen:
    location_link = ""
    price_min = 0
    price_max = 0
    purpose = 0
    page = 1

    def __init__(self, location_link = 'https://zameen.com/Homes/Lahore_Johar_Town-93-1.html',
                 price_min = 0,
                 price_max = 0,
                 purpose = 0,
                 page = 1):
        """Constructor

        Keyword arguments:
            location_link -- This is the link which will be parsed however it might be changed due to following arguments.
            price_min -- This argument will determine lower limit of price.
            price_max -- This argument will determine upper limit of price.
            purpose -- This will determine weather to parse '0: Buy/Sell' or '1: Rentals'.
            page -- This will determine which page to parse for a particular area.
        """
        self.location_link = location_link
        self.price_min = price_min
        self.price_max = price_max
        self.purpose = purpose # Buy is 0, rent is 1.
        self.page = page

    def getLink(self):
        linkBreakdown = self.location_link.split("-")
        linkBreakdown[2] = str(self.page) + ".html"

        new_location_link = self.unsplit(linkBreakdown, "-")

        if self.purpose == 1:
            linkBreakdown = self.location_link.split("/")
            linkBreakdown[3] = "Rentals"

            new_location_link = self.unsplit(linkBreakdown, "/")

        if self.price_min > 0:
            new_location_link += "?price_min=" + str(self.price_min)
            if self.price_max > 0:
                new_location_link += "&price_max=" + str(self.price_max)
        elif self.price_max > 0:
            new_location_link += "?price_max=" + str(self.price_max)

        return new_location_link

    def unsplit(self, strlist, splitarg):
        strUnsplit = ""

        for item in strlist:
            strUnsplit += item + splitarg

        return strUnsplit[0:-1]

    def getHtmlDoc(self):
        return requests.get(self.getLink()).text

    def getSoup(self):
        return BeautifulSoup(self.getHtmlDoc(), 'lxml')

    def getListings(self):
        """This method will return parsed data of the desired area.

        In case the page doesn't contain any data, the method will return following:
            self.page -- Number of the page parse.
            0 -- In place of total_pages.
            None -- In place of listings dictionary.

        The method returns following data:
            current_page -- Page which was parsed.
            total_pages -- Total number of pages that were parsed.
            listings -- Dictionary in following format:
                Key: Data index assigned by 'zameen.com' to the listing.
                Value: Another dictionary containing parsed data with following keys:
                    link -- Link to listing on 'zameen.com'.
                    title -- Title of the listing.
                    location -- Location of the property.
                    price -- Price/Rent of the property.
                    area -- Area of the property.
                    description -- Description of the listing.
                    addedBy -- Date on which the listing was created and updated.
                    beds -- Number of beds (can be none)
        """
        listings = {}

        soup = self.getSoup()

        try:
            listings_list = soup.find('ul', attrs={'class': 'left search-list list-view'})
            listing_items = listings_list.findAll('li', attrs={'class': 'listig-card-outter'})
        except AttributeError:
            print("No data on this page.")
            return self.page, 0, None

        for listing in listing_items:
            single = {}
            anchor = listing.find('a')
            listing_dsc = anchor.find('div', attrs={'class': 'listing-card-dsc left'})

            single['link'] = anchor['href'] # Link to listing.
            single['title'] = listing_dsc.find('div', attrs={'class': 'title-wrap'}).div.text # Title.
            single['location'] = listing_dsc.find('div', attrs={'class': 'location'}).text # Location of the property.
            single['price'] = listing_dsc.div.findAll('span')[1].text # Price of the property.
            single['area'] = listing_dsc.find('ul', attrs={'class': 'left slider_pinfo'}).find('li', attrs={'id': 'area'}).span.text # Area of the property.
            single['description'] = listing_dsc.find('p', attrs={'class':'description left'}).text # Description of the property.
            single['addedBy'] = listing_dsc.find('span', attrs={'class':'addedby'}).text # Date on which listing was created and updated.

            # try: # Number of beds.
            #     single['beds'] = listing_dsc.find('ul', attrs={'class': 'left slider_pinfo'}).find('li', attrs={'id': 'bed'}).span.text
            # except AttributeError:
            #     single['beds'] = None

            listings[int(listing['data-index'])] = single

        # page_info = soup.find('div', attrs={'class' : 'pg_counts'}).text
        #
        # current_page = int(page_info.split(" ")[1])
        # total_pages = int(page_info.split(" ")[3].strip())
        return listings
        #return single['price']
        #return single['link']
