class Solution {
    public boolean isPalindrome(String s) {
        String input = s.replaceAll("[^a-zA-Z0-9]","");
        String reverse = new StringBuilder(input).reverse().toString();
        return input.toLowerCase().equals(reverse.toLowerCase());
    }
}