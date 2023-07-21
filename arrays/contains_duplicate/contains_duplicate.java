package contains_duplicate;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public static void main(String[] args) {
        int[] nums = {1,2,3,1};
        System.out.println(containsDuplicate(nums));
    }
    
    public static boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int i : nums) {
            if (seen.contains(i)) {
                return true;
            }
            seen.add(i);
        }
        return false;
    }
}