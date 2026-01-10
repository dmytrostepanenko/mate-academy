def check_emails_against_blacklist(emails: list[str], blacklist: set) -> str:
    #  Write code here
    if emails:
        for email in emails:
            if email in blacklist:
                return email
                break
            else:
                return ""
    else:
        return ""


if __name__ == "__main__":
    # emails = ["user@example.com", "spam@blacklist.com", "anotheruser@example.com"]
    # blacklist = {"spam@blacklist.com", "banneduser@example.com"}

    # print(check_emails_against_blacklist(emails, blacklist) == "spam@blacklist.com")

    emails = []
    blacklist = {"spam@blacklist.com", "banneduser@example.com"}

    print(check_emails_against_blacklist(emails, blacklist) == "")
    
