from threading import Semaphore
from typing import Callable

class ZeroEvenOdd:
    def __init__(self, n: int):
        self.n = n
        self.zero_semaphore = Semaphore(1)  # A semaphore for allowing 'zero' to be printed
        self.even_semaphore = Semaphore(0)  # A semaphore for allowing 'even' numbers to be printed
        self.odd_semaphore = Semaphore(0)   # A semaphore for allowing 'odd' numbers to be printed

    def zero(self, print_number: Callable[[int], None]) -> None:
        """
        Prints 'zero' n times and alternates the control between printing odd and even numbers
        :param print_number: The function to call to print the number
        """
        for i in range(self.n):
            self.zero_semaphore.acquire()  # Wait for the zero semaphore to be released
            print_number(0)                # Print zero

            # Determine if the next number after zero should be odd or even
            if i % 2 == 0:                 # If 'i' is even, the next number should be odd
                self.odd_semaphore.release()  # Allow the odd method to print an odd number
            else:                           # If 'i' is odd, the next number should be even
                self.even_semaphore.release()  # Allow the even method to print an even number

    def even(self, print_number: Callable[[int], None]) -> None:
        """
        Prints the even numbers starting from 2 to n
        :param print_number: The function to call to print the number
        """
        for i in range(2, self.n + 1, 2):
            self.even_semaphore.acquire()  # Wait for the even semaphore to be released 
            print_number(i)                # Print the even number
            self.zero_semaphore.release()  # Allow the zero method to print zero again

    def odd(self, print_number: Callable[[int], None]) -> None:
        """
        Prints the odd numbers starting from 1 to n
        :param print_number: The function to call to print the number
        """
        for i in range(1, self.n + 1, 2):
            self.odd_semaphore.acquire()   # Wait for the odd semaphore to be released
            print_number(i)                # Print the odd number
            self.zero_semaphore.release()  # Allow the zero method to print zero again
        
        
  
        
        
