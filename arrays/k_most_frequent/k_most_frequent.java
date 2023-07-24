package k_most_frequent;
import java.util.HashMap;
import java.util.ArrayList;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> count = new HashMap<>();
        ArrayList<ArrayList<Integer>> freqs = new ArrayList<>();
        while (freqs.size() <= nums.length) {
            freqs.add(new ArrayList<>());
        }

        for (int num : nums) {
            count.put(num, 1 + count.getOrDefault(num, 0));
        }
        for (int key : count.keySet()) {
            freqs.get(count.get(key)).add(key);
        }

        int[] res = new int[k];
        int j = 0;
        for (int i = freqs.size() - 1; i >= 0; i--) {
            for (int l = 0; l < freqs.get(i).size(); l++) {
                res[j] = freqs.get(i).get(l);
                j++;
                if (j == k) {
                    return res;
                }
            }
        }
        return null;
    }
}