class Solution {
    public String solution(String s, String skip, int index) {
        StringBuilder answer = new StringBuilder();
        
        for (char c : s.toCharArray()) {
            int s_index = 0;
            while (s_index < index) {
                c = (char) ('a' + (c - 'a' + 1) % 26);
                if (skip.indexOf(c) == -1) {
                    s_index++;
                }
            }
            answer.append(c);
        }
        
        return answer.toString();
    }
}
