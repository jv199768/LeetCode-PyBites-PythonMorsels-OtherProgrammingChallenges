#include <vector>

class Bank {
public:
    // Use underscore naming for private member variables to distinguish from method parameters
    std::vector<long long> _balances;
    int _numAccounts; // Variable to store the number of accounts

    // Constructor to initialize the Bank object with a list of balances
    Bank(std::vector<long long>& balances) {
        _balances = balances;
        _numAccounts = balances.size();
    }

    // Transfer method - moves 'money' from 'account1' to 'account2'
    bool transfer(int account1, int account2, long long money) {
        // Check if either of the account numbers are invalid or if the balance is insufficient
        if (account1 > _numAccounts || account2 > _numAccounts || _balances[account1 - 1] < money) {
            return false;
        }
        // Perform the transfer by adjusting the balances of both accounts
        _balances[account1 - 1] -= money;
        _balances[account2 - 1] += money;
        return true;
    }

    // Deposit method - adds 'money' to 'account'
    bool deposit(int account, long long money) {
        // Check if the account number is invalid
        if (account > _numAccounts) {
            return false;
        }
        // Increase the balance of the account by 'money'
        _balances[account - 1] += money;
        return true;
    }

    // Withdraw method - deducts 'money' from 'account'
    bool withdraw(int account, long long money) {
        // Check if the account number is invalid or if the balance is insufficient
        if (account > _numAccounts || _balances[account - 1] < money) {
            return false;
        }
        // Decrease the balance of the account by 'money'
        _balances[account - 1] -= money;
        return true;
    }
};
