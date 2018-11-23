import boto3

rds = boto3.client('rds')

try:
    response = rds.create_db_instance(
        DBInstanceIdentifier='pyawstestnkv',
        MasterUsername='dbadmin',
        MasterUserPassword='AppleAnd5Bananascom',
        DBInstanceClass='db.t2.micro',
        Engine='mariadb',
        AllocatedStorage=5)
    print response
except Exception as error:
    print error
