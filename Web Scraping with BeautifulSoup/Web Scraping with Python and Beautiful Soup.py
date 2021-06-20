from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup  # TODO -> learn more about: BeautifulSoup

my_url = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709'

uReq(my_url)
# opens a connection and download the web-page
u_client = uReq(my_url)
page_html = u_client.read()  # dumps everything out of this page in html code, into the variable
u_client.close()

# html parser
page_soup = soup(page_html, "html.parser")
# print(page_soup.h1)  # print the header of the page
# print(page_soup.p)  # print some paragraph from the page
# print(page_soup.body.span)

# grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})
# for div in containers:
#     print(div)

contain = containers[0]
# container = containers[0]
# print(container.a)

filename = "products.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"

f.write(headers)


for index, container in enumerate(containers, 1):
    brand = contain.div.div.a.img["title"]
    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text
    shipping_container = contain.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()

    print(f"{index}- Brand: {brand}")
    print(f"-  Product name: {product_name}")
    print(f"-  Shipping: {shipping}")

    f.write(brand + ', ' + product_name.replace(',', '') + ', ' + shipping + "\n")

f.close()
