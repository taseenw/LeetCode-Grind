class Solution {
    public boolean isPalindrome(int x) {
        int remainder;
        int rev=0;
        int org=x;
        while(x>0){
            remainder=x%10;
            rev=rev*10+remainder;
            x=x/10;
        }
        if(rev==org){
            return true;
        }else{
            return false;
        }
    }
    
}