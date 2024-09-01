import requests
from colours import print_green
from pprint import pprint

def get_vulns_by_package(package, version):
    url = "https://api.osv.dev/v1/query"
    data = {
        "package": {"name": f"{package}"},
        "version": f"{version}"
    }

    # send POST request with json data
    response = requests.post(url, json=data).json()
    # print(response)
    if response == {}:
        print_green("\nNo known vulnerabilities.")
        return []
    
    vs = []
    # Get the vulnerabilities
    vulns = response['vulns']

    for vuln in vulns:   

        if 'summary' in vuln:
            summary = vuln['summary']
        else:
            summary = 'Summary cannot be provided.'
        v = {
            'cve': vuln['aliases'][0],
            'summary': summary,
        }

        # Grab the ECOSYSTEM events if any
        events = []
        ranges = vuln['affected'][0]['ranges']
        for r in ranges:
            if r['type'] == 'ECOSYSTEM':
                events = r['events']
                break
        
        # Grab the fixed version, if events was found
        for e in events:
            if 'fixed' in e:
                v['fixed'] = e['fixed']

        if 'fixed' not in v:
            v['fixed'] = 'No fix avaiable.'


        # Grab severity from database_specific, if available
        database_specific = vuln['database_specific'] \
            if 'database_specific' in vuln \
            else None

        if database_specific and 'severity' in database_specific:
            # Get the severity
            v['severity'] = database_specific['severity']
        else:
            v['severity'] = 'No severity available.'



        vs.append(v)

    return vs
