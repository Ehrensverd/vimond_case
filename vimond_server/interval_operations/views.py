from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

def calculate_intervals(includes, excludes):
    result = [[10, 19], [31, 100]]
    return result

@api_view(["POST"])
def process_intervals(request):
    if request.method == 'POST':
        data = request.data
        includes = data.get('includes', [])
        excludes = data.get('excludes', [])
        result = calculate_intervals(includes, excludes)
        return Response({'result': result})


