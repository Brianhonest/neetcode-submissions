class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            maX_element=0
            if i == len(arr)-1:
                arr[i]=-1
                break
            for j in range(i+1,len(arr)):
                maX_element=max(maX_element,arr[j])
            arr[i]=maX_element
        return arr