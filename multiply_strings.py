class Solution:
        def multiply(self, num1: str, num2: str) -> str:
            # If either number is "0", return "0" because the product will also be "0"
            if num1 == "0" or num2 == "0":
                return "0"
        
            # Determine the lengths of the input strings
            length_num1, length_num2 = len(num1), len(num2)
        
            # Create a result list to store the product digits
            result = [0] * (length_num1 + length_num2)
        
            # Reverse process of multiplication, processing digits from the end
            for i in range(length_num1 - 1, -1, -1):
                digit_num1 = int(num1[i])
                for j in range(length_num2 - 1, -1, -1):
                    digit_num2 = int(num2[j])
                    # Add product of current digits to the previously stored value in result list
                    result[i + j + 1] += digit_num1 * digit_num2
        
            # Handle carrying over digits > 9 to the next place
            for i in range(length_num1 + length_num2 - 1, 0, -1):
                result[i - 1] += result[i] // 10  # carry over
                result[i] %= 10                     # keep only the last digit
        
            # Skip leading zeros in the result list
            start_index = 0 if result[0] != 0 else 1
        
            # Convert the result list to string
            return "".join(str(digit) for digit in result[start_index:])
        
