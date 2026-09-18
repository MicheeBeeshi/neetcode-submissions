class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #[8,6,10,5,1,7,1] 

        #O(n)
        #move through array, tracking minbuy and best profit as you go
        minbuy =0;
        maxprof =0;
        for i in range(len(prices)):
            # check the profit by substracting the minbuy from current price 
            if(i>0 and prices[i]-minbuy >maxprof):
                maxprof = prices[i]-minbuy
            #at each index, check if this is the minimum price seen so far, and update min buy
            if(i==0 or prices[i]< minbuy ):
                minbuy = prices[i];
        
        return maxprof
    



    # O(n^2)  
    #map: maxtrans{key: maxsell, index: maxbuy} 
    # grab max, find difference between prices[indexofmax]-  prices[indexofmax -1]
    # only replace maxtrans if the difference is the largest youve seen so far
    # repeat until indexofmax-1 = 0
    # create a subarray of everything to the right of max, 
        #grab the new max, repeat above steps until indexofmax-1 = 0
    #repeat until len(subarray) to the right of max <=1
    #return maxsell-maxbuy
   
   
        
    #brute force = O(n^2)
        #repeat for all price array vals
            #find max buy price
            #find max sell
                #calculate difference between maxbuy and every num to its left: diff = val - array[i]
                #store in a map; {key = difference, val = index }
            #repeat for all nums in the left subarray
            #after completing all calculations, find max amoung keys = maxbuy
            #store index of max buy and max sell in map: maxtrans{key = max sell, max buy};

         


 

        