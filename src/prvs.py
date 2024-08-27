import subprocess
import argparse
from colours import print_red, print_yellow, print_bold
from osv_api import get_vulns_by_package

# add options here
parser = argparse.ArgumentParser(
                    prog='Python Requirements Vulnerability Scanner (PRVS)',
                    description='This program outputs all known vulnerabilities for each package specified in the requiremets.txt file',
                    epilog='''python3 prvs.py -p ./requirements.txt''')

parser.add_argument('-p', '--path', default = './requirements.txt', help='Path to the requirements.txt (or whatever you named it) file.')
parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Increase verbosity, show vulnerabilities specifics') # on/off

args = parser.parse_args()

# all vulnerabilities across all packages
vuln_counter = 0

def get_package_version(package_name):
    output = subprocess.run(["pip", "index", "versions", package_name], capture_output=True, text=True)
    latest = output.stdout.split("(")[1].split(")")[0]  
    return latest  

def get_latest_version(package_name):
    output = subprocess.run(["pip", "index", "versions", package_name], capture_output=True, text=True)
    latest = output.stdout.split("(")[1].split(")")[0]  
    return latest  

def print_results(vs, package, verbose):
    # print(vs)
    vulnies_count = len(vs)

    if args.verbose: 
        for v in vs:
            print(f"\nVulnerabilties:")
            print(f"\tVulnerability ID: {v.get('cve')}")
            print(f"\tSummary: {v.get('summary')}")
            print(f"\tFixed in version: {v['fixed']}")
        if vulnies_count == 1:
            print_red(f'\nThis package has {vulnies_count} vulnerability.')
        elif vulnies_count > 1:
            print_red(f'\nThis package has {vulnies_count} vulnerabilities.')
    
    else:
        if vulnies_count == 1:
            print_red(f'\nThis package has {vulnies_count} vulnerability.')
        elif vulnies_count > 1:
            print_red(f'\nThis package has {vulnies_count} vulnerabilities.')
    

    latest_v = get_latest_version(package.split('==')[0])
    
    upgrade_to = "0.0.0.0"
    for v in vs:
        if upgrade_to < v['fixed'] and v['fixed'] != "No fix avaiable.":
            upgrade_to = v['fixed']
    
    if package.split('==')[1] != latest_v:
        print_yellow(f"\n>>> You are using an outdated version. Latest is {latest_v}.")
    
    if upgrade_to > "0.0.0.0":
        print_red(f">>> Consider upgrading to version {upgrade_to} to resolve all known vulnerabilities.\n")
        
    return



new_requirements = []
reqs = open(args.path, 'r')
lines = reqs.readlines()
for line in lines:
    line = line.strip()
    if not line or "#" in line:
        continue
    elif "==" not in str(line): 
        package_name = line
        latest = get_package_version(package_name)
        new_requirements.append(f"{package_name}=={latest}")
    else:
        new_requirements.append(line)

vulny_packages = 0
for package in new_requirements:
    print_bold(f"\n\nPackage found: {package}")
    vs = get_vulns_by_package(package.split("==")[0],package.split("==")[1])
    vuln_counter += len(vs)
    print_results(vs, package, args.verbose)
    if vs != []:
        vulny_packages+=1


print_bold(f'\n>>> {vuln_counter} vulnerabilties found across {vulny_packages} vulnerable packages.')