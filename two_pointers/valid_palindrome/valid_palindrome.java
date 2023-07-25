package two_pointers.valid_palindrome;

class Solution {
    public boolean isPalindrome(String s) {
        String res = "";
        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetterOrDigit(s.charAt(i))) res+=s.charAt(i);
        }
        res = res.toLowerCase();

        int start = 0;
        int end = res.length() - 1;
        while (start < end) {
            if (res.charAt(start) != res.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}