from rest_framework.pagination import PageNumberPagination

class MessagePagination(PageNumberPagination):
    """
    custom pagination class for the pagination model

    """
    # default number of pages to return per page
    page_size = 20

    # allow clients to overide page size via the query parameter
    # e.g. /api/messages/?page_size=50

    page_size_query_param = 'page_size'

    # set maximum page size
    max_page_size = 100

