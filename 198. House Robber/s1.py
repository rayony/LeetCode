import itertools

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
           
        #generate valid combination list
        combination = []
        list_tmp = []
        
        for i in range(1,int(len(nums)/2+1)+1):
            list_tmp = [list(x) for x in itertools.combinations(range(len(nums)), i)]
            for j in range(len(list_tmp)):
                if (i==1):
                    #print("direct add to list: ",list_tmp[j])
                    combination.append(list_tmp[j])
                else:
                    isValid = True
                    for k in range(len(list_tmp[j])-1):
                        if (list_tmp[j][k+1] - list_tmp[j][k] ) <= 1:
                            #print("comparing: ",list_tmp[j], "[INVALID] ",list_tmp[j][k]," and ",list_tmp[j][k+1])
                            isValid = False
                            break
                    if (isValid):
                        #print("comparing: ",list_tmp[j],"[VALID]")
                        combination.append(list_tmp[j])
                
        #for i in range(len(combination)):                    
            #print(combination[i])
        
        
        #comparing valid combination list
        max_earning=0
        
        for i in range(len(combination)):
            #print("scenario #",i," - ", combination[i])
            earning = 0

            for j in range(len(combination[i])):
                earning +=nums[combination[i][j]]
                #print("\trobbing #",combination[i][j]," ($",nums[combination[i][j]], ")")                
            #print("total earning: $",earning)

            if earning > max_earning:
                max_earning = earning
                #print("max_earning updated: $",max_earning)
            #print("\n")
        
        #print("max_earning: $",max_earning)
        return max_earning
