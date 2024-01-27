def extract_domain(email):
    return email.split('@')[-1]

def filter_and_sort_emails(n):
    unique_domains = set()

    for _ in range(n):
        email = input()
        if '@' in email:
            domain = extract_domain(email)
            unique_domains.add(domain)

    sorted_domains = sorted(unique_domains)
    return sorted_domains

def main():
    n = int(input())
    sorted_domains = filter_and_sort_emails(n)

    for domain in sorted_domains:
        print(domain)

if __name__ == "__main__":
    main()


