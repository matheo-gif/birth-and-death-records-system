
import pymongo


connection = pymongo.MongoClient('localhost',27017)

database = connection['data1']
# collection =database['users']
collection =database['D1_DATA']


data_list = [
    {"name": "Alice wakanesa", "sex":"female","place of death":"female","DOB":"01/01/2000","DOD":"01/01/2000","occupation":"alive","residence":"female","county":"female",
    "Age": 25,"issued_to": "los","national_id": 1234556,"next of kin id": 1234556, "nationality": "Los Angeles","serial no": "1234556"},
    {"name": "john wakanesa", "sex":"female","place of death":"female","DOB":"01/01/2000","DOD":"01/01/2000","occupation":"alive","residence":"female","county":"female",
    "Age": 25,"issued_to": "los","national_id": 1234556,"next of kin id": 1234556, "nationality": "Los Angeles","serial no": "1234556"},
    {"name": "betty wakanesa", "sex":"female","place of death":"female","DOB":"01/01/2000","DOD":"01/01/2000","occupation":"alive","residence":"female","county":"female",
    "Age": 25,"issued_to": "los","national_id": 1234556,"next of kin id": 1234556, "nationality": "Los Angeles","serial no": "1234556"},
    {"name": "mark wakanesa", "sex":"female","place of death":"female","DOB":"01/01/2000","DOD":"01/01/2000","occupation":"alive","residence":"female","county":"female",
    "Age": 25,"issued_to": "los","national_id": 1234556,"next of kin id": 1234556, "nationality": "Los Angeles","serial no": "1234556"},
    {"name": "judy wakanesa", "sex":"female","place of death":"female","DOB":"01/01/2000","DOD":"01/01/2000","occupation":"alive","residence":"female","county":"female",
    "Age": 25,"issued_to": "los","national_id": 1234556,"next of kin id": 1234556, "nationality": "Los Angeles","serial no": "1234556"},
]
insert_many_result = collection.insert_many(data_list)