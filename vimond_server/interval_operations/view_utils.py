
def convert_to_intervals(interval_string):
    """
    Convert a comma-separated interval string to a list of interval lists.
    Handles both single numbers and ranges.
    """
    def parse_interval(interval):
        parts = [int(num.strip()) for num in interval.split('-')]
        if len(parts) not in [1, 2]:
            raise ValueError(f"Invalid interval format: '{interval}'")
        return parts if len(parts) == 2 else [parts[0], parts[0]]

    return [parse_interval(interval) for interval in interval_string.split(',') if interval.strip()]
