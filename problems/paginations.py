from rest_framework.pagination import (
    LimitOffsetPagination,
)

class ProblemLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10