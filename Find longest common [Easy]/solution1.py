"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longestCommonPrefix(strs: list[str]) -> str:

    seeds = strs[0]

    search = ""

    stop_search = False

    for c in seeds:

        search += c

        for each in strs:
            if search not in each[:len(search)]:
                stop_search = True
                break
        
        if stop_search: 
            search = search[:-1]
            break
    
    return search

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["c","acc","ccc"]))
print(longestCommonPrefix(["a"]))