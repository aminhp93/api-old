from rest_framework.pagination import (
    LimitOffsetPagination,
)

class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10