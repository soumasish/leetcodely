"""Created by sgoswami on 7/21/17."""
"""Given the running logs of n functions that are executed in a non-preemptive single threaded CPU, find the exclusive
 time of these functions.
Each function has a unique id, start from 0 to n-1. A function may be called recursively or by another function.

A log is a string has this format : function_id:start_or_end:timestamp. For example, "0:start:0" means function 0 
starts from the very beginning of time 0. "0:end:0" means function 0 ends to the very end of time 0.

Exclusive time of a function is defined as the time spent within this function, the time spent by calling other 
functions should not be considered as this function's exclusive time. You should return the exclusive time of each 
function sorted by their function id."""
#TODO: Doesn't provide exclusive time, current logic supports total time

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = []
        stack = []
        for log in logs:
            fn, typ, tm = log.split(':')
            fn, tm = int(fn), int(tm)

            if typ == 'start':
                stack.append((fn, tm))

            else:
                item = stack.pop()
                res.append((fn, tm - item[1] + 1))
        res = sorted(res, key=lambda x : x[0])
        print(res)
        ans = [x[1] for x in res]
        return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))

