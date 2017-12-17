"""Created by sgoswami on 7/19/17."""
"""Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false."""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        start_times = [interval.start for interval in intervals]
        end_times = [interval.end for interval in intervals]
        start_times = sorted(start_times)
        end_times = sorted(end_times)

        room_count, available_rooms, s, e = 0, 0, 0, 0

        while s < len(start_times):
            if start_times[s] < end_times[e]:
                if available_rooms == 0:
                    room_count += 1
                else:
                    available_rooms -= 1
                s += 1
            else:
                available_rooms += 1
                e += 1
        return room_count == 1








