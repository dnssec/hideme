import webbrowser

def do_pop_all(first_name, last_name):
    # This function would populate all fields, but in a headless environment, it's not applicable.
    print(f"Populating all fields with First Name: {first_name}, Last Name: {last_name}")

def do_search(site_key, first_name, last_name):
    url_templates = {
        'TruePeople': 'https://www.truepeoplesearch.com/results?name={first_name}%20{last_name}',
        'FastPeople': 'https://www.fastpeoplesearch.com/name/{first_name}-{last_name}',
        'Nuwber': 'https://nuwber.com/search?name={first_name}%20{last_name}',
        'XLEK': 'https://xlek.com/search_results.php?fname={first_name}&lname={last_name}&locations:all',
        'Cubib': 'https://cubib.com/search_results.php?fname={first_name}&lname=&{last_name}&locations:all',
        'FamilyTreeNow': 'https://www.familytreenow.com/search/genealogy/results?first&{first_name}&last=&{last_name}',
        'Intelius': 'https://www.intelius.com/people-search/&{first_name}&-&{last_name}',
        'Radaris': 'https://radaris.com/p/{first_name}&/&{last_name}',
        'CyberBackgroundChecks': 'https://www.cyberbackgroundchecks.com/people/{first_name}&-&{last_name}',
        'Spytox': 'https://www.spytox.com/people/search?name= {first_name}&+ &{last_name}',
        # Add all other site templates here
    }
    
    url = url_templates.get(site_key).format(first_name=first_name, last_name=last_name)
    webbrowser.open(url, new=2)

def do_all(first_name, last_name):
    site_keys = [
        'TruePeople',
        'FastPeople',
        'Nuwber',
        'XLEK',
        'Cubib',
        'FamilyTreeNow',
        'Intelius',
        'Radaris'
        'CyberBackgroundChecks'
        'Spytox'
        # Add all other site keys here
    ]
    
    for site_key in site_keys:
        do_search(site_key, first_name, last_name)

# Example usage:

# Simulating the form submission for doPopAll
do_pop_all("John", "Doe")

# Simulating individual form submissions
do_search("TruePeople", "John", "Doe")
do_search("FastPeople", "John", "Doe")

# Simulating 'Submit All' button
do_all("John", "Doe")

