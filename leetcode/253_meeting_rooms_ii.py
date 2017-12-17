"""Created by sgoswami on 7/6/17."""
"""Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required."""


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start_times = [item.start for item in intervals]
        end_times = [item.end for item in intervals]
        start_times = sorted(start_times)
        end_times = sorted(end_times)
        available_rooms, num_rooms, s, e = 0, 0, 0, 0

        while s < len(start_times) and e < len(end_times):
            if start_times[s] < end_times[e]:
                if available_rooms == 0:
                    num_rooms += 1
                else:
                    available_rooms -= 1
                s += 1
            else:
                available_rooms += 1
                e += 1
        return num_rooms
