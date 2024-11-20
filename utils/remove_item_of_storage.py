
def rm_item_of_storage(_object):
    from django.http import QueryDict
    import pprint
    from storage.models import Storage

    if isinstance(_object, QueryDict):
        _object = _object.dict()
    pprint.pprint(_object)

    Storage.objects.filter(nome__icontains=_object.car_model)
