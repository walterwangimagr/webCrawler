from selenium import webdriver
import re

href = "property/residential/sale/auckland/auckland-city/mount-wellington/listing/3727438227?rsqid=28aa521284744ed9b883a25211b0bf75-004"
if href.startswith("property"):
    href = "/a/" + href
    print(href)
