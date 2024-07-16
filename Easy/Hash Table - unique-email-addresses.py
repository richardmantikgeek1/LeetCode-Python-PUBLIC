class Solution:
    def numUniqueEmails(self, emails):
        memo = {}
        for email in emails:
            actual_email = self.get_actual_email(email)
            memo[actual_email] = True

        return len(memo.keys())

    def get_actual_email(self, email):
        actual_email = ''
        i = 0
        is_ignored = False
        is_domain_name = False
        while (i < len(email)):
            c = email[i]
            if (not is_domain_name and c == '@'):
                is_ignored = False
                is_domain_name = True
                actual_email += c
            elif (not is_domain_name and c == '.'):
                pass
            elif (not is_domain_name and c == '+'):
                is_ignored = True
            elif (not is_domain_name and is_ignored):
                pass
            else:
                actual_email += c

            i += 1

        return actual_email
    
sol = Solution()
result = sol.get_actual_email('test.email+alex@leetcode.com')
print(result)