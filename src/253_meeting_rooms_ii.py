"""Created by sgoswami on 7/6/17."""
"""Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required."""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # start_times = []
        # end_times = []
        # for i, v in enumerate(intervals):
        #     start_times.append(v.start)
        #     end_times.append(v.end)
        # start_times = sorted(start_times)
        # end_times = sorted(end_times)
        #
        # num_rooms, available_rooms, s, e = 0, 0, 0, 0
        #
        # while s < len(start_times):
        #     if start_times[s] < end_times[e]:
        #         if available_rooms == 0:
        #             num_rooms += 1
        #         else:
        #             available_rooms -= 1
        #         s += 1
        #     else:
        #         available_rooms += 1
        #         e += 1
        #
        # return num_rooms
        start_times, end_times = [], []
        for i,v in enumerate(intervals):
            start_times.append(v.start)
            end_times.append(v.end)
        start_times = sorted(start_times)
        end_times = sorted(end_times)

        s = e = 0
        num_rooms = available = 0
        while s < len(start_times):
            if start_times[s] < end_times[e]:
                if available == 0:
                    num_rooms += 1
                else:
                    available -= 1
                s += 1
            else:
                available += 1
                e += 1

        return num_rooms







