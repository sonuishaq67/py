class githubApiError(Exception):

    def __init__(self, status_code ):
        if status_code==403:
            message="Rate limit reached"
        else
         