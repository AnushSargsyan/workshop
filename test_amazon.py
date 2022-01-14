import logging
from amazon_page import go_to_page, logging
from  amazon_page import searching
import amazon_page
import pytest
from selenium import webdriver

import logging


def test_search_item_from_amazon(get_driver):
    try:
        amazon_page.go_to_page('https://www.amazon.com/')
        amazon_page.searching(get_driver)
        assert len(amazon_page.search_results) > 0 , "Any cases Failed"
        
    except Exception as e:
        logging(e)



