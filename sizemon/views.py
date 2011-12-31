from django.http import HttpResponse
from sizemon.models import Snapshot, Path
import operator

def show_home(request):
    data = {}

    snapshots = Snapshot.objects.order_by('-crdate')[:2]
    for snapshot in snapshots:
        paths = snapshot.path_set.all()
        for path in paths:
            if path.path in data:
                data[path.path].append(path.size)
            else:
                data[path.path] = [path.size]

    diff = {}
    for path in data:
        sizes = data[path]
        if len(sizes) > 1:
            if sizes[0] != sizes[1]:
                diff[path] = sizes[0] - sizes[1]

    list = sorted(diff.iteritems(), key=operator.itemgetter(1))

    response = HttpResponse()
    response['Content-Type'] = 'text/plain'
    for line in list:
        response.write('%s\t%s\n' % (line[0], line[1]))
    return response
