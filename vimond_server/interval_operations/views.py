from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .interval_processors import calculate_intervals
from .view_utils import convert_to_intervals

@api_view(['POST'])
def api_process_intervals(request):
    if request.method == 'POST':
        data = request.data
        includes = data.get('includes', [])
        excludes = data.get('excludes', [])
        
        # print("INCLUDES\n", includes)
        # print("EXCLUDES\n", excludes)
  
        result = calculate_intervals(includes, excludes)
        return Response({'result': result})
    else:
        return Response({'error': 'Invalid request method'})


def html_process_intervals(request):
    result = None
    error_message = None

    if request.method == 'POST':
        includes = request.POST.get('includes', '')
        excludes = request.POST.get('excludes', '')

        try:
            includes_list = convert_to_intervals(includes) if includes else []
            excludes_list = convert_to_intervals(excludes) if excludes else []

            result = calculate_intervals(includes_list, excludes_list)

        except ValueError as e:
            error_message = str(e)

    return render(request, 'interval_operations/interval_operations.html', {'result': result, 'error_message': error_message})