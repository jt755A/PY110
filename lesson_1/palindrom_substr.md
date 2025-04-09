input: string
output: collection of strings (lists shown in test cases solutions)
rules:
    Explicit requirements:
        - collect each palindrome substring that is 2 or more characters long (palindrome is string that reads the same front to back).
        - checking for palindromes is case-sensitive: 'mom' is palindrome, 'Mom' is not
        - return collection

    Implicit requirements:
        - empty string provided as input returns empty collection
        - where no palindromes found, reutrn empty collection
        - palindromes are returned by descending length: longest first (shorter ones often substring of longer palindroms anyway)
