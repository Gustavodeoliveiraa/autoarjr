def get_and_strip_request_param(self, param):
    return self.request.GET.get(param, '').strip()
