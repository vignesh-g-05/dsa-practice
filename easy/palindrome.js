/*
125. Valid Palindrome

Input: "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Worst case: when a number has no non-alphanumeric and
*/

/*
Time Complexity: O(n)
Space Complexty: O(n)
*/
function solution1(str) {
  const regex = /[^a-zA-Z0-9]/g;
  const normalizedString = str.replace(regex, "").toLocaleLowerCase();
  if (normalizedString.length < 2) return true;
  let rev = "";
  for (let i = 0; i < normalizedString.length; i++) {
    rev = normalizedString[i] + rev;
  }
  return rev === normalizedString;
}

/*
Time Complexity: O(n/2) -> O(n)
Space Complexty: O(n)
*/
export function solution2(str = "") {
  const regex = /[^a-zA-Z0-9]/g;
  const normalizedString = str.replace(regex, "").toLocaleLowerCase();
  if (normalizedString.length < 2) return true;
  let fir = 0;
  let las = normalizedString.length - 1;
  while (fir < las) {
    if (normalizedString[fir++] !== normalizedString[las--]) {
      return false;
    }
  }
  return true;
}
