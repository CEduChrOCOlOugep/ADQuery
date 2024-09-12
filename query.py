import csv
from pyad import adquery


# Define the function to query AD and return results
def query_ad_with_paging(page_size=1000):
    q = adquery.ADQuery()

    # Modify the LDAP query as per your needs
    q.execute_query(
        attributes=["cn", "distinguishedName", "sAMAccountName", "mail"],  # Replace or add more attributes as needed
        where_clause="objectClass='user'",  # Adjust the objectClass or filter as required
        base_dn="DC=yourdomain,DC=com",  # Modify the base DN to your environment
        page_size=page_size
    )

    # Store results in a list
    results = []
    for row in q.get_results():
        results.append(row)

    return results


# Define the function to write the results to a CSV file
def write_to_csv(data, filename="ad_results.csv"):
    if data:
        # Get headers from the first record keys
        headers = data[0].keys()

        # Write to CSV
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)


# Main function to perform AD query and save the results
def main():
    print("Querying Active Directory...")
    ad_results = query_ad_with_paging()

    print(f"Number of records fetched: {len(ad_results)}")
    if ad_results:
        print(f"Saving results to CSV...")
        write_to_csv(ad_results)
        print(f"Results saved to 'ad_results.csv'")


if __name__ == "__main__":
    main()
