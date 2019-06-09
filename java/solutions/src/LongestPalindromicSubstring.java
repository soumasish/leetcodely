import java.util.HashMap;
import java.lang.*;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        HashMap<String, Integer> hmap = new HashMap<String, Integer>();
       
        int max = 0;
        int longestCount = 0;
        int start = 0; 
        for(int i=0;i<s.length();i++){
            String ch = Character.toString(s.charAt(i));
            if(hmap.get(ch) == null){
                hmap.put(ch, i);
                longestCount++;
                
            } else{  
                max = Math.max(max,longestCount);
    
                if (start <= hmap.get(ch) ){
                    int buff = i - hmap.get(ch);

                    if(buff<longestCount){
                        longestCount = buff;
                    } 
                    start = hmap.get(ch)+1;
                }
                else {
                    longestCount++;
                }
                
                hmap.put(ch, i);
            }
            max = Math.max(max,longestCount);
            
        }
        return max;
    }
}