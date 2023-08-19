# XML_to_DB_parser

Basic XML to DataBase parser on python

## Running

After staring provide .XML filename and press ENTER.

Console results should look like tihs:
    
    File name: test_data.xml
    Parsing CATEGORIES...
    Done parsing CATEGORIES!
    Parsing TEASERS...
    Done parsing TEASERS!

And DataBase should have filled tables:

    sqlite> SELECT * FROM TEASERS;
    +------+------+-----------------------------------+-----------------------------------+-------------------------+----------------------+--------------------------------------------------------------+--------+
    | T_ID | C_ID |                URL                |              PICTURE              |          TITLE          |        VENDOR        |                             TEXT                             | ACTIVE |
    +------+------+-----------------------------------+-----------------------------------+-------------------------+----------------------+--------------------------------------------------------------+--------+
    | 1029 | 4    | https://test.site.com/test/?t1=1  | https://test.site.com/imgs/i1.jpg | Discount on Phones      | Phone Discount       | Galaxystore - the official Samsung brand store.              | 1      |
    +------+------+-----------------------------------+-----------------------------------+-------------------------+----------------------+--------------------------------------------------------------+--------+
    | 818  | 16   | https://test.site.com/test2/?t1=2 | https://test.site.com/imgs/i1.jpg | Discount on Electronics | Electronics Discount | "Technopark" is a network of household appliances and electr | 1      |
    |      |      |                                   |                                   |                         |                      | onics stores.                                                |        |
    +------+------+-----------------------------------+-----------------------------------+-------------------------+----------------------+--------------------------------------------------------------+--------+
    | 949  | 4    | https://test.site.com/test2/?t1=2 | https://test.site.com/imgs/i2.jpg | Discount on Electronics | Electronics Discount | "Center" Corporation - a store for household appliances and  | 1      |
    |      |      |                                   |                                   |                         |                      | electronics!                                                 |        |
    +------+------+-----------------------------------+-----------------------------------+-------------------------+----------------------+--------------------------------------------------------------+--------+
    sqlite> SELECT * FROM CATEGORIES;
    +------+----------------------------------+
    | C_ID |             CATEGORY             |
    +------+----------------------------------+
    | 4    | Electronics and Appliances       |
    | 1    | Clothing, Shoes, and Accessories |
    | 7    | Health and Beauty                |
    | 9    | Jewelry and Accessories          |
    | 16   | Services                         |
    | 12   | Pets                             |
    | 14   | Courses                          |
    | 6    | Gift Ideas                       |
    | 13   | Home and Garden                  |
    | 8    | Kids and Baby                    |
    | 18   | Hypermarket                      |
    | 5    | Groceries                        |
    +------+----------------------------------+
