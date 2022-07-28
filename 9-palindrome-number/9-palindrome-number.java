class Solution {
    public boolean isPalindrome(int x) {
        boolean isPalindrome = true;
        String xS = String.valueOf(x);
        int parse = xS.length()/2;
        for(int y=0;y<parse;y++){
            if(xS.charAt(y) != xS.charAt(xS.length()-1-y)){
                return false;
            }
        }
        return isPalindrome;
    }
}