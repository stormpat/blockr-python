from blockr.api import Api

api = Api('bitcoin', 'text')
print api.block_info([1,'2','3', 4])