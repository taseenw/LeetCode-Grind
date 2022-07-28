class Solution(object):  
    def merge(self, nums1, m, nums2, n):   
        #Combine lists
        p=0;
        for x in range(m,m+n):
            nums1[x]=nums2[p]
            p=p+1
       #Merge Sort combined list
        def mergeSort(nums1):
            if len(nums1) > 1:
                lefts=nums1[:len(nums1)//2]
                rights=nums1[len(nums1)//2:]

                mergeSort(lefts)
                mergeSort(rights)

                x=0
                y=0 
                z=0 

                while x<len(lefts) and y<len(rights): 
                    if lefts[x]<rights[y]: 
                        nums1[z]=lefts[x]
                        x+=1 
                    else: 
                        nums1[z] = rights[y]
                        y+=1 
                    z+=1

                while x<len(lefts):
                    nums1[z]=lefts[x]
                    x+=1
                    z+=1

                while y<len(rights):
                    nums1[z]=rights[y]
                    y+=1
                    z+=1

            return nums1                
        
        return mergeSort(nums1)