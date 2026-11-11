class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #create stack for the non assigned values 
        #[38] now comes 38, if the stack i not empty; then compare 38 with each of them and reord the index diff two list, one for the date waiting, the other for the date diff
        dates=[]#record index
        dif_date=[0]*len(temperatures) #record the 1,3,4,5,

        for i in range(len(temperatures)): #i is idx
            temp=temperatures[i]
            if dates==[]:
                dates.append(i)
            else:
                while dates:
                    
                    if temp<=temperatures[dates[-1]]:
                        dates.append(i)
                        break
                    else:
                        day_idx=dates.pop()
                        dif_date[day_idx]=i-day_idx
                   
                if not dates:
                    dates.append(i)
        return dif_date





