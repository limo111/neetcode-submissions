class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        result=[]

        for num in nums:
            count[num]=count.get(num,0)+1

        for _ in range(k):
            key=max(count,key=count.get)
            result.append(key)
            del count[key]
        return result