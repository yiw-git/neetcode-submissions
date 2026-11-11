
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        result = []

        left, right = intervals[0]

        for start, end in intervals[1:]:

            if start <= right:
                # Overlapping intervals
                right = max(right, end)

            else:
                # No overlap: save previous interval
                result.append([left, right])

                # Start a new interval
                left, right = start, end

        # Don't forget the last interval
        result.append([left, right])

        return result
