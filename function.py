import json as simplejson
import boto3
from datetime import date

client = boto3.client('cloudformation')

def stack_remover(event, context):
    # TODO implement  
    
    stackStatusList= ['CREATE_COMPLETE' , 'UPDATE_COMPLETE', 'ROLLBACK_FAILED', 'DELETE_FAILED', 'ROLLBACK_COMPLETE']
    today = date.today()
    paginator = client.get_paginator('describe_stacks')
    for stacks in  paginator.paginate():
        for stack in stacks['Stacks']:             
                        if stack['StackStatus'] in stackStatusList:
                            print('StackStatus :' + stack['StackStatus'])
                            print('StackName : ' + stack['StackName'])
                            print('StackLastUpdatedDateTime : ' + str(stack['LastUpdatedTime']))
                            print('StackTags : ' + str(stack['Tags']))
                            stackLastUpdated = stack['LastUpdatedTime'].date()
                            noOfDays = (today-stackLastUpdated).days
                            print('Age of stack in days : ' +str(noOfDays))                            
                            if noOfDays > 14:
                                 response = client.delete_stack(
                                    StackName= stack['StackName']
                                 )
                                 print('Stack has Deleted : ' +stack['StackName'])
