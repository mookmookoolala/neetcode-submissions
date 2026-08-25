class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        full=set()
        for email in emails:
            name,domain = email.split('@')
            clean=name.split("+")[0]
            nice=clean.replace(".", "")
            full.add(nice+"@"+domain)
        return(len(full))
