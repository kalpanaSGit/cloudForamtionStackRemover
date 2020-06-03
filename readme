# cloudformation-stakc-remover
## About Serverless function
    This is serverless lambda fucntion written using Python to Delete the stacks if its more than 14 days old.
    A CloudWatch event triggers a Lambda which will retrieve a list of all stacks.

## The criteria to delete a stack are:
    
    1. The stack Status should be one of these ['CREATE_COMPLETE' , 'UPDATE_COMPLETE', 'ROLLBACK_FAILED', 'DELETE_FAILED', 'ROLLBACK_COMPLETE']
    2. The LastUpdatedTime is more than 14 days old
    3. The CloudWatch event is set to trigger the Lambda at 2am AEST each day.
