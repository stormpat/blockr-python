""" This module contains the utility functions for the main module. """

def request_type(request):
    """ If the request is for multiple addresses, build a str with separator """
    if isinstance(request, list):
        request = ",".join(request)
    return request

# def have_confs(confirmations):
#     """ If the request has URI params we add them to the request string """
#     confs = {'confirmations': confirmations}
#     if confs['confirmations'] > 0:
#         return True
#     else:
#         return False
