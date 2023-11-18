from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

def calculate_intervals(includes, excludes):
    def merge_intervals(intervals):
        """Merge overlapping intervals.
        
        Sorts the intervals based on their start point.
        Then merges overlapping intervals into a single interval.
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current_start, current_end in intervals[1:]:
            # Unpack the last merged interval
            last_merged_start, last_merged_end = merged[-1]
            
            # If the current interval overlaps with the last merged interval, merge them
            if current_start <= last_merged_end:
                merged[-1] = [last_merged_start, max(current_end, last_merged_end)]
            else:
                # Otherwise, add the current interval as a new entry
                merged.append([current_start, current_end])

        return merged

    def subtract_intervals(incl, excl):
        """Subtract exclude intervals from include intervals.
        
        Iterates through each include interval and adjusts its range
        based on the exclude intervals.
        """
        result = []
        exclude_index = 0

        for include_start, include_end in incl:
            # Advance exclude index if exclude interval ends before the current include interval starts
            while exclude_index < len(excl) and excl[exclude_index][1] < include_start:
                exclude_index += 1

            # Process overlapping exclude intervals
            while exclude_index < len(excl) and include_start <= include_end:
                exclude_start, exclude_end = excl[exclude_index]
                
                # If the exclude interval starts after the current start of include interval,
                # add the non-overlapping part to the result
                if include_start < exclude_start:
                    result.append([include_start, min(exclude_start - 1, include_end)])

                # Adjust the start of the include interval to the end of the exclude interval
                # and move to the next exclude interval if it's completely covered
                if exclude_end < include_end:
                    include_start = exclude_end + 1
                    exclude_index += 1
                else:
                    include_start = include_end + 1

            # If there's any part of the include interval left, add it to the result
            if include_start <= include_end:
                result.append([include_start, include_end])

        return result

    # Merge overlapping intervals within includes and excludes
    merged_includes = merge_intervals(includes)
    merged_excludes = merge_intervals(excludes)

    # Subtract exclude intervals from include intervals
    return subtract_intervals(merged_includes, merged_excludes)



@api_view(['POST'])
def api_process_intervals(request):
    if request.method == 'POST':
        includes = request.POST.get('includes', '')
        excludes = request.POST.get('excludes', '')
        includes_list = [list(map(int, interval.split('-'))) for interval in includes.split(',')]
        excludes_list = [list(map(int, interval.split('-'))) for interval in excludes.split(',')]
        result = calculate_intervals(includes_list, excludes_list)
        return Response({'result': result})
    else:
        return Response({'error': 'Invalid request method'})


def html_process_intervals(request):
    if request.method == 'POST':
        includes = request.POST.get('includes', '')
        excludes = request.POST.get('excludes', '')
        includes_list = [list(map(int, interval.split('-'))) for interval in includes.split(',')]
        excludes_list = [list(map(int, interval.split('-'))) for interval in excludes.split(',')]
        result = calculate_intervals(includes_list, excludes_list)
    else:
        result = None

    return render(request, 'interval_operations/interval_operations.html', {'result': result})