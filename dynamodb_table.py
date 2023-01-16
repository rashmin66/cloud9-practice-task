import boto3

# #Get the service resource.
dynamodb = boto3.resource('dynamodb')

##Create the DynamoDB table.
# table = dynamodb.create_table(
#     TableName='SL_Cricket_ODI_Captains_R',
#     KeySchema=[
#         {
#             'AttributeName': 'player_name',
#             'KeyType': 'HASH'
#         },
#         {
#             'AttributeName': 'year',
#             'KeyType': 'RANGE'
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'player_name',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'year',
#             'AttributeType': 'N'
#         },
#         
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 10,
#         'WriteCapacityUnits': 10
#     }
# )
# print("creating table...")
# # Wait until the table exists.
# table.wait_until_exists()

# # Print out some data about the table.
# print(table.item_count)
table = dynamodb.Table('SL_Cricket_ODI_Captains_R')
#print(table.creation_date_time)


# Prepare the items
items = [
    {'player_name': 'Aravinda de Silva', 'year': 1992, 'ODI_match_runs': '9284', 'average_ODI_match_runs':'34.90', 'ODI_win_persentage': '27.78'},
    {'player_name': 'Aravinda de Silva', 'year': 1992,'ODI_match_runs': '9284','average_ODI_match_runs':'34.90', 'ODI_win_persentage': '27.78'},
    {'player_name': 'Roshan Mahanama',   'year': 1994,'ODI_match_runs': '5162','average_ODI_match_runs':'29.49', 'ODI_win_persentage': '50'},
    {'player_name': 'Sanath Jayasuriya', 'year': 1998,'ODI_match_runs': '13364','average_ODI_match_runs':'32.51', 'ODI_win_persentage': '55.56'},
    {'player_name': 'Marvan Athapaththu','year': 2001,'ODI_match_runs': '8529','average_ODI_match_runs':'37.57', 'ODI_win_persentage': '55.56'},
    {'player_name': 'Mahela Jayawardana','year': 2004,'ODI_match_runs': '12381','average_ODI_match_runs':'33.01', 'ODI_win_persentage': '53.97'},
    {'player_name': 'Chaminda Vas',      'year': 2006,'ODI_match_runs': '2018', 'average_ODI_match_runs':'13.72', 'ODI_win_persentage': '0'},  
    {'player_name': 'Kumar Sangakkara',  'year': 2009,'ODI_match_runs': '13975','average_ODI_match_runs':'41.96', 'ODI_win_persentage': '60'},
    {'player_name': 'T.M. Dilshan',      'year': 2010,'ODI_match_runs': '10290','average_ODI_match_runs':'39.27', 'ODI_win_persentage': '42.31'},
    {'player_name': 'Angelo Mathews',    'year': 2012,'ODI_match_runs': '5835','average_ODI_match_runs':'41.67', 'ODI_win_persentage': '47.12'},
    {'player_name': 'Dinesh Chandimal',  'year': 2013,'ODI_match_runs': '3854','average_ODI_match_runs':'31.85', 'ODI_win_persentage': '50'},
    {'player_name': 'Lahiru Thirimanna', 'year': 2015,'ODI_match_runs': '3194','average_ODI_match_runs':'34.71', 'ODI_win_persentage': '33.33'},
    {'player_name': 'Upul Tharanga',     'year': 2016,'ODI_match_runs': '6941','average_ODI_match_runs':'33.85', 'ODI_win_persentage': '42.86'},
    {'player_name': 'Thisara Perera',    'year': 2017,'ODI_match_runs': '2338','average_ODI_match_runs':'19.98', 'ODI_win_persentage': '33.33'},
    {'player_name': 'Dimuth Karunarathne','year': 2020,'ODI_match_runs': '767','average_ODI_match_runs':'21.22', 'ODI_win_persentage': ''},
    {'player_name': 'Dasun Shanaka',     'year': 2022,'ODI_match_runs': '946','average_ODI_match_runs':'24.89', 'ODI_win_persentage': ''},
    ]


# Use a batch_writer to write the items
with table . batch_writer() as batch:
    for item in items:
      batch.put_item(Item=item)
 
 
 ##getting an item     
# response = table.get_item(
#     Key={
#         'player_name': 'Dasun Shanaka',
#         'year': 2022, 
#     }
# )
# item = response['Item']
# print(item)
  
      
##deleting an item
# table.delete_item(
#     Key={
#         'player_name': 'Dasun Shanaka',
#         'year': 2022, 
#     }
# )

