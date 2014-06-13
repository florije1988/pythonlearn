# -*- coding: utf-8 -*-
__athor__ = 'florije'
import curses
import urllib
import json

if __name__ == '__main__':
    if 1 > 0:
        a = 100

    if not '':
        print 'florije'

    else:
        print 'xiaoqibao'

    data = {
        "Local": "zh_CN",
        "Version": "1.1",
        "Request": {
            "CustomerIPAddress": "192.168.1.1",
            "RatePlanId": "1008686001",
            "Contact": {
                "Mobile": "13581518255",
                "Name": "daqibao"
            },
            "LatestArrivalTime": "17:00",
            "CurrencyCode": "RMB",
            "AffiliateConfirmationId": "1008686001",
            "ArrivalDate": "2014-06-11",
            "RoomTypeId": "100",
            "ConfirmationType": "Phone",
            "HotelId": "100",
            "OrderRooms": [
                {
                    "Customers": [
                        {
                            "Name": "xiaoqibao",
                            "Gender": 1,
                            "IdType": 1,
                            "IdNo": "1130181198812125566"
                        },
                        {
                            "Name": "dongdong",
                            "Gender": 1,
                            "IdType": 1,
                            "IdNo": "1320181198812125566"
                        }
                    ]
                }
            ],
            "DepartureDate": "2014-06-12",
            "TotalPrice": 256,
            "PaymentType": 1,
            "EarliestArrivalTime": "12:00",
            "CustomerType": 1,
            "NumberOfCustomers": 2,
            "NumberOfRooms": 2
        }
    }

    sessionid = 123456
    order_id = '1008686001'
    order_price = '256'
    hotel_name = '北京旅馆'
    room_type = 1
    hotel_longitude = '0'
    hotel_latitude = '0'
    hotel_city = '北京'

    str_url = 'sessionid=%s&order_id=%s&order_price=%s&hotel_name=%s&room_type=%s&hotel_longitude=%s&hotel_latitude=%s&hotel_city=%s&data=%s' \
              % (sessionid, order_id, order_price, hotel_name, room_type, hotel_longitude, hotel_latitude, hotel_city,
                 json.dumps(data))
    print str_url
    print urllib.quote(str_url)

    result = {
        'Local': 'zh_CN',
        'Version': '1.1',
        'Request': {
            'NumberOfRooms': 2,
            'LatestArrivalTime': '17:00',
            'TotalPrice': 256,
            'ConfirmationType': 'Phone',
            'ArrivalDate': '2014-06-11',
            'CurrencyCode': 'RMB',
            'CustomerIPAddress': '192.168.1.1',
            'OrderRooms': [
                {
                    'Customers': [
                        {
                            'Gender': 1,
                            'IdNo': '1130181198812125566',
                            'Name': 'xiaoqibao',
                            'IdType': 1
                        },
                        {
                            'Gender': 1,
                            'IdNo': '1320181198812125566',
                            'Name': 'dongdong',
                            'IdType': 1
                        }
                    ]
                },
                {
                    'Customers': [
                        {
                            'Gender': 1,
                            'IdNo': '1130181198812125566',
                            'Name': 'xiaoqibao',
                            'IdType': 1
                        },
                        {
                            'Gender': 1,
                            'IdNo': '1320181198812125566',
                            'Name': 'dongdong',
                            'IdType': 1
                        }
                    ]
                }
            ],
            'RatePlanId': '1008686001',
            'PaymentType': 1,
            'Contact': {
                'Mobile': '13581518255',
                'Name': 'daqibao'
            },
            'EarliestArrivalTime': '12:00',
            'NumberOfCustomers': 4,
            'RoomTypeId': '100',
            'AffiliateConfirmationId': '1008686001',
            'CustomerType': 1,
            'HotelId': '100',
            'DepartureDate': '2014-06-12'
        }
    }

    # print result['Request']['OrderRooms']['Customers']  # it's wrong， 我看错了

    x = [1, 2, 3]
    x.extend([4, 5])
    print (x)

    list_cus = [
        {'Gender': 1, 'IdNo': '1130181198812125566', 'Name': 'xiaoqibao', 'IdType': 1},
        {'Gender': 1, 'IdNo': '1320181198812125566', 'Name': 'dongdong', 'IdType': 1}
    ]


    # str_param = 'timestamp=1402479595&signature=6f08b04853686069e0e5626d09b96a9a&user=e1a5055630793717b31a12c73364c3dc&format=json&method=hotel.order.create&data={"Local":"zh_CN","Version":"1.1","Request":{"CustomerIPAddress":"192.168.1.178","RatePlanId":103794,"Contact":{"Mobile":"8885551212","Name":"AppleseedJohn"},"LatestArrivalTime":"17:00","CurrencyCode":"RMB","AffiliateConfirmationId":"smallpay_1401777203","ArrivalDate":"2014-06-05","RoomTypeId":"0010","ConfirmationType":"Phone","HotelId":"10101129","OrderRooms":[{"Customers":[{"Name":"刘文","Gender":"Female"}]}],"DepartureDate":"2014-06-06","TotalPrice":"600.22","PaymentType":"SelfPay","EarliestArrivalTime":"12:00","CustomerType":"Chinese","NumberOfCustomers":"1","NumberOfRooms":"1"}}'

    test_data = {
        'Local': 'zh_CN',
        'Version': '1.1',
        'Request': {
            'NumberOfRooms': 2,
            'LatestArrivalTime': '17:00',
            'TotalPrice': 256,
            'ConfirmationType': 'Phone',
            'ArrivalDate': '2014-06-12',
            'CurrencyCode': 'RMB',
            'CustomerIPAddress': '192.168.1.1',
            'OrderRooms': [
                {
                    'Customers': [
                        {
                            'Gender': 1,
                            'IdNo': '1130181198812125566',
                            'Name': 'xiaoqibao',
                            'IdType': 1
                        },
                        {
                            'Gender': 1,
                            'IdNo': '1320181198812125566',
                            'Name': 'dongdong',
                            'IdType': 1
                        }
                    ]
                },
                {
                    'Customers': [
                        {
                            'Gender': 1,
                            'IdNo': '1130181198812125566',
                            'Name': 'xiaoqibao',
                            'IdType': 1
                        },
                        {
                            'Gender': 1,
                            'IdNo': '1320181198812125566',
                            'Name': 'dongdong',
                            'IdType': 1
                        }
                    ]
                }
            ],
            'RatePlanId': '1008686001',
            'PaymentType': 1,
            'Contact': {
                'Mobile': '13581518255',
                'Name': 'daqibao'
            },
            'EarliestArrivalTime': '12:00',
            'NumberOfCustomers': 4,
            'RoomTypeId': '100',
            'AffiliateConfirmationId': '1008686001',
            'CustomerType': 1,
            'HotelId': '100',
            'DepartureDate': '2014-06-15'
        }
    }

    test_data_json = json.dumps(test_data)

    pre_params = 'timestamp=1402479595&signature=6f08b04853686069e0e5626d09b96a9a&user=e1a5055630793717b31a12c73364c3dc&format=json&method=hotel.order.create&data='
    total_params = pre_params + test_data_json

